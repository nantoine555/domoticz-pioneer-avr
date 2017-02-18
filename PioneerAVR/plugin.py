# Pioneer AVR
#
# Author: Olaf Conradi
#
"""
<plugin key="PioneerAVR" name="Pioneer AVR"
        author="Olaf Conradi" version="0.1"
        externallink="https://github.com/oohlaf/domoticz-pioneer-avr">
    <params>
        <param field="Address" label="IP Address"
               default="192.168.1.177"
               width="250px" required="true"/>
        <param field="Port" label="Port"
               default="8102"
               width="50px" required="true"/>
        <param field="Mode6" label="Log Level"
               width="75px">
            <options>
                <option label="Debug" value="DEBUG" default="true"/>
                <option label="Info" value="INFO"/>
                <option label="Warning" value="WARNING"/>
                <option label="Error" value="ERROR"/>
                <option label="Critical" value="CRITICAL"/>
            </options>
        </param>
    </params>
</plugin>
"""
import logging

import Domoticz

from domologger import DomoticzHandler, setup_logging
from pioneer import PioneerDevice, PioneerState


log = logging.getLogger(__name__)


UNITS = {
    'display': 1,
    'listening_mode': 2,
    'playing_mode': 3,
    'main_sound_level': 4,
    'main_volume': 5,
    }


def update_device(unit, n_value, s_value):
    if unit in Devices:
        if (Devices[unit].nValue != n_value
                or Devices[unit].sValue != s_value):
            log.debug('before update device')
            dump_config_to_log(unit)
            Devices[unit].Update(nValue=n_value, sValue=s_value)
            log.debug('after update device')
            dump_config_to_log(unit)


_avr_state = None
_avr_device = None


def onStart():
    global _avr_state
    global _avr_device

    if Parameters['Mode6'] == 'DEBUG':
        Domoticz.Debugging(1)
    else:
        Domoticz.Debugging(0)
    setup_logging(base_path=Parameters['HomeFolder'],
                  root_level=Parameters['Mode6'])

    log.debug('onStart called')

    options = {
        'volume_max': 185,
        'volume_min': 0,
        'volume_db_min': -80.5,
        'volume_db_step': 0.5,
        'volume_slider_max': 121,
        'volume_slider_min': 21,   # -70 dB
        }

    _avr_state = PioneerState(UNITS, options, update_device)
    _avr_device = PioneerDevice(_avr_state)

    if UNITS['display'] not in Devices:
        Domoticz.Device(Name="Display",
                        Unit=UNITS['display'],
                        TypeName="Text",
                        Image=5).Create()
    if UNITS['listening_mode'] not in Devices:
        Domoticz.Device(Name="Listening Mode",
                        Unit=UNITS['listening_mode'],
                        TypeName="Text").Create()
    if UNITS['playing_mode'] not in Devices:
        Domoticz.Device(Name="Playing Listening Mode",
                        Unit=UNITS['playing_mode'],
                        TypeName="Text").Create()
    if UNITS['main_sound_level'] not in Devices:
        Domoticz.Device(Name="Sound Level Main Zone",
                        Unit=UNITS['main_sound_level'],
                        TypeName="Sound Level").Create()
    if UNITS['main_volume'] not in Devices:
        Domoticz.Device(Name="Volume Main Zone",
                        Unit=UNITS['main_volume'],
                        TypeName="Switch",
                        Switchtype=7,
                        Image=8).Create()
    dump_config_to_log()
    Domoticz.Transport('TCP/IP', Parameters['Address'], Parameters['Port'])
    Domoticz.Protocol('Line')
    Domoticz.Heartbeat(30)
    Domoticz.Connect()


def onStop():
    log.debug('onStop called')


def onConnect(Status, Description):
    log.debug('onConnect called\nStatus: %s\nDescription: %s',
              Status, Description)
    if Status == 0:
        _avr_device.connected = True
        Domoticz.Send(Message='?P\r')
        onHeartbeat()
    else:
        _avr_device.connected = False


def onMessage(Data, Status, Extra):
    if log.isEnabledFor(logging.DEBUG):
        str_data = Data.decode('ASCII', 'ignore')
        log.debug('onMessage called\nData: %s\nStatus: %s',
                  str_data, Status)
    _avr_device.readline(Data)


def onCommand(Unit, Command, Level, Hue):
    log.debug('onCommand called\nUnit: %s\nCommand: %s\nLevel: %s\nHue: %s',
              Unit, Command, Level, Hue)


def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    log.debug('onNotification called\nName: %s\nSubject: %s\nText: %s\n'
              'Status: %s\nPriority: %s\nSound: %s\nImageFile: %s',
              Name, Subject, Text, Status, Priority, Sound, ImageFile)


def onDisconnect():
    log.debug('onDisconnect called')
    _avr_device.connected = False


def onHeartbeat():
    if _avr_device.connected:
        log.debug('onHeartbeat called')
        Domoticz.Send(Message='?V\r')
        Domoticz.Send(Message='?FL\r')
        Domoticz.Send(Message='?S\r')
        Domoticz.Send(Message='?L\r')
        Domoticz.Send(Message='?AST\r')
    else:
        Domoticz.Connect()


def dump_config_to_log(unit=None):
    if log.isEnabledFor(logging.DEBUG):
        def dump_unit(unit):
            msg = 'Device: {}\n' \
                  'Device ID: {}\n' \
                  'Device Name: {}\n' \
                  'Device nValue: {}\n' \
                  'Device sValue: {}\n' \
                  'Device LastLevel: {}'.format(unit,
                                                Devices[unit].ID,
                                                Devices[unit].Name,
                                                Devices[unit].nValue,
                                                Devices[unit].sValue,
                                                Devices[unit].LastLevel)
            return msg

        if unit is not None:
            log.debug(dump_unit(unit))
        else:
            msg = 'Device Parameters:'
            for x in Parameters:
                if Parameters[x] != '':
                    msg += '\n{}: {}'.format(x, Parameters[x])
            log.debug(msg)
            msg = 'Device count: {}'.format(len(Devices))
            for x in Devices:
                msg += '\n{}'.format(dump_unit(x))
            log.debug(msg)

# Pioneer AVR
#
# Author: Olaf Conradi
#
"""
<plugin key="PioneerAVR" name="Pioneer AVR"
        author="Olaf Conradi" version="0.1">
    <params>
        <param field="Address" label="IP Address"
               default="192.168.1.177"
               width="250px" required="true"/>
        <param field="Port" label="Port"
               default="8102"
               width="50px" required="true"/>
        <param field="Mode6" label="Debug"
               width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"/>
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz

from domoavr import DomoticzAVR
from pioneer import PioneerDevice


UNITS = {
    'display': 1,
    'listening_mode': 2,
    'main_sound_level': 3,
    'main_volume': 4,
    }


def update_device(unit, n_value, s_value):
    if unit in Devices:
        if (Devices[unit].nValue != n_value
                or Devices[unit].sValue != s_value):
            Domoticz.Log('before update device')
            dump_config_to_log()
            Devices[unit].Update(nValue=n_value, sValue=s_value)
            Domoticz.Log('after update device')
            dump_config_to_log()


_avr_state = None
_avr_device = None


def onStart():
    global _avr_state
    global _avr_device

    Domoticz.Log('onStart called')

    options = {
        'volume_max': 185,
        'volume_min': 0,
        'volume_db_min': -80.5,
        'volume_db_step': 0.5,
        'volume_slider_max': 121,
        'volume_slider_min': 21,   # -70 dB
        }

    if Parameters['Mode6'] == 'Debug':
        Domoticz.Debugging(1)
    else:
        Domoticz.Debugging(0)

    _avr_state = DomoticzAVR(UNITS, options, update_device)
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
    Domoticz.Log('onStop called')


def onConnect(Status, Description):
    Domoticz.Log('onConnect called\nStatus: ' + str(Status) +
                 '\nDescription: ' + str(Description))
    if Status == 0:
        _avr_device.connected = True
        Domoticz.Send(Message='?P\r')
        onHeartbeat()
    else:
        _avr_device.connected = False


def onMessage(Data, Status, Extra):
    str_data = Data.decode('ASCII', 'ignore')
    Domoticz.Log('onMessage called\nData: ' + str(str_data) +
                 '\nStatus: ' + str(Status))
    _avr_device.readline(Data)


def onCommand(Unit, Command, Level, Hue):
    Domoticz.Log('onCommand called\nUnit: ' + str(Unit) +
                 '\nCommand: ' + str(Command) +
                 '\nLevel: ' + str(Level) +
                 '\nHue: ' + str(Hue))


def onNotification(Data):
    Domoticz.Log('onNotification called\nData: ' + str(Data))


def onDisconnect():
    Domoticz.Log('onDisconnect called')
    _avr_device.connected = False


def onHeartbeat():
    if _avr_device.connected:
        Domoticz.Log('onHeartbeat called')
        Domoticz.Send(Message='?V\r')
        Domoticz.Send(Message='?FL\r')
    else:
        Domoticz.Connect()


def dump_config_to_log(unit=None):
    msg = ''
    if unit is None:
        msg += 'Device Parameters:\n'
        for x in Parameters:
            if Parameters[x] != '':
                msg += "'" + x + "': '" + str(Parameters[x]) + "'\n"
        msg += 'Device count: ' + str(len(Devices)) + '\n'
        for x in Devices:
            msg += "Device:           " + str(x) + "-" + str(Devices[x]) + '\n'
            msg += "Device ID:       '" + str(Devices[x].ID) + "'\n"
            msg += "Device Name:     '" + Devices[x].Name + "'\n"
            msg += "Device nValue:    " + str(Devices[x].nValue) + '\n'
            msg += "Device sValue:   '" + Devices[x].sValue + "'\n"
            msg += "Device LastLevel: " + str(Devices[x].LastLevel) + '\n'
    else:
        x = unit
        msg += "Device:           " + str(x) + "-" + str(Devices[x]) + '\n'
        msg += "Device ID:       '" + str(Devices[x].ID) + "'\n"
        msg += "Device Name:     '" + Devices[x].Name + "'\n"
        msg += "Device nValue:    " + str(Devices[x].nValue) + '\n'
        msg += "Device sValue:   '" + Devices[x].sValue + "'\n"
        msg += "Device LastLevel: " + str(Devices[x].LastLevel) + '\n'
    Domoticz.Debug(msg)

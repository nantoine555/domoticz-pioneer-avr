import logging


log = logging.getLogger(__name__)


FL_FONT = {}


LISTENING_MODES = {
    '0001': 'Stereo (cyclic)',
    '0009': 'Stereo (direct)',
    '0151': 'Auto Level Control',
    '0003': 'Front Stage Surround Advance Focus',
    '0004': 'Front Stage Surround Advance Wide',
    '0153': 'Retriever Air',
    '0010': 'Standard',
    '0011': '(Two Ch Source)',
    '0013': 'Dolby Pro Logic2 Movie',
    '0018': 'Dolby Pro Logic2x Movie',
    '0014': 'Dolby Pro Logic2 Music',
    '0019': 'Dolby Pro Logic2x Music',
    '0015': 'Dolby Pro Logic2 Game',
    '0020': 'Dolby Pro Logic2x Game',
    '0031': 'Dolby Pro Logic2z Height',
    '0032': 'Wide Surround Movie',
    '0033': 'Wide Surround Music',
    '0012': 'Dolby Pro Logic',
    '0016': 'Neo:6 cinema',
    '0017': 'Neo:6 Music',
    '0028': 'XM HD Surround',
    '0029': 'Neural Surround',
    '0021': '(Multi Ch Source)',
    '0022': '(Multi Ch Source)+Dolby EX',
    '0023': '(Multi Ch Source)+Dolby Pro Logic2x Movie',
    '0024': '(Multi Ch Source)+Dolby Pro Logic2x Music',
    '0034': '(Multi Ch Source)+Dolby Pro Logic2z Height',
    '0035': '(Multi Ch Source)+Wide Surround Movie',
    '0036': '(Multi Ch Source)+Wide Surround Music',
    '0025': 'DTS-ES Neo:6',
    '0026': 'DTS-ES Matrix',
    '0027': 'DTS-ES Discrete',
    '0030': 'DTS-ES 8 Ch Discrete',
    '0100': 'Advances Surround (cyclic)',
    '0101': 'Action',
    '0103': 'Drama',
    '0102': 'Sci-Fi',
    '0105': 'Mono Film',
    '0104': 'Entertainment Show',
    '0106': 'Expanded Theater',
    '0116': 'TV Surround',
    '0118': 'Advanced Game',
    '0117': 'Sports',
    '0107': 'Classical',
    '0110': 'Rock/Pop',
    '0109': 'Unplugged',
    '0112': 'Extended Stero',
    '0113': 'Phones Surround',
    '0050': 'THX (cyclic)',
    '0051': 'Dolby Pro Logic+THX Cinema',
    '0052': 'Dolby Pro Logic II Movie+THX Cinema',
    '0053': 'Neo:6 Cinema+THX Cinema',
    '0054': 'Dolby Pro Logic IIx Movie+THX Cinema',
    '0092': 'Dolby Pro Logic IIz Height+THX Cinema',
    '0055': 'THX Select2 Games',
    '0068': 'THX Cinema (for Two Ch)',
    '0069': 'THX Music (for Two Ch)',
    '0070': 'THX Games (for Two Ch)',
    '0071': 'Dolby Pro Logic II Music+THX Music',
    '0072': 'Dolby Pro Logic IIx Music+THX Music',
    '0093': 'Dolby Pro Logic IIz Height+THX Music',
    '0073': 'Neo:6 Music+THX Music',
    '0074': 'Dolby Pro Logic II Game+THX Games',
    '0075': 'Dolby Pro Logic IIx Game+THX Games',
    '0094': 'Dolby Pro Logic IIz Height+THX Games',
    '0076': 'THX Ultra2 Games',
    '0077': 'Dolby Pro Logic+THX Music',
    '0078': 'Dolby Pro Logic+THX Games',
    '0056': 'THX Cinema (for Multi Ch)',
    '0057': 'THX Surround EX (for Multi Ch)',
    '0058': 'Dolby Pro Logic IIx Movie+THX Cinema (for Multi Ch)',
    '0095': 'Dolby Pro Logic IIz Height+THX Cinema (for Multi Ch)',
    '0059': 'ES Neo:6+THX Cinema (for Multi Ch)',
    '0060': 'ES Matrix+THX Cinema (for Multi Ch)',
    '0061': 'ES Discrete+THX Cinema (for Multi Ch)',
    '0067': 'ES 8 Ch Discrete+THX Cinema (for Multi Ch)',
    '0062': 'THX Select2 Cinema (for Multi Ch)',
    '0063': 'THX Select2 Music (for Multi Ch)',
    '0064': 'THX Select2 Games (for Multi Ch)',
    '0065': 'THX Ultra2 Cinema (for Multi Ch)',
    '0066': 'THX Ultra2 Music (for Multi Ch)',
    '0079': 'THX Ultra2 Games (for Multi Ch)',
    '0080': 'THX Music (for Multi Ch)',
    '0081': 'THX Games (for Multi Ch)',
    '0082': 'Dolby Pro Logic IIx Music+THX Music (for Multi Ch)',
    '0096': 'Dolby Pro Logic IIz Height+THX Music (for Multi Ch)',
    '0083': 'EX+THX Games (for Multi Ch)',
    '0097': 'Dolby Pro Logic IIz Height+THX Games (for Multi Ch)',
    '0084': 'Neo:6+THX Music (for Multi Ch)',
    '0085': 'Neo:6+THX Games (for Multi Ch)',
    '0086': 'ES Matrix+THX Music (for Multi Ch)',
    '0087': 'ES Matrix+THX Games (for Multi Ch)',
    '0088': 'ES Discrete+THX Music (for Multi Ch)',
    '0089': 'ES Discrete+THX Games (for Multi Ch)',
    '0090': 'ES 8 Ch Discrete+THX Music (for Multi Ch)',
    '0091': 'ES 8 Ch Discrete+THX Games (for Multi Ch)',
    '0005': 'Auto Surr/Stream Direct (cyclic)',
    '0006': 'Auto Surround',
    '0152': 'Optimum Surround',
    '0151': 'Auto Level Control',
    '0007': 'Direct',
    '0008': 'Pure Direct',
    }


PLAYING_MODES = {
    '0001': 'Stereo',
    '0002': 'Front Stage Surround Focus',
    '0003': 'Front Stage Surround Wide',
    '0004': 'Retriever Air',
    '0101': 'Dolby Pro Logic IIx Movie',
    '0102': 'Dolby Pro Logic II Movie',
    '0103': 'Dolby Pro Logic IIx Music',
    '0104': 'Dolby Pro Logic II Music',
    '0105': 'Dolby Pro Logic IIx Game',
    '0106': 'Dolby Pro Logic II Game',
    '0107': 'Dolby Pro Logic',
    '0108': 'Neo:6 Cinema',
    '0109': 'Neo:6 Music',
    '010a': 'XM HD Surround',
    '010b': 'Neural Surround',
    '010c': 'Two Ch Straight Decode',
    '010d': 'Dolby Pro Logic IIz Height',
    '010e': 'Wide Surround Movie',
    '010f': 'Wide Surround Music',
    '1101': 'Dolby Pro Logic IIx Movie',
    '1102': 'Dolby Pro Logic IIx Music',
    '1103': 'Dolby Digital EX',
    '1104': 'DTS+Neo:6/DTS-HD+Neo:6',
    '1105': 'ES Matrix',
    '1106': 'ES Discrete',
    '1107': 'DTS-ES 7.1',
    '1108': 'Multi Ch Straight Decode',
    '1109': 'Dolby Pro Logic IIz Height',
    '110a': 'Wide Surround Movie',
    '110b': 'Wide Surround Music',
    '0201': 'Action',
    '0202': 'Drama',
    '0203': 'Sci-Fi',
    '0204': 'Mono Film',
    '0205': 'Entertainment Show',
    '0206': 'Expanded',
    '0207': 'TV Surround',
    '0208': 'Advanced Game',
    '0209': 'Sports',
    '020a': 'Classical',
    '020b': 'Rock/Pop',
    '020c': 'Unplugged',
    '020d': 'Extended Stereo',
    '020e': 'Phones Surround',
    '0301': 'Dolby Pro Logic IIx Movie+THX',
    '0302': 'Dolby Pro Logic II Movie+THX',
    '0303': 'Dolby Pro Logic+THX Cinema',
    '0304': 'Neo:6 Cinema+THX',
    '0305': 'THX Cinema',
    '0306': 'Dolby Pro Logic IIx Music+THX',
    '0307': 'Dolby Pro Logic II Music+THX',
    '0308': 'Dolby Pro Logic+THX Music',
    '0309': 'Neo:6 Music+THX',
    '030a': 'THX Music',
    '030b': 'Dolby Pro Logic IIx Game+THX',
    '030c': 'Dolby Pro Logic II Game+THX',
    '030d': 'Dolby Pro Logic+THX Games',
    '030e': 'THX Ultra2 Games',
    '030f': 'THX Select2 Games',
    '0310': 'THX Games',
    '0311': 'Dolby Pro Logic IIz+THX Cinema',
    '0312': 'Dolby Pro Logic IIz+THX Music',
    '0313': 'Dolby Pro Logic IIz+THX Games',
    '1301': 'THX Surround EX',
    '1302': 'Neo:6+THX Cinema',
    '1303': 'ES Matrix+THX Cinema',
    '1304': 'ES Discrete+THX Cinema',
    '1305': 'ES 7.1+THX Cinema',
    '1306': 'Dolby Pro Logic IIx Movie+THX',
    '1307': 'THX Ultra2 Cinema',
    '1308': 'THX Select2 Cinema',
    '1309': 'THX Cinema',
    '130a': 'Neo:6+THX Music',
    '130b': 'ES Matrix+THX Music',
    '130c': 'ES Discrete+THX Music',
    '130d': 'ES 7.1+THX Music',
    '130e': 'Dolby Pro Logic IIx Music+THX',
    '130f': 'THX Ultra2 Music',
    '1310': 'THX Select2 Music',
    '1311': 'THX Music',
    '1312': 'Neo:6+THX Games',
    '1313': 'ES Matrix+THX Games',
    '1314': 'ES Discrete+THX Games',
    '1315': 'ES 7.1+THX Games',
    '1316': 'Dolby Digital EX+THX Games',
    '1317': 'THX Ultra2 Games',
    '1318': 'THX Select2 Games',
    '1319': 'THX Games',
    '131a': 'Dolby Pro Logic IIz+THX Cinema',
    '131b': 'Dolby Pro Logic IIz+THX Music',
    '131c': 'Dolby Pro Logic IIz+THX Games',
    '0401': 'Stereo',
    '0402': 'Dolby Pro Logic II Movie',
    '0403': 'Dolby Pro Logic IIx Movie',
    '0404': 'Neo:6 Cinema',
    '0405': 'Auto Surround Straight Decode',
    '0406': 'Dolby Digital EX',
    '0407': 'Dolby Pro Logic IIx Movie',
    '0408': 'DTS+Neo:6',
    '0409': 'ES Matrix',
    '040a': 'ES Discrete',
    '040b': 'DTS-ES 7.1',
    '040c': 'XM HD Surround',
    '040d': 'Neural Surround',
    '040e': 'Retriever Air',
    '0501': 'Stereo',
    '0502': 'Dolby Pro Logic II Movie',
    '0503': 'Dolby Pro Logic IIx Movie',
    '0504': 'Neo:6 Cinema',
    '0505': 'Auto Level Control Straight Decocde',
    '0506': 'Dolby Digital EX',
    '0507': 'Dolby Pro Logic IIx Movie',
    '0508': 'DTS+Neo:6',
    '0509': 'ES Matrix',
    '050a': 'ES Discrete',
    '050b': 'DTS-ES 7.1',
    '050c': 'XM HD Surround',
    '050d': 'Neural Sournd',
    '050e': 'Retriever Air',
    '0601': 'Stereo',
    '0602': 'Dolby Pro Logic II Movie',
    '0603': 'Dolby Pro Logic IIx Movie',
    '0604': 'Neo:6 Cinema',
    '0605': 'Stream Direct Nprmal Straight Decocde',
    '0606': 'Dolby Digital EX',
    '0607': 'Dolby Pro Logic IIx Movie',
    '0608': '',
    '0609': 'ES Matrix',
    '060a': 'ES Discrete',
    '060b': 'DTS-ES 7.1',
    '0701': 'Stream Direct Pure Two Ch',
    '0702': 'Dolby Pro Logic II Movie',
    '0703': 'Dolby Pro Logic IIx Movie',
    '0704': 'Neo:6 Cinema',
    '0705': 'Stream Direct Nprmal Straight Decocde',
    '0706': 'Dolby Digital EX',
    '0707': 'Dolby Pro Logic IIx Movie',
    '0708': '',
    '0709': 'ES Matrix',
    '070a': 'ES Discrete',
    '070b': 'DTS-ES 7.1',
    '0881': 'Optimum',
    '0e01': 'HDMI Through',
    '0f01': 'Multi Ch In',
    }


AUDIO_SIGNALS = {
    '00': 'Analog',
    '01': 'Analog',
    '02': 'Analog',
    '03': 'PCM',
    '04': 'PCM',
    '05': 'Dobly Digital',
    '06': 'DTS',
    '07': 'DTS-ES Matrix',
    '08': 'DTS-ES Discrete',
    '09': 'DTS 96/24',
    '10': 'DTS 96/24 ES Matrix',
    '11': 'DTS 96/24 ES Discrete',
    '12': 'MPEG-2 AAC',
    '13': 'WMA9 Pro',
    '14': 'DSD->PCM',
    '15': 'HDMI Through',
    '16': 'Dolby Digital Plus',
    '17': 'Dolby TrueHD',
    '18': 'DTS Express',
    '19': 'DTS-HD Master Audio',
    '20': 'DTS-HD High Resolution',
    '21': 'DTS-HD High Resolution',
    '22': 'DTS-HD High Resolution',
    '23': 'DTS-HD High Resolution',
    '24': 'DTS-HD High Resolution',
    '25': 'DTS-HD High Resolution',
    '26': 'DTS-HD High Resolution',
    '27': 'DTS-HD Master Audio',
    }


# In Hz
AUDIO_FREQUENCIES = {
    '00': 32000,
    '01': 44100,
    '02': 48000,
    '03': 88200,
    '04': 96000,
    '05': 176400,
    '06': 192000,
    }


def build_fl_font():
    for i, j in zip(range(5, 13),
                    [0x0044, 0x0044, 0x01C0, 0x01C1,
                     0x25C0, 0x25B6, 0x2661, 0x2024]):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(j)
    for i, j in zip(range(16, 26), range(0x2070, 0x207A)):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(j)
    for i in range(32, 96):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(i)
    for i in range(97, 127):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(i)
    for i, j in zip(range(128, 134),
                    [0x0152, 0x0153, 0x0132, 0x0133, 0x03C0, 0x2213]):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(j)
    for i, j in zip(range(140, 146),
                    [0x2190, 0x2191, 0x2192, 0x2193, 0x271A, 0x266A]):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(j)
    for i in range(161, 256):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(i)
    for i, j in zip([15, 31, 96, 127],
                    [0x03A9, 0x203E, 0x2551, 0x2588]):
        idx = format(i, '02X')
        FL_FONT[idx] = chr(j)


class PioneerState():
    def __init__(self, units, options, update_device):
        # Config
        self._units = units
        self._options = options
        self._update_device = update_device
        # State
        self._connected = False
        self._display = ''
        self._mute = False
        self._power = False
        self._volume = options['volume_min']
        self._volume_db = options['volume_db_min']
        self._listening_mode = ''
        self._playing_mode = ''

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, value):
        self._connected = value

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, text):
        self._display = text
        self._update_device(self._units['display'],
                            0,
                            str(self._display))

    @property
    def mute(self):
        return self._mute

    @mute.setter
    def mute(self, value):
        self._mute = value
        slider = self.volume_to_slider(self._volume)
        if value:
            self._update_device(self._units['main_sound_level'],
                                0,
                                'mute')
            self._update_device(self._units['main_volume'],
                                0x01,   # Switch On
                                str(slider))
        else:
            self._update_device(self._units['main_sound_level'],
                                0,
                                str(self._volume_db))
            self._update_device(self._units['main_volume'],
                                0x00,   # Switch Off
                                str(slider))

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, level):
        self._volume = level
        self._volume_db = round(self._options['volume_db_step'] * level +
                                self._options['volume_db_min'], 1)
        slider = self.volume_to_slider(level)
        self._update_device(self._units['main_sound_level'],
                            0,
                            str(self._volume_db))
        self._update_device(self._units['main_volume'],
                            0x02,   # Set Level
                            str(slider))

    def volume_to_slider(self, level):
        if level > self._options['volume_slider_max']:
            slider = 100
        elif level < self._options['volume_slider_min']:
            slider = 0
        else:
            slider = round((level - self._options['volume_slider_min']) *
                           100 /
                           (self._options['volume_slider_max'] -
                            self._options['volume_slider_min']), 0)
        return slider

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def listening_mode(self):
        return self._listening_mode

    @listening_mode.setter
    def listening_mode(self, mode):
        self._listening_mode = mode
        self._update_device(self._units['listening_mode'],
                            0,
                            str(self.listening_mode_name))

    @property
    def listening_mode_name(self):
        try:
            name = LISTENING_MODES[self._listening_mode]
        except KeyError:
            log.warning('Unknown listening mode %s', mode)
            name = ''
        return name

    @property
    def playing_mode(self):
        return self._playing_mode

    @playing_mode.setter
    def playing_mode(self, mode):
        self._playing_mode = mode
        self._update_device(self._units['playing_mode'],
                            0,
                            str(self.playing_mode_name))

    @property
    def playing_mode_name(self):
        try:
            name = PLAYING_MODES[self._playing_mode]
        except KeyError:
            log.warning('Unknown playing listening mode %s', mode)
            name = ''
        return name

    @property
    def input_signal(self):
        return self._input_signal

    @input_signal.setter
    def input_signal(self, signal):
        self._input_signal = signal

    @property
    def input_frequency(self):
        return self._input_frequency

    @input_frequency.setter
    def input_frequency(self, frequency):
        self._input_signal = frequency

    @property
    def input_channels(self):
        return self._input_channels

    @input_channels.setter
    def input_channels(self, channel):
        self._input_channels = channel

    @property
    def output_channels(self):
        return self._output_channels

    @output_channels.setter
    def output_channels(self, channel):
        self._output_channels = channel


class PioneerDevice():
    def __init__(self, state):
        self._state = state
        self._response_codes = {
            'VOL': self._parse_volume,
            'FL': self._parse_display,
            'PWR': self._parse_power,
            'SR': self._parse_listening_mode,
            'LM': self._parse_playing_mode,
            'AST': self._parse_audio_mode,
            }
        if not FL_FONT:
            build_fl_font()

    @property
    def connected(self):
        return self._state.connected

    @connected.setter
    def connected(self, value):
        self._state.connected = value

    def readline(self, data):
        data = data.decode('ASCII', 'ignore').strip()
        if not data:
            return False
        elif data.startswith('E'):
            log.error('Error reading response %s', data)
            return False
        elif data.startswith('B00'):
            log.warning('Too busy to read response %s', data)
            return False
        for prefix, function in self._response_codes.items():
            if data.startswith(prefix):
                function(data)
                return True

    def _parse_power(self, data):
        param = data[3:4]
        if param == '0':
            self._state.power = True
        else:
            self._state.power = False

    def _parse_volume(self, data):
        self._state.volume = int(data[3:6])

    def _parse_display(self, data):
        display = ''
        for i in range(4, 32, 2):
            char = data[i:i+2]
            try:
                display += FL_FONT[char]
            except KeyError:
                display += ' '
        self._state.display = display

    def _parse_listening_mode(self, data):
        mode = data[2:6]
        log.debug('Listening mode %s', mode)
        self._state.listening_mode = mode

    def _parse_playing_mode(self, data):
        mode = data[2:6]
        log.debug('Playing listening mode %s', mode)
        self._state.playing_mode = mode

    def _parse_audio_mode(self, data):
        on_off = {'0': False, '1': True}
        input_signal = data[3:5]
        input_frequency = data[5:7]
        input_channels = {
            'L': on_off[data[7]],
            'C': on_off[data[8]],
            'R': on_off[data[9]],
            'SL': on_off[data[10]],
            'SR': on_off[data[11]],
            'SBL': on_off[data[12]],
            'S': on_off[data[13]],
            'SBR': on_off[data[14]],
            'LFE': on_off[data[15]],
            'FHL': on_off[data[16]],
            'FHR': on_off[data[17]],
            'FWL': on_off[data[18]],
            'FWR': on_off[data[19]],
            'XL': on_off[data[20]],
            'XC': on_off[data[21]],
            'XR': on_off[data[22]],
            }
        output_channels = {
            'L': on_off[data[23]],
            'C': on_off[data[24]],
            'R': on_off[data[25]],
            'SL': on_off[data[26]],
            'SR': on_off[data[27]],
            'SBL': on_off[data[28]],
            'SB': on_off[data[29]],
            'SBR': on_off[data[30]],
            'SW': on_off[data[31]],
            'FHL': on_off[data[32]],
            'FHR': on_off[data[33]],
            'FWL': on_off[data[34]],
            'FWR': on_off[data[35]],
            }
        self._state.input_signal = input_signal
        self._state.input_frequency = input_frequency
        self._state.input_channels = input_channels
        self._state.output_channels = output_channels

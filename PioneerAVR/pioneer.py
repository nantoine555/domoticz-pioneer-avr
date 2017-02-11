FL_FONT = {}


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


class PioneerDevice():
    def __init__(self, state):
        self._state = state
        self._response_codes = {
            'VOL': self._parse_volume,
            'FL': self._parse_display,
            'PWR': self._parse_power,
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
            return False
        elif data.startswith('B00'):
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

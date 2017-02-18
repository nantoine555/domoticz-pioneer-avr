from pioneer import LISTENING_MODES, PLAYING_MODES


class DomoticzAVR():
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

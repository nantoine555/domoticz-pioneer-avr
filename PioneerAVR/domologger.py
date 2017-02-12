import logging


class DomoticzHandler(logging.Handler):
    def __init__(self, domoticz_module, level=logging.NOTSET):
        logging.Handler.__init__(self, level)
        self._domoticz = domoticz_module

    def emit(self, record):
        try:
            msg = self.format(record)
            if record.levelno <= logging.DEBUG:
                self._domoticz.Debug(msg)
            elif record.levelno <= logging.WARNING:
                self._domoticz.Log(msg)
            else:
                self._domoticz.Error(msg)
        except Exception:
            self.handleError(record)

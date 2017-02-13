import json
import logging
import logging.config
import os

from Domoticz import Debug, Log, Error


log = logging.getLogger(__name__)


def setup_logging(base_path, log_config_file, root_level='DEBUG'):
    if not os.path.isabs(log_config_file):
        log_config_file = os.path.join(base_path, log_config_file)
    if os.path.exists(log_config_file):
        with open(log_config_file, 'rt') as f:
            config = json.load(f)
        for handler in config['handlers']:
            try:
                setting = config['handlers'][handler]['filename']
            except KeyError:
                continue
            if not os.path.isabs(setting):
                setting = os.path.join(base_path, setting)
                config['handlers'][handler]['filename'] = setting
        config['root']['level'] = root_level
        try:
            logging.config.dictConfig(config)
        except (ValueError, TypeError, AttributeError, ImportError):
            log.exception('Error loading logging configuration '
                          'from file %s', log_config_file)


class DomoticzHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        logging.Handler.__init__(self, level)

    def emit(self, record):
        try:
            msg = self.format(record)
            if record.levelno <= logging.DEBUG:
                Debug(msg)
            elif record.levelno <= logging.WARNING:
                Log(msg)
            else:
                Error(msg)
        except Exception:
            self.handleError(record)

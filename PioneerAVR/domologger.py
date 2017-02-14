import json
import logging
import logging.config
import os

from Domoticz import (Debug as DDebug,
                      Log as DLog,
                      Error as DError)


log = logging.getLogger(__name__)


def setup_logging(log_config_dict=None,
                  log_config_file='logging.json',
                  base_path=None,
                  root_level='DEBUG'):
    def fallback_logging():
        root_log = logging.getLogger()
        root_log.setLevel(logging.DEBUG)
        root_log.addHandler(DomoticzHandler())

    def make_abs_file_handlers(base_path, config):
        for handler in config['handlers']:
            try:
                setting = config['handlers'][handler]['filename']
            except KeyError:
                continue
            if not os.path.isabs(setting):
                setting = os.path.join(base_path, setting)
                config['handlers'][handler]['filename'] = setting
        return config

    if log_config_dict is None and log_config_file is not None:
        if base_path is not None and not os.path.isabs(log_config_file):
            log_config_file = os.path.join(base_path, log_config_file)
        try:
            with open(log_config_file, 'rt') as f:
                try:
                    log_config_dict = json.load(f)
                except:
                    fallback_logging()
                    log.exception('Error loading JSON log configuration '
                                  'from file %s', log_config_file)
                    return
        except OSError:
            fallback_logging()
            log.error('Could not open log configuration file %s',
                      log_config_file)
            return

    if log_config_dict is not None:
        if base_path is not None:
            log_config_dict = make_abs_file_handlers(base_path, log_config_dict)
        if root_level is not None:
            log_config_dict['root']['level'] = root_level
        try:
            logging.config.dictConfig(log_config_dict)
        except (ValueError, TypeError, AttributeError, ImportError):
            fallback_logging()
            log.exception('Error loading logging configuration')
    else:
        fallback_logging()
        log.error('No logging configuration given')


class DomoticzHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        logging.Handler.__init__(self, level)

    def emit(self, record):
        try:
            msg = self.format(record)
            if record.levelno <= logging.DEBUG:
                DDebug(msg)
            elif record.levelno <= logging.WARNING:
                DLog(msg)
            else:
                DError(msg)
        except Exception:
            self.handleError(record)

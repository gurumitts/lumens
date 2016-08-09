import logging
from logging.config import fileConfig
import web
from lumens import Lumens


def start():
    fileConfig('conf/log.conf')
    logging.getLogger('lumens').log(logging.DEBUG, 'Log setup complete')
    _lumens = Lumens()

    web.start(_lumens)



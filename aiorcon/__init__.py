import logging

from .rcon import RCON
from .exceptions import (RCONError, RCONAuthenticationError, RCONConnectionError, RCONTimeoutError,
                        RCONClosedError, RCONCommunicationError, RCONMessageError, RCONStateError)
__version__ = '0.6.8'

log = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: %(message)s',
                    datefmt="[%d/%m/%Y %H:%M]")

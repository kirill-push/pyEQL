# logging system
"""Create a logging system using Python's built-in module.

Each module within pyEQL has its own logger, with a StreamHandler attached to it that
directs formatted messages to standard output. This is intended to facilitate the use
of pyEQL as an interactive console program, at the expense of some flexibility when
using it as a true library in another application.

The default logging levels are mapped to pyEQL events as follows:

DEBUG       -   detailed messages about function execution including methods used, data sources,
                temperature adjustments, etc.
INFO        -   Messages indicating calculation steps, function calls, etc.
WARNING     -   assumptions or limitations of module output
ERROR       -   Module could not complete a task due to invalid input or other problem
CRITICAL    -   not used

:copyright: 2013-2023 by Ryan S. Kingsbury
:license: LGPL, see LICENSE for more details.

"""
import logging

# courtesy https://calmcode.io/logging/format.html

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
handler = logging.StreamHandler()

# the formatter determines what our logs will look like
fmt = "%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s"
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger.addHandler(handler)
# use rich for pretty log formatting, if installed
try:
    from rich.logging import RichHandler

    logger.addHandler(RichHandler(rich_tracebacks=True))
except ImportError:
    pass

logger.setLevel(logging.WARNING)


# define a log filter to emit only unique log messages
class Unique(logging.Filter):
    """Messages are allowed through just once.
    The 'message' includes substitutions, but is not formatted by the
    handler. If it were, then practically all messages would be unique!
    """

    def __init__(self, name=""):
        logging.Filter.__init__(self, name)
        self.reset()

    def reset(self):
        """Act as if nothing has happened."""
        self.__logged = {}

    def filter(self, rec):
        """logging.Filter.filter performs an extra filter on the name."""
        return logging.Filter.filter(self, rec) and self.__is_first_time(rec)

    def __is_first_time(self, rec):
        """Emit a message only once."""
        msg = rec.msg % (rec.args)
        if msg in self.__logged:
            self.__logged[msg] += 1
            return False
        self.__logged[msg] = 1
        return True

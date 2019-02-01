import threading
import math
from sim import _ShouldCloseWrapper
from sim import _get_bodies
from sim import _Body


class _LogicThread(threading.Thread):
    def __init__(self, should_close):
        super(_LogicThread, self).__init__()
        self.m_should_close = should_close

    def run(self):
        while not self.m_should_close.m_should_close:
            pass

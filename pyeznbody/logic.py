import threading
import math
import time


class _LogicThread(threading.Thread):
    def __init__(self, should_close):
        super(_LogicThread, self).__init__()
        self.m_should_close = should_close

    def run(self):
        self.last_time = time.time()
        while not self.m_should_close.m_should_close:
            self.delta, self.last_time = time.time() - self.last_time, time.time()

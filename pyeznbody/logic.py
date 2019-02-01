import threading
import math
import time

G = 0.001  # 6.67 * 10**(-11)
E = 0.001


class _LogicThread(threading.Thread):
    def __init__(self, should_close, get_bodies):
        super(_LogicThread, self).__init__()
        self.m_should_close = should_close
        self.m_get_bodies = get_bodies

    def run(self):
        self.last_time = time.time()
        while not self.m_should_close.m_should_close:
            self.delta, self.last_time = time.time() - self.last_time, time.time()
            for b in self.m_get_bodies():
                a_x = 0
                a_y = 0
                for ob in self.m_get_bodies():
                    if b is not ob:
                        r2 = (b.m_pos[0] - ob.m_pos[0])**2 + \
                            (b.m_pos[1] - ob.m_pos[1])**2
                        a_x += (-1) * G * \
                            (b.m_pos[0] - ob.m_pos[0]) / (r2**2+E)
                        a_y += (-1) * G * \
                            (b.m_pos[1] - ob.m_pos[1]) / (r2**2+E)
                b.m_vel[0] = b.m_vel[0] + self.delta * a_x
                b.m_vel[1] = b.m_vel[1] + self.delta * a_y

            for b in self.m_get_bodies():
                b.m_pos[0], b.m_pos[1] = b.m_pos[0] + b.m_vel[0] * \
                    self.delta, b.m_pos[1] + b.m_vel[1] * self.delta

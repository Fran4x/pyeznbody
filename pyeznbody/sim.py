import window

bodies = []
m_resolution = [0, 0]


class _Body:
    def __init__(self, pos):
        self.m_pos = pos
        self.m_vel = (0, 0)


class _ShouldCloseWrapper:

    def __init__(self):
        self.m_should_close = False


def init(resolution=[640, 480]):
    should_close = _ShouldCloseWrapper()
    global m_resolution
    m_resolution = resolution
    global graphicsThread
    graphicsThread = window._GraphicsThread(
        resolution, _yield_screen_body_pos, should_close)
    graphicsThread.start()
    global bodies
    bodies = []


def add_body(pos):
    bodies.append(_Body(pos))


def _yield_screen_body_pos():
    for b in bodies:
        yield ((int((b.m_pos[0]+1)/2 * m_resolution[0]),
                int((b.m_pos[1]+1)/2 * m_resolution[1])))

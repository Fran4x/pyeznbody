import pyeznbody.window
import pyeznbody.logic

bodies = []
m_resolution = [0, 0]


class _Body:
    def __init__(self, pos, vel=(0, 0)):
        self.m_pos = pos
        self.m_vel = vel


class _ShouldCloseWrapper:

    def __init__(self):
        self.m_should_close = False


def init(resolution=[640, 480]):
    should_close = _ShouldCloseWrapper()
    global close

    def close():
        should_close.m_should_close = True

    global m_resolution
    m_resolution = resolution
    global graphics_thread
    graphics_thread = pyeznbody.window._GraphicsThread(
        resolution, _yield_screen_body_pos, should_close)
    graphics_thread.setDaemon(True)
    graphics_thread.start()
    global logic_thread
    logic_thread = pyeznbody.logic._LogicThread(should_close, _get_bodies)
    logic_thread.setDaemon(True)
    logic_thread.start()

    global bodies
    bodies = []


def add_body(pos, vel=(0, 0)):
    bodies.append(_Body(pos, vel))


def _yield_screen_body_pos():
    for b in bodies:
        yield ((int((b.m_pos[0]+1)/2 * m_resolution[0]),
                int((b.m_pos[1]+1)/2 * m_resolution[1])))


def _get_bodies():
    return bodies

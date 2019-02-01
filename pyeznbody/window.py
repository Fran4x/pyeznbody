import threading
import pygame
import pygame.locals
import pygame.draw


class _GraphicsThread(threading.Thread):
    def __init__(self, resolution, position_yielder, should_close):
        super(_GraphicsThread, self).__init__()
        self.m_position_yielder = position_yielder
        self.m_should_close = should_close
        pygame.init()
        self.m_screen = pygame.display.set_mode(resolution)

    def run(self):
        while not self.m_should_close.m_should_close:
            self.m_screen.fill((0, 0, 0))

            for p in self.m_position_yielder():
                self._draw_body(p)

            pygame.display.update()
            for e in pygame.event.get():
                if e.type == pygame.locals.QUIT or (e.type == pygame.locals.KEYUP and e.key == pygame.locals.K_ESCAPE):
                    self.m_should_close.m_should_close = True
                    break
        pygame.display.quit()

    def should_close(self):
        return self.m_should_close

    def _draw_body(self, position):
        pygame.draw.circle(self.m_screen, (255, 255, 255), position, 3)

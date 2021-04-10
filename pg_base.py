import pygame
from pg_models import loadHouse, loadCar, loadTire


class PGRenderer:
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)
    background = BLACK

    size = (512, 512)
    title = "PyGame Renderer"

    def __init__(self):
        self.house = loadHouse()
        self.car = loadCar()
        self.tire = loadTire()

    @classmethod
    def run(cls, *args, **kwargs):
        pygame.init()
        instance = cls(*args, **kwargs)
        screen = pygame.display.set_mode(cls.size)
        pygame.display.set_caption(cls.title)

        clock = pygame.time.Clock()
        done = False
        while not done:
            clock.tick(100)
            screen.fill(cls.background)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    done = True
            instance.key_pressed = pygame.key.get_pressed()
            if instance.key_pressed[pygame.K_ESCAPE]:
                done = True
            instance.poll_keys()
            instance.render(screen)
            pygame.display.flip()
        pygame.quit()

    def render(self):
        pass

    def poll_keys(self):
        pass


if __name__ == "__main__":
    PGRenderer.run()

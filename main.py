from lab07.pg_models import Point3D
from pg_base import PGRenderer
import pygame
import numpy as np


class Lab7Renderer(PGRenderer):
    title = "Lab 7: Graphics Implementation"

    def __init__(self):
        super().__init__()
        self.posx = 0.0
        self.posy = 10.0
        self.posz = 60.0
        self.angle = np.pi
        self.toScreen = np.array([
            [512 / 2, 0, 512 / 2],
            [0, -512 / 2, 512 / 2],
            [0, 0, 1]
        ])

    def render(self, screen):
        for i in range(1, 4):
            for line in self.house:
                self.render_house(line, i, -20, False, screen)
                self.render_house(line, i, 20, True, screen)

        transformMatrix = self.get_view()
        self.render_tires(transformMatrix, screen)
        for line in self.car:
            self.render_car(line, transformMatrix, screen)

    def render_house(self, line, i, z, flip, screen):
        sCoord = np.array([[line.start.x + (i * 20)],
                           [line.start.y],
                           [line.start.z + z],
                           [1]
                           ])
        eCoord = np.array([[line.end.x + (i * 20)],
                           [line.end.y],
                           [line.end.z + z],
                           [1]
                           ])

        if flip:
            flipMatrix = np.array([
                [np.cos(np.pi), 0, np.sin(np.pi), 80],
                [0, 1, 0, 0],
                [-np.sin(np.pi), 0, np.cos(np.pi), 40],
                [0, 0, 0, 1]
            ])
            sCoord = flipMatrix.dot(sCoord)
            eCoord = flipMatrix.dot(eCoord)

        sCoord = self.get_view().dot(sCoord)
        eCoord = self.get_view().dot(eCoord)
        sCoord = self.get_projection().dot(sCoord)
        eCoord = self.get_projection().dot(eCoord)
        if self.clip_test(sCoord, eCoord):
            return
        sCoord[0] /= sCoord[3]
        sCoord[1] /= sCoord[3]
        sCoord[2] /= sCoord[3]
        sCoord[3] /= sCoord[3]
        eCoord[0] /= eCoord[3]
        eCoord[1] /= eCoord[3]
        eCoord[2] /= eCoord[3]
        eCoord[3] /= eCoord[3]
        sCoord = sCoord[:3]
        eCoord = eCoord[:3]
        sCoord = self.toScreen.dot(sCoord)
        eCoord = self.toScreen.dot(eCoord)
        startPoint = self.array_to_point3d(sCoord)
        endPoint = self.array_to_point3d(eCoord)

        pygame.draw.line(screen, self.RED, (startPoint.x, startPoint.y), (endPoint.x, endPoint.y))

        return startPoint, endPoint

    def render_car(self, line, transformMatrix, screen):
        sCoord = np.array([[line.start.x],
                           [line.start.y],
                           [line.start.z],
                           [1]
                           ])
        eCoord = np.array([[line.end.x],
                           [line.end.y],
                           [line.end.z],
                           [1]
                           ])
        sCoord = transformMatrix.dot(sCoord)
        eCoord = transformMatrix.dot(eCoord)
        sCoord = self.get_projection().dot(sCoord)
        eCoord = self.get_projection().dot(eCoord)
        if self.clip_test(sCoord, eCoord):
            return
        sCoord[0] /= sCoord[3]
        sCoord[1] /= sCoord[3]
        sCoord[2] /= sCoord[3]
        sCoord[3] /= sCoord[3]
        eCoord[0] /= eCoord[3]
        eCoord[1] /= eCoord[3]
        eCoord[2] /= eCoord[3]
        eCoord[3] /= eCoord[3]
        sCoord = sCoord[:3]
        eCoord = eCoord[:3]
        sCoord = self.toScreen.dot(sCoord)
        eCoord = self.toScreen.dot(eCoord)
        startPoint = self.array_to_point3d(sCoord)
        endPoint = self.array_to_point3d(eCoord)

        pygame.draw.line(screen, self.BLUE, (startPoint.x, startPoint.y), (endPoint.x, endPoint.y))

    def render_tires(self, tMatrix, screen):
        for line in self.tire:
            tire1Start = np.array([[line.start.x],
                                   [line.start.y],
                                   [line.start.z],
                                   [1]
                                   ])
            tire1End = np.array([[line.end.x],
                                 [line.end.y],
                                 [line.end.z],
                                 [1]
                                 ])
            tire2Start = np.array([[line.start.x],
                                   [line.start.y],
                                   [line.start.z],
                                   [1]
                                   ])
            tire2End = np.array([[line.end.x],
                                 [line.end.y],
                                 [line.end.z],
                                 [1]
                                 ])
            tire3Start = np.array([[line.start.x],
                                   [line.start.y],
                                   [line.start.z],
                                   [1]
                                   ])
            tire3End = np.array([[line.end.x],
                                 [line.end.y],
                                 [line.end.z],
                                 [1]
                                 ])
            tire4Start = np.array([[line.start.x],
                                   [line.start.y],
                                   [line.start.z],
                                   [1]
                                   ])
            tire4End = np.array([[line.end.x],
                                 [line.end.y],
                                 [line.end.z],
                                 [1]
                                 ])

            tire1PlacementMatrix = np.array([[1, 0, 0, 2],
                                             [0, 1, 0, -0.3],
                                             [0, 0, 1, -5 / 2],
                                             [0, 0, 0, 1]
                                             ])
            tire2PlacementMatrix = np.array([[1, 0, 0, -2],
                                             [0, 1, 0, -0.3],
                                             [0, 0, 1, -5 / 2],
                                             [0, 0, 0, 1]
                                             ])
            tire3PlacementMatrix = np.array([[1, 0, 0, 2],
                                             [0, 1, 0, -0.3],
                                             [0, 0, 1, 5 / 2],
                                             [0, 0, 0, 1]
                                             ])
            tire4PlacementMatrix = np.array([[1, 0, 0, -2],
                                             [0, 1, 0, -0.3],
                                             [0, 0, 1, 5 / 2],
                                             [0, 0, 0, 1]
                                             ])

            tire1Start = tire1PlacementMatrix.dot(tire1Start)
            tire1End = tire1PlacementMatrix.dot(tire1End)
            tire2Start = tire2PlacementMatrix.dot(tire2Start)
            tire2End = tire2PlacementMatrix.dot(tire2End)
            tire3Start = tire3PlacementMatrix.dot(tire3Start)
            tire3End = tire3PlacementMatrix.dot(tire3End)
            tire4Start = tire4PlacementMatrix.dot(tire4Start)
            tire4End = tire4PlacementMatrix.dot(tire4End)

            tire1Start = tMatrix.dot(tire1Start)
            tire1End = tMatrix.dot(tire1End)
            tire2Start = tMatrix.dot(tire2Start)
            tire2End = tMatrix.dot(tire2End)
            tire3Start = tMatrix.dot(tire3Start)
            tire3End = tMatrix.dot(tire3End)
            tire4Start = tMatrix.dot(tire4Start)
            tire4End = tMatrix.dot(tire4End)

            tire1Start = self.get_projection().dot(tire1Start)
            tire1End = self.get_projection().dot(tire1End)
            tire2Start = self.get_projection().dot(tire2Start)
            tire2End = self.get_projection().dot(tire2End)
            tire3Start = self.get_projection().dot(tire3Start)
            tire3End = self.get_projection().dot(tire3End)
            tire4Start = self.get_projection().dot(tire4Start)
            tire4End = self.get_projection().dot(tire4End)

            if self.clip_test(tire1Start, tire1End):
                continue
            if self.clip_test(tire2Start, tire2End):
                continue
            if self.clip_test(tire3Start, tire3End):
                continue
            if self.clip_test(tire4Start, tire4End):
                continue

            tire1Start[0] /= tire1Start[3]
            tire1Start[1] /= tire1Start[3]
            tire1Start[2] /= tire1Start[3]
            tire1Start[3] /= tire1Start[3]
            tire1End[0] /= tire1End[3]
            tire1End[1] /= tire1End[3]
            tire1End[2] /= tire1End[3]
            tire1End[3] /= tire1End[3]
            tire2Start[0] /= tire2Start[3]
            tire2Start[1] /= tire2Start[3]
            tire2Start[2] /= tire2Start[3]
            tire2Start[3] /= tire2Start[3]
            tire2End[0] /= tire2End[3]
            tire2End[1] /= tire2End[3]
            tire2End[2] /= tire2End[3]
            tire2End[3] /= tire2End[3]
            tire3Start[0] /= tire3Start[3]
            tire3Start[1] /= tire3Start[3]
            tire3Start[2] /= tire3Start[3]
            tire3Start[3] /= tire3Start[3]
            tire3End[0] /= tire3End[3]
            tire3End[1] /= tire3End[3]
            tire3End[2] /= tire3End[3]
            tire3End[3] /= tire3End[3]
            tire4Start[0] /= tire4Start[3]
            tire4Start[1] /= tire4Start[3]
            tire4Start[2] /= tire4Start[3]
            tire4Start[3] /= tire4Start[3]
            tire4End[0] /= tire4End[3]
            tire4End[1] /= tire4End[3]
            tire4End[2] /= tire4End[3]
            tire4End[3] /= tire4End[3]

            tire1Start = tire1Start[:3]
            tire1End = tire1End[:3]
            tire2Start = tire2Start[:3]
            tire2End = tire2End[:3]
            tire3Start = tire3Start[:3]
            tire3End = tire3End[:3]
            tire4Start = tire4Start[:3]
            tire4End = tire4End[:3]

            tire1Start = self.toScreen.dot(tire1Start)
            tire1End = self.toScreen.dot(tire1End)
            tire2Start = self.toScreen.dot(tire2Start)
            tire2End = self.toScreen.dot(tire2End)
            tire3Start = self.toScreen.dot(tire3Start)
            tire3End = self.toScreen.dot(tire3End)
            tire4Start = self.toScreen.dot(tire4Start)
            tire4End = self.toScreen.dot(tire4End)

            tire1S = self.array_to_point3d(tire1Start)
            tire1E = self.array_to_point3d(tire1End)
            tire2S = self.array_to_point3d(tire2Start)
            tire2E = self.array_to_point3d(tire2End)
            tire3S = self.array_to_point3d(tire3Start)
            tire3E = self.array_to_point3d(tire3End)
            tire4S = self.array_to_point3d(tire4Start)
            tire4E = self.array_to_point3d(tire4End)

            pygame.draw.line(screen, self.GREEN, (tire1S.x, tire1S.y), (tire1E.x, tire1E.y))
            pygame.draw.line(screen, self.GREEN, (tire2S.x, tire2S.y), (tire2E.x, tire2E.y))
            pygame.draw.line(screen, self.GREEN, (tire3S.x, tire3S.y), (tire3E.x, tire3E.y))
            pygame.draw.line(screen, self.GREEN, (tire4S.x, tire4S.y), (tire4E.x, tire4E.y))


    def poll_keys(self):
        if self.key_pressed[pygame.K_a]:
            self.posx -= np.cos(self.angle) / 10
            self.posz -= np.sin(self.angle) / 10
        if self.key_pressed[pygame.K_d]:
            self.posx += np.cos(self.angle) / 10
            self.posz += np.sin(self.angle) / 10
        if self.key_pressed[pygame.K_s]:
            self.posx += np.sin(self.angle) / 10
            self.posz -= np.cos(self.angle) / 10
        if self.key_pressed[pygame.K_w]:
            self.posx -= np.sin(self.angle) / 10
            self.posz += np.cos(self.angle) / 10
        if self.key_pressed[pygame.K_q]:
            self.angle += np.pi / 360
        if self.key_pressed[pygame.K_e]:
            self.angle -= np.pi / 360
        if self.key_pressed[pygame.K_r]:
            self.posy += 0.2
        if self.key_pressed[pygame.K_f]:
            self.posy -= 0.2
        if self.key_pressed[pygame.K_h]:
            self.posx = 0
            self.posy = 0
            self.posz = 60
            self.angle = np.pi

    def get_projection(self):
        n = 0.1
        f = 1000.0
        zoomX = 1 / np.tan(np.pi/8)
        zoomY = zoomX
        return np.array([
            [zoomX, 0, 0, 0],
            [0, zoomY, 0, 0],
            [0, 0, (f + n) / (f - n), (-2 * n * f) / (f - n)],
            [0, 0, 1, 0]
        ])

    def get_view(self):
        translation = np.array([
            [1, 0, 0, -self.posx],
            [0, 1, 0, -self.posy],
            [0, 0, 1, -self.posz],
            [0, 0, 0, 1]
        ])
        rotation = np.array([
            [np.cos(self.angle), 0, np.sin(self.angle), 0],
            [0, 1, 0, 0],
            [-np.sin(self.angle), 0, np.cos(self.angle), 0],
            [0, 0, 0, 1]
        ])
        return rotation.dot(translation)

    def array_to_point3d(self, array):
        return Point3D(array[0, 0], array[1, 0], array[2, 0])

    def clip_test(self, start, end):
        if start[0] < -start[3] or start[0] > start[3] or start[1] < -start[3] or \
                start[1] > start[3] or start[2] < -start[3] or start[2] > start[3]:
            return True
        if end[0] < -end[3] or end[0] > end[3] or end[1] < -end[3] or \
                end[1] > end[3] or end[2] < -end[3] or end[2] > end[3]:
            return True
        return False


if __name__ == "__main__":
    Lab7Renderer.run()

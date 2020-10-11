import tkinter as tk
import math
import math_util as mu


class PointRenderer():
    def __init__(self, c, cam):
        self.c = c
        self.w = int(c['width'])
        self.h = int(c['height'])
        self.s = int(max(self.w, self.h) / 2)
        self.cam = cam

    def render(self, points):
        self.c.delete("all")

        self.v = self.cam.rot.rotate(mu.Vector3.forward)
        self.r = self.cam.rot.rotate(mu.Vector3.right)
        self.u = self.cam.rot.rotate(mu.Vector3.up)

        tfov = math.tan(self.cam.fov / 2)

        points_vector = [mu.Vector3(p) - self.cam.pos for p in points]
        points_vector.sort(key=lambda x: x.magnitude(), reverse=True)

        for p in points_vector:
            pv = self.v.dot(p)
            if pv > 0:
                xp = p / pv - self.v
                rad = xp.magnitude() / tfov
                screen_x = 0
                screen_y = 0
                if rad > 0:
                    phi = math.atan2(xp.dot(self.u), xp.dot(self.r))
                    screen_x = rad * math.cos(phi)
                    screen_y = rad * math.sin(phi)
                pos_x = (1 + screen_x) * self.s - \
                    int(max((self.h - self.w) / 2, 0))
                pos_y = (1 - screen_y) * self.s - \
                    int(max((self.w - self.h) / 2, 0))
                self.c.create_oval(pos_x - 3, pos_y - 3,
                                   pos_x + 3, pos_y + 3, fill='white')

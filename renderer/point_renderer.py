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

        points_vector = [mu.Vector3(p) - self.cam.pos for p in points]
        points_vector.sort(key=lambda x: x.magnitude(), reverse=True)

        for vec_p in points_vector:
            vec_v = self.cam.rot.rotate(mu.Vector3([0, 0, -1]))
            vec_r = self.cam.rot.rotate(mu.Vector3([1, 0, 0]))
            vec_u = self.cam.rot.rotate(mu.Vector3([0, 1, 0]))
            pv = vec_v.dot(vec_p)
            if pv > 0:
                vec_xp = vec_p / pv - vec_v
                mag_xp = vec_xp.magnitude()
                rad = mag_xp / (math.tan(self.cam.fov / 2))
                screen_x = 0
                screen_y = 0
                if rad > 0:
                    phi = math.atan2(vec_xp.dot(vec_u), vec_xp.dot(vec_r))
                    screen_x = rad * math.cos(phi)
                    screen_y = rad * math.sin(phi)
                pos_x = (1 + screen_x) * self.s - \
                    int(max((self.h - self.w) / 2, 0))
                pos_y = (1 - screen_y) * self.s - \
                    int(max((self.w - self.h) / 2, 0))
                self.c.create_oval(pos_x - 3, pos_y - 3,
                                   pos_x + 3, pos_y + 3, fill='white')

import tkinter as tk
import math
import math_util as mu


class WireframeRenderer():
    def __init__(self, c, cam, *vargs, **kwargs):
        self.c = c
        self.w = int(c['width'])
        self.h = int(c['height'])
        self.s = int(max(self.w, self.h) / 2)
        self.near = kwargs['near'] if 'near' in kwargs else 0.1
        self.far = kwargs['far'] if 'far' in kwargs else 2000
        self.cam = cam

    def render(self, points, lines):
        self.c.delete("all")

        self.v = self.cam.rot.rotate(mu.Vector3.forward)
        self.r = self.cam.rot.rotate(mu.Vector3.right)
        self.u = self.cam.rot.rotate(mu.Vector3.up)

        self.tfov = math.tan(self.cam.fov / 2)

        points_vector = [mu.Vector3(p) - self.cam.pos for p in points]
        points_code = []
        endpoints = []

        self.ref = [self.r - self.v * self.tfov, self.r + self.v * self.tfov,
                    self.u - self.v * self.tfov, self.u + self.v * self.tfov, self.v, self.v]
        self.ref2 = [0, 0, 0, 0, self.near, self.far]

        # draw axes
        origin = -self.cam.pos
        axis_end = [mu.Vector3(10, 0, 0) + origin,
                    mu.Vector3(0, 10, 0) + origin,
                    mu.Vector3(0, 0, 10) + origin]
        colors = ['#ff0000', '#00ff00', '#0000ff']

        origin_code = self.clip_code(origin)
        axis_info = [[axis_end[i], self.clip_code(
            axis_end[i]), colors[i]] for i in range(3)]

        axis_info.sort(key=lambda x: x[0].magnitude(), reverse=True)

        for ai in axis_info:
            res = self.clip_line([origin, ai[0]], [origin_code, ai[1]])
            if not res is None:
                self.c.create_line(self.project_point(
                    res[0]), self.project_point(res[1]), fill=ai[2])

        for p in points_vector:
            points_code.append(self.clip_code(p))

        for l in lines:
            c = [points_code[l[0]], points_code[l[1]]]
            res = self.clip_line([points_vector[l[0]], points_vector[l[1]]], c)
            if not res is None:
                endpoints.append(res)

        for s in endpoints:
            self.c.create_line(self.project_point(
                s[0]), self.project_point(s[1]), fill='white')

    def project_point(self, p):
        '''
        Returns screen coordinates of a point. Works well if point is projected on screen, otherwise error could be occurred.
        '''
        pv = p.dot(self.v)
        xp = p / pv - self.v
        rad = xp.magnitude() / self.tfov
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
        return [pos_x, pos_y]

    def clip_code(self, p):
        '''
        Returns code according to position, defined by Cohen-Sutherland Algorithm.

        0x1 -> outside right plane
        0x2 -> outside left plane
        0x4 -> outside up plane
        0x8 -> outside down plane
        0x10 -> outside near plane
        0x20 -> outside far plane
        '''
        code = 0
        right_angle = math.atan2(p.dot(self.r), p.dot(self.v))
        up_angle = math.atan2(p.dot(self.u), p.dot(self.v))
        pv = p.dot(self.v)
        if right_angle > self.cam.fov / 2:
            code = code | 1
        if right_angle < -self.cam.fov / 2:
            code = code | 2
        if up_angle > self.cam.fov / 2:
            code = code | 4
        if up_angle < -self.cam.fov / 2:
            code = code | 8
        if pv < self.near:
            code = code | 16
        if pv > self.far:
            code = code | 32
        return code

    def clip_line(self, l, c=None):
        '''
        Returns new points and clip code calculated by Cohen-Sutherland Algorithm.
        Applies Cohen-Sutherland algorithm recursively to get result line by single function call.
        '''
        if c is None:
            c = [self.clip_code(l[0]), self.clip_code(l[1])]
        pick_code = max(c)
        while pick_code > 0:
            for i in range(6):
                if c[0] & c[1]:
                    return None
                if c[0] | c[1] == 0:
                    return l
                pick_code = max(c)
                if pick_code & (1 << i) != 0:
                    t = (-l[1].dot(self.ref[i]) + self.ref2[i]) / \
                        (l[0] - l[1]).dot(self.ref[i])
                    mid = t * l[0] + (1 - t) * l[1]
                    if c[0] & (1 << i) != 0:
                        l[0] = mid
                        c[0] = self.clip_code(l[0]) & ~(1 << i)
                    else:
                        l[1] = mid
                        c[1] = self.clip_code(l[1]) & ~(1 << i)
                    break
        return l

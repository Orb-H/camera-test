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

        vec_v = self.cam.rot.rotate(mu.Vector3([0, 0, -1]))
        vec_r = self.cam.rot.rotate(mu.Vector3([1, 0, 0]))
        vec_u = self.cam.rot.rotate(mu.Vector3([0, 1, 0]))

        tfov = math.tan(self.cam.fov / 2)

        points_vector = [mu.Vector3(p) - self.cam.pos for p in points]
        points_code = []
        endpoints = []

        self.ref = [vec_r - vec_v * tfov, vec_r + vec_v * tfov,
                    vec_u - vec_v * tfov, vec_u + vec_v * tfov, vec_v, vec_v]
        self.ref2 = [0, 0, 0, 0, self.near, self.far]

        # draw axes
        origin = -self.cam.pos
        axis_end = [mu.Vector3(10, 0, 0) + origin,
                    mu.Vector3(0, 10, 0) + origin,
                    mu.Vector3(0, 0, 10) + origin]
        colors = ['#ff0000', '#00ff00', '#0000ff']

        origin_code = self.clip_code(origin, vec_v, vec_r, vec_u)
        axis_info = [[axis_end[i], self.clip_code(axis_end[i], vec_v, vec_r, vec_u), colors[i]]
                     for i in range(3)]

        axis_info.sort(key=lambda x: x[0].magnitude(), reverse=True)

        for ai in axis_info:
            if origin_code & ai[1] == 0:
                res = self.clip_line([origin, ai[0]], [origin_code, ai[1]])
                self.c.create_line(self.project_point(res[0], vec_v, vec_r, vec_u, tfov), self.project_point(
                    res[1], vec_v, vec_r, vec_u, tfov), fill=ai[2])

        # Using Cohen-Sutherland algorithm
        for vec_p in points_vector:
            points_code.append(self.clip_code(vec_p, vec_v, vec_r, vec_u))

        for l in lines:
            c = [points_code[l[0]], points_code[l[1]]]
            if c[0] & c[1] != 0:
                continue
            res = self.clip_line([points_vector[l[0]], points_vector[l[1]]], c)
            endpoints.append([res[0], res[1]])

        for s in endpoints:
            self.c.create_line(self.project_point(s[0], vec_v, vec_r, vec_u, tfov), self.project_point(
                s[1], vec_v, vec_r, vec_u, tfov), fill='white')

    def project_point(self, vec_p, vec_v, vec_r, vec_u, tfov):
        '''
        Returns screen coordinates of a point. Works well if point is projected on screen, otherwise error could be occurred.
        '''
        pv = vec_p.dot(vec_v)
        vec_xp = vec_p / pv - vec_v
        rad = vec_xp.magnitude() / tfov
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
        return [pos_x, pos_y]

    def clip_code(self, vec_p, vec_v, vec_r, vec_u):
        code = 0
        right_angle = math.atan2(vec_p.dot(vec_r), vec_p.dot(vec_v))
        up_angle = math.atan2(vec_p.dot(vec_u), vec_p.dot(vec_v))
        if right_angle > self.cam.fov / 2:
            code = code | 1
        if right_angle < -self.cam.fov / 2:
            code = code | 2
        if up_angle > self.cam.fov / 2:
            code = code | 4
        if up_angle < -self.cam.fov / 2:
            code = code | 8
        if vec_p.dot(vec_v) < self.near:
            code = code | 16
        if vec_p.dot(vec_v) > self.far:
            code = code | 32
        return code

    def clip_line(self, l, c):
        '''
        Returns new points and clip code calculated by Cohen-Sutherland Algorithm.
        '''
        pick_code = max(c[0], c[1])
        while pick_code > 0:
            for i in range(6):
                if pick_code & (1 << i) != 0:
                    t = (-l[1].dot(self.ref[i]) + self.ref2[i]) / \
                        (l[0] - l[1]).dot(self.ref[i])
                    mid = t * l[0] + (1 - t) * l[1]
                    if c[0] & pick_code:
                        l[0] = mid
                        c[0] ^= (1 << i)
                    else:
                        l[1] = mid
                        c[1] ^= (1 << i)
                    break
            pick_code = max(c[0], c[1])
        return [l[0], l[1]]

import math
import tkinter as tk
from math_util import *
import renderer.point_renderer as pr
import renderer.wireframe_renderer as wr
import renderer.polygon_projector as pp


class Camera:
    '''
    A class for camera.
    '''

    def __init__(self, fov, canvas, renderer=None):
        self.fov = fov
        self.pos = Vector3([0, 0, 0])
        self.rot = Quaternion(Vector3([0, 0, 0]))

        self.c = canvas
        self.r = pp.PolygonProjector(canvas, self)

    def render(self):
        if self.c is None or self.r is None:
            return
        self.r.render([[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1], [1, 1, 0]], [
                      [0, 1, 2, 3], [0, 4, 5, 1], [1, 5, 6, 2], [2, 6, 7, 3], [3, 7, 4, 0], [4, 7, 6, 5]])  # simple example

    # Position

    def move(self, amount):
        self.pos += amount

    def move_forward(self, amount):
        self.move(self.rot * Vector3([0, 0, -amount]))

    def move_backward(self, amount):
        self.move_forward(-amount)

    def move_right(self, amount):
        self.move(self.rot * Vector3([amount, 0, 0]))

    def move_left(self, amount):
        self.move_right(-amount)

    def move_up(self, amount):
        self.move(self.rot * Vector3([0, amount, 0]))

    def move_down(self, amount):
        self.move_up(-amount)

    # Rotation

    def rotate(self, amount):
        self.rot = amount * self.rot

    def rotate_up(self, amount):
        axis = self.rot * Vector3([1, 0, 0])
        axis = axis / axis.magnitude() * math.sin(amount)
        self.rotate(Quaternion(
            Vector4([math.cos(amount), axis[0], axis[1], axis[2]])))

    def rotate_down(self, amount):
        self.rotate_up(-amount)

    def rotate_left(self, amount):
        axis = self.rot * Vector3([0, 1, 0])
        axis = axis / axis.magnitude() * math.sin(amount)
        self.rotate(Quaternion(
            Vector4([math.cos(amount), axis[0], axis[1], axis[2]])))

    def rotate_right(self, amount):
        self.rotate_left(-amount)

    def rotate_ccw(self, amount):
        axis = self.rot * Vector3([0, 0, 1])
        axis = axis / axis.magnitude() * math.sin(amount)
        self.rotate(Quaternion(
            Vector4([math.cos(amount), axis[0], axis[1], axis[2]])))

    def rotate_cw(self, amount):
        self.rotate_ccw(-amount)

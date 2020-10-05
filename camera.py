import math
import tkinter as tk
from math_util import *
import renderer.point_renderer as pr


class Camera:
    '''
    A class for camera.
    '''

    def __init__(self, fov, canvas, renderer=None):
        self.fov = fov
        self.pos = Vector([0, 0, 0])
        self.rot = Quaternion(Vector([0, 0, 0]))

        self.c = canvas
        self.r = pr.PointRenderer(canvas, self)

    def render(self):
        if self.c is None or self.r is None:
            return
        self.r.render([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [
                      0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]])  # simple example

    # Position

    def move(self, amount):
        self.pos += amount

    def move_forward(self, amount):
        self.move(self.rot * Vector([0, 0, -amount]))

    def move_backward(self, amount):
        self.move_forward(-amount)

    def move_right(self, amount):
        self.move(self.rot * Vector([amount, 0, 0]))

    def move_left(self, amount):
        self.move_right(-amount)

    def move_up(self, amount):
        self.move(self.rot * Vector([0, amount, 0]))

    def move_down(self, amount):
        self.move_up(-amount)

    # Rotation

    def rotate(self, amount):
        self.rot = amount * self.rot

    def rotate_up(self, amount):
        self.rotate(Quaternion(
            Vector([math.cos(amount), math.sin(amount), 0, 0])))

    def rotate_down(self, amount):
        self.rotate_up(-amount)

    def rotate_left(self, amount):
        self.rotate(Quaternion(
            Vector([math.cos(amount), 0, math.sin(amount), 0])))

    def rotate_right(self, amount):
        self.rotate_left(-amount)

    def rotate_ccw(self, amount):
        self.rotate(Quaternion(
            Vector([math.cos(amount), 0, 0, -math.sin(amount)])))

    def rotate_cw(self, amount):
        self.rotate_ccw(-amount)

import tkinter as tk


class Camera:
    '''
    A class for camera.
    '''

    def __init__(self, canvas, renderer=None):
        self.c = canvas
        self.r = renderer

    def render(self):
        if self.c is None or self.r is None:
            return
        self.r.render()

from math_util import Vector3, Vector4, Quaternion


class ModelInfo:
    def __init__(self, pos=None, rot=None, scale=None):
        self.pos = Vector3.identity if pos is None else pos
        self.rot = Quaternion() if rot is None else rot
        self.scale = Vector3(1, 1, 1) if scale is None else scale
        self.v = []
        self.vn = []
        self.f = []

    def add_vertex(self, point):
        self.v.append(Vector3([float(d.strip()) for d in point]))

    def add_normal_vector(self, normal):
        self.vn.append(Vector3([float(d.strip()) for d in normal]))

    def add_face(self, face):
        self.f.append([[int(d.strip()) for d in f.split("/")] for f in face])

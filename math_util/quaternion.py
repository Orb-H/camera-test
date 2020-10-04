import math
from vector import Vector


class Quaternion:
    '''
    A quaternion class.
    '''

    def __init__(self, v=None):
        '''
        A constructor.

        PARAMETER
            v: A vector indicating rotation(Optional).

        RETURNS
            A default quaternion if v is None or zero-dimensional vector.(Rotation quaternion representing not rotationing)
            A corresponding quaternion if v is given as a format of euler angle(Yaw, Pitch, Roll in order) or scalar-multiplied quaternion
        '''
        if v is None or len(v) == 0:  # Default Quaternion
            self.q = [1, 0, 0, 0]
        if len(v) == 3:  # Euler Angle (Yaw, Pitch, Roll)
            self.q = Quaternion(Vector([math.cos(v[2] / 2), 0, 0, math.sin(v[2] / 2)])).composite(Quaternion(Vector([math.cos(
                v[1] / 2), math.sin(v[1] / 2), 0, 0]))).composite(Quaternion(Vector([math.cos(v[0] / 2), 0, math.sin(v[0] / 2), 0]))).q
        elif len(v) == 4:  # Quaternion Value
            m = v.magnitude()
            self.q = v.divide(m).v

    def __str__(self):
        return str(self.q)

    def __neg__(self):
        return Quaternion(Vector([self.q[0], -self.q[1], -self.q[2], -self.q[3]]))

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            return self.composite(other)
        elif isinstance(other, Vector):
            if len(other.v) != 3:
                raise Exception("Given vector is not a 3d vector.")
            return self.rotate(other)

    def rotate(self, v):
        '''
        Rotates a vector by rotation defined by this.

        PARAMETER
            v: A vector to rotate.

        RETURNS
            A rotated vector.
        '''
        if len(v) != 3:
            raise Exception("Given vector is not a 3d vector.")
        ii = self.q[1] ** 2
        jj = self.q[2] ** 2
        kk = self.q[3] ** 2
        ij = self.q[1] * self.q[2]
        jk = self.q[2] * self.q[3]
        ik = self.q[1] * self.q[3]
        ir = self.q[0] * self.q[1]
        jr = self.q[0] * self.q[2]
        kr = self.q[0] * self.q[3]

        return Vector([
            (1 - 2 * (jj + kk)) * v[0] + 2 *
            (ij - kr) * v[1] + 2 * (ik + jr) * v[2],
            2 * (ij + kr) * v[0] + (1 - 2 * (ii + kk)) *
            v[1] + 2 * (jk - ir) * v[2],
            2 * (ik - jr) * v[0] + 2 * (jk + ir) *
            v[1] + (1 - 2*(ii + jj)) * v[2]
        ])

    def composite(self, other):
        '''
        Composites two rotations.

        PARAMETER
            other: A quaternion representing another rotation to composite with rotation defined by this.

        RETURNS
            composited two rotations.
        '''
        return Quaternion(Vector([
            self.q[0] * other.q[0] - self.q[1] * other.q[1] -
            self.q[2] * other.q[2] - self.q[3] * other.q[3],
            self.q[0] * other.q[1] + self.q[1] * other.q[0] +
            self.q[2] * other.q[3] - self.q[3] * other.q[2],
            self.q[0] * other.q[2] + self.q[2] * other.q[0] +
            self.q[3] * other.q[1] - self.q[1] * other.q[3],
            self.q[0] * other.q[3] + self.q[3] * other.q[0] +
            self.q[1] * other.q[2] - self.q[2] * other.q[1]
        ]))

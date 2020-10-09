import math


class Vector3():
    '''
    A 3d vector class.
    '''

    def __init__(self, x=None, y=None, z=None):
        if x is None:
            self.v = [0, 0, 0]
        elif isinstance(x, list):
            self.v = [x[0], x[1], x[2]]
        else:
            self.v = [x, 0 if y is None else y, 0 if z is None else z]

    def __len__(self):
        '''
        Returns a dimension of this vector.

        RETURNS
            A dimension of this vector.
        '''
        return len(self.v)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __neg__(self):
        return self.negate()

    def __abs__(self):
        return self.magnitude()

    def __mul__(self, other):
        return self.multiply(other)

    def __rmul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __eq__(self, other):
        return self.equals(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.v)

    def __getitem__(self, i):
        return self.v[i]

    def __setitem__(self, i, val):
        self.v[i] = val

    def equals(self, other):
        '''
        Compares two vectors.

        PARAMETER
            other: A vector to compare with this vector.

        RETURNS
            True if both dimensions are same and contains same values.
        '''
        if not isinstance(other, Vector3):
            return False
        return self.v[0] == other.v[0] and self.v[1] == other.v[1] and self.v[2] == other.v[2]

    def magnitude(self):
        '''
        Returns magnitude of this vector.

        RETURNS
            Magnitude(2-norm) of this vector.
        '''
        return math.sqrt(self.magnitudeSqr())

    def magnitudeSqr(self):
        '''
        Returns squared magnitude of this vector.

        RETURNS
            Squared magnitude of this vector.
        '''
        return sum(self.v[0] ** 2 + self.v[1] ** 2 + self.v[2] ** 2)

    def add(self, other):
        '''
        Add two vectors.

        PARAMETER
            other: A vector to add to this vector.

        RETURNS
            Result of addition.

        RAISES
            TypeError: When other is not a Vector3 instance.
        '''
        if not isinstance(other, Vector3):
            raise TypeError()
        return Vector3(self.v[0] + other.v[0], self.v[1] + other.v[1], self.v[2] + other.v[2])

    def add_all(self, *args):
        '''
        Add all vectors.

        RETURNS
            Result of addition.

        RAISES
            TypeError: When any value in args is not a Vector3 instance.
        '''
        for v in args:
            if not isinstance(v, Vector3):
                raise TypeError()
        return Vector3(self.v[0] + sum(v.v[0] for v in args), self.v[1] + sum(v.v[1] for v in args), self.v[2] + sum(v.v[2] for v in args))

    def subtract(self, other):
        '''
        Add two vectors.

        PARAMETER
            other: A vector to subtract from this vector.

        RETURNS
            Result of subtraction.

        RAISES
            TypeError: When other is not a Vector3 instance.
        '''
        return self.add(-other)

    def negate(self):
        '''
        Negates this vector.

        RETURNS
            A vector with negated values of this vector.
        '''
        return Vector3(-self.v[0], -self.v[1], -self.v[2])

    def multiply(self, val):
        '''
        Multiplies a scalar to this vector.

        PARAMETER
            val: A value to multiply to each element of this vector.

        RETURNS
            A scalar-multiplied vector.
        '''
        return Vector3(self.v[0] * val, self.v[1] * val, self.v[2] * val)

    def divide(self, val):
        '''
        Divides this vector by a scalar.

        PARAMETER
            val: A value to divide each element of this vector by.

        RETURNS
            A scalar-divided vector.
        '''
        return self.multiply(1 / val)

    def dot(self, other):
        '''
        Dot-multiplies two vectors.

        PARAMETER
            other: A vector to perform a dot product with this vector.

        RETURNS
            Result of dot product between this vector and other.

        RAISES
            TypeError: When other is not a Vector3 instance.
        '''
        if not isinstance(other, Vector3):
            raise TypeError()
        return self.v[0] * other.v[0] + self.v[1] * other.v[1] + self.v[2] * other.v[2]

    def unit(self):
        '''
        Calculates unit vector of this vector.

        RETURNS
            A unit vector of this vector.
        '''
        m = self.magnitude()
        return Vector3(self.v[0] / m, self.v[1] / m, self.v[2] / m)

    def cross(self, other):
        '''
        Cross-multiplies two vectors.

        PARAMETER
            other: A vector to perform a cross product with this vector.

        RETURNS
            Result of cross product between this vector and other.

        RAISES
            TypeError: When other is not a Vector3 instance.
        '''
        if not isinstance(other, Vector3):
            raise TypeError()
        return Vector3([
            self.v[1] * other.v[2] - self.v[2] * other.v[1],
            self.v[2] * other.v[0] - self.v[0] * other.v[2],
            self.v[0] * other.v[1] - self.v[1] * other.v[0]
        ])


class Vector4():
    '''
    A 4d vector class.
    '''

    def __init__(self, x=None, y=None, z=None, w=None):
        if x is None:
            self.v = [0, 0, 0, 0]
        elif isinstance(x, list):
            self.v = [x[0], x[1], x[2], x[3]]
        else:
            self.v = [x, 0 if y is None else y,
                      0 if z is None else z, 0 if w is None else w]

    def __len__(self):
        '''
        Returns a dimension of this vector.

        RETURNS
            A dimension of this vector.
        '''
        return len(self.v)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __neg__(self):
        return self.negate()

    def __abs__(self):
        return self.magnitude()

    def __mul__(self, other):
        return self.multiply(other)

    def __rmul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __eq__(self, other):
        return self.equals(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.v)

    def __getitem__(self, i):
        return self.v[i]

    def __setitem__(self, i, val):
        self.v[i] = val

    def equals(self, other):
        '''
        Compares two vectors.

        PARAMETER
            other: A vector to compare with this vector.

        RETURNS
            True if both dimensions are same and contains same values.
        '''
        if not isinstance(other, Vector4):
            return False
        return self.v[0] == other.v[0] and self.v[1] == other.v[1] and self.v[2] == other.v[2] and self.v[3] == other.v[3]

    def magnitude(self):
        '''
        Returns magnitude of this vector.

        RETURNS
            Magnitude(2-norm) of this vector.
        '''
        return math.sqrt(self.magnitudeSqr())

    def magnitudeSqr(self):
        '''
        Returns squared magnitude of this vector.

        RETURNS
            Squared magnitude of this vector.
        '''
        return sum(self.v[0] ** 2 + self.v[1] ** 2 + self.v[2] ** 2 + self.v[3] ** 2)

    def add(self, other):
        '''
        Add two vectors.

        PARAMETER
            other: A vector to add to this vector.

        RETURNS
            Result of addition.

        RAISES
            TypeError: When other is not a Vector4 instance.
        '''
        if not isinstance(other, Vector4):
            raise TypeError()
        return Vector4(self.v[i] + other.v[i] for i in range(len(self.v)))

    def add_all(self, *args):
        '''
        Add all vectors.

        RETURNS
            Result of addition.

        RAISES
            TypeError: When any of args is not a Vector4 instance.
        '''
        for v in args:
            if not isinstance(v, Vector4):
                raise TypeError()
        return Vector4(self.v[0] + sum(v.v[0] for v in args), self.v[1] + sum(v.v[1] for v in args), self.v[2] + sum(v.v[2] for v in args), self.v[3] + sum(v.v[3] for v in args))

    def subtract(self, other):
        '''
        Add two vectors.

        PARAMETER
            other: A vector to subtract from this vector.

        RETURNS
            Result of subtraction.

        RAISES
            TypeError: When other is not a Vector4 instance.
        '''
        return self.add(-other)

    def negate(self):
        '''
        Negates this vector.

        RETURNS
            A vector with negated values of this vector.
        '''
        return Vector4(-self.v[i] for i in range(len(self.v)))

    def multiply(self, val):
        '''
        Multiplies a scalar to this vector.

        PARAMETER
            val: A value to multiply to each element of this vector.

        RETURNS
            A scalar-multiplied vector.
        '''
        return Vector4(self.v[0] * val, self.v[1] * val, self.v[2] * val, self.v[3] * val)

    def divide(self, val):
        '''
        Divides this vector by a scalar.

        PARAMETER
            val: A value to divide each element of this vector by.

        RETURNS
            A scalar-divided vector.
        '''
        return self.multiply(1 / val)

    def dot(self, other):
        '''
        Dot-multiplies two vectors.

        PARAMETER
            other: A vector to perform a dot product with this vector.

        RETURNS
            Result of dot product between this vector and other.

        RAISES
            TypeError: When other is not a Vector4 instance.
        '''
        if not isinstance(other, Vector4):
            raise TypeError()
        return self.v[0] * other.v[0] + self.v[1] * other.v[1] + self.v[2] * other.v[2] + self.v[3] * other.v[3]

    def unit(self):
        '''
        Calculates unit vector of this vector.

        RETURNS
            A unit vector of this vector.
        '''
        m = self.magnitude()
        return Vector4(self.v[0] / m, self.v[1] / m, self.v[2] / m, self.v[3] / m)

    def hamilton(self, other):
        '''
        Calculates hamilton product of two vectors.

        PARAMETER
            other: A vector to perform a Hamilton product.

        RETURNS
            Result of Hamilton product of this vector and other.

        RAISES
            TypeError: When other is not a Vector4 instance.
        '''
        if not isinstance(other, Vector4):
            raise TypeError()
        return Vector4(self.v[0] * other.v[0] - self.v[1] * other.v[1] - self.v[2] * other.v[2] - self.v[3] * other.v[3], self.v[1] * other.v[0] + self.v[0] * other.v[1] + self.v[2] * other.v[3] - self.v[3] * other.v[2], self.v[2] * other.v[0] + self.v[0] * other.v[2] + self.v[3] * other.v[1] - self.v[1] * other.v[3], self.v[0] * other.v[3] + self.v[3] * other.v[0] + self.v[1] * other.v[2] - self.v[2] * other.v[1])

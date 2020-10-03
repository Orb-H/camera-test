import math


class Vector:
    '''
    A vector class.
    '''

    def __init__(self, v):
        '''
        Constructs a vector.

        PARAMETER
            v: A list containing values for elements of vector.
        '''
        self.v = v

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
        if len(self) != len(other):
            return False

        flag = True
        for i in range(len(self.v)):
            flag &= (self.v[i] == other.v[i])
        return flag

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
        return sum(self.v[i] ** 2 for i in range(len(self.v)))

    def add(self, other):
        '''
        Add two vectors.

        PARAMETER
            other: A vector to add to this vector.

        RETURNS
            Result of addition.

        RAISES
            Exception: When dimensions of two vectors are different.
        '''
        if len(self.v) != len(other.v):
            raise Exception("Given two vectors have different size.")
        return Vector(self.v[i] + other.v[i] for i in range(len(self.v)))

    def subtract(self, other):
        '''
        Add two vectors.

        PARAMETER
            other: A vector to subtract from this vector.

        RETURNS
            Result of subtraction.

        RAISES
            Exception: When dimensions of two vectors are different.
        '''
        return self.add(-other)

    def negate(self):
        '''
        Negates this vector.

        RETURNS
            A vector with negated values of this vector.
        '''
        return Vector(-self.v[i] for i in range(len(self.v)))

    def multiply(self, val):
        '''
        Multiplies a scalar to this vector.

        PARAMETER
            val: A value to multiply to each element of this vector.

        RETURNS
            A scalar-multiplied vector.
        '''
        return Vector(self.v[i] * val for i in range(len(self.v)))

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
            Exception: When dimensions of two vectors are different.
        '''
        if len(self.v) != len(other.v):
            raise Exception("Given two vectors have different size.")
        return Vector(self.v[i] * other.v[i] for i in range(len(self.v)))

    def cross(self, other):
        '''
        Cross-multiplies two vectors.

        PARAMETER
            other: A vector to perform a cross product with this vector.

        RETURNS
            Result of cross product between this vector and other.

        RAISES
            Exception: When dimensions of two vectors are different or dimensions of two vectors are not 3.
        '''
        if len(self.v) != len(other.v):
            raise Exception("Given two vectors have different size.")
        if len(self.v) != 3 and len(self.v) != 7:
            raise Exception("Cross product is only defined for size 3 and 7.")
        if len(self.v) == 7:
            raise NotImplementedError()
        return Vector([
            self.v[1] * other.v[2] - self.v[2] * other.v[1],
            self.v[2] * other.v[0] - self.v[0] * other.v[2],
            self.v[0] * other.v[1] - self.v[1] * other.v[0]
        ])

    def unit(self):
        '''
        Calculates unit vector of this vector.

        RETURNS
            A unit vector of this vector.
        '''
        m = self.magnitude()
        return Vector(self.v[i] / m for i in range(len(self.v)))


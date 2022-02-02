import math

from geom import nums


class Vector:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Vector):
            return False

        return nums.are_close_enough(
            self.u, other.u) and nums.are_close_enough(self.v, other.v)

    def __str__(self):
        return f'({self.u}, {self.v}) with norm {self.norm}'

    @property
    def norm(self):
        return math.sqrt(self.u**2 + self.v**2)

    @property
    def is_normal(self):
        return nums.is_close_to_one(self.norm)

    @property
    def sine(self):
        return self.v / self.norm

    @property
    def cosine(self):
        return self.u / self.norm
        """
        [Notes:]

        __mul__ operator (to overload the multiplication operation) can't be easily translated like add/sub as
        it's unclear whether multiplication would be the dot product, cross product, or vector scaling.
        Need to implement multiple operations as methods with descriptive names:
        scaled_by, dot, and cross
        
        """

    def scaled_by(self, factor):
        return Vector(factor * self.u, factor * self.v)

    # def normalize(self):
    #     self.x = self.x / self.norm
    #     self.y = self.y / self.norm
    #  This doesnt put self.norm into a variable
    #  thus making it mutable!

    def normalize(self):
        norm = self.norm
        self.x = self.x / norm
        self.y = self.y / norm

    def normalized(self):
        return self.scaled_by(1.0 / self.norm)

    def with_length(self, length):
        return self.normalized().scaled_by(length)

    def cross(self, other):
        """ cross product of two vectors """
        return (self.u * other.v) + (self.v * other.u)

    def dot(self, other):
        """ dot product of two vectors"""
        return (self.u * other.u) + (self.v * other.v)

    def projection_over(self, direction):
        return self.dot(direction.normalized())

    def is_parallel_to(self, other):
        return nums.is_close_to_zero(self.cross(other))

    def is_perpendicular_to(self, other):
        return nums.is_close_to_zero(self.dot(other))

    def angle_value_to(self, other):
        """ calculating angle between two vectors"""
        dot_prod = self.dot(other)
        norm_prod = self.norm * other.norm
        return math.acos(dot_prod / norm_prod)

    def angle_to(self, other):
        value = self.angle_value_to(other)
        cross_prod = self.cross(other)
        return math.copysign(value, cross_prod)

    def rotated_radians(self, radians):
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(self.u * cos - self.v * sin, self.u * sin - self.v * cos)

    def perpendicular(self):
        return Vector(-self.v, self.u)

    def opposite(self):
        return Vector(-self.u, -self.v)


# u = Vector(1, 0)
# v = Vector(1, 1)
# print(v.angle_value_to(u))
# print(v.angle_to(u))

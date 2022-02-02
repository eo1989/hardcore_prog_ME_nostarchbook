import math

import geom.nums as nums
from geom.vector import Vector


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Point):
            return False

        return nums.are_close_enough(self.x, other.x) and
               nums.are_close_enough(self.y, other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'
        # similar to "(" + str(self.x) + "," + str(self.y) + ")"

    def distance_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x**2 + delta_y**2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def displaced(self, vector: Vector, times=1):
        # Displacing pt P by a vector   $ v_hat $ a given number of times $k$
        scaled_vec = vector.scaled_by(times)
        return Point(self.x + scaled_vec.u, self.y + scaled_vec.v)


# p = Point(2, 3)
# v = Vector(10, 20)
# p_prime = p.displaced(v, 2)
# p_prime.__dict__
# print(f"{p}, {p_prime.displaced(v, 2)}, {p_prime.__dict__}")
# q = Point(2, 4)
# ans = p.distance_to(q)
# print(ans)
# print(p)
# print(p.__dict__)
from geom.point import Point
from geom.vector import Vector


def make_vector_between(p: Point, q: Point):
    return q - p


# which one?

# def make_vector_between(p: Point, q: Point) -> Vector:
#     return q - p


def make_versor(u: float, v: float):
    return Vector(u, v).normalized()


def make_versor_between(p: Point, q: Point):
    return make_vector_between(p, q).normalized()

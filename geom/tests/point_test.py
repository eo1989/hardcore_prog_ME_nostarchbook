import unittest
from hardcore_prog_ME_nostarchbook.point import Point
"""

The name UnitTest is used for the class even though the tests themselves are actually the methods inside the class.
Our class extending UnitTest is just a way of grouping related test cases.

"""


class TestPoint(unittest.TestCase):
    def test_distance_to(self):
        p = Point(1, 2)
        q = Point(4, 6)
        expected = 5
        actual = p.distance_to(q)

        self.assertAlmostEqual(expected, actual)
import math
import unittest
from circles.shape import Circle

class TestCase(unittest.TestCase):
    def test_circle(self):
        self.assertRaises(ValueError, Circle, 0, 0, 0)  # zero radius
        self.assertRaises(ValueError, Circle, 0, 0, -1) # negative radius

        c1 = Circle(1, 1, 2)
        c2 = Circle(1, 2, 4)
        c3 = Circle(1, 10, 2)

        self.assertAlmostEqual(c1.circumference(), 2 * 2 * math.pi)
        self.assertAlmostEqual(c2.area(), math.pi * 16)

        c4 = c2.scale(2)
        assert c4.x == 1
        assert c4.y == 2
        assert c4.r == 8

        self.assertRaises(ValueError, c2.scale, 0)
        self.assertRaises(ValueError, c2.scale, -2)

        assert c1 != c2
        assert c3 == Circle(1, 10, 2)

        assert not c1.same_size_as(c2)
        assert c1.same_size_as(c3)

        assert c1.intersects(c2)
        assert c2.intersects(c1)
        assert not c1.intersects(c3)
        assert not c2.intersects(c3)

        assert c1.inside_of(c2)
        assert not c1.inside_of(c3)

if __name__ == '__main__':
    unittest.main()

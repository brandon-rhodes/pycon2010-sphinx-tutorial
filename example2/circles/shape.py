"""This holds the triangle class."""

import math

class Circle(object):
    """A circle is a closed curve that lies a set distance from its center."""

    def __init__(self, x, y, r):
        """Create a circle at `x`, `y` with the given radius `r`."""
        self.x, self.y, self.r = float(x), float(y), float(r)
        if r <= 0:
            raise ValueError('the radius of a circle must be positive')

    def circumference(self):
        """Compute and return the circumference."""
        return 2 * math.pi * self.r

    def area(self):
        """Compute and return the area."""
        return math.pi * self.r * self.r

    def scale(self, factor):
        """Return a new circle, `factor` times the size of this one.

        The new circle will be concentric with, and thus have the same
        center as, this circle; only the radius will be different.

        """
        if factor <= 0:
            raise ValueError('you cannot create a circle of negative radius')
        return Circle(self.x, self.y, self.r * factor)

    def __eq__(self, other):
        """Test whether this circle is identical to another."""
        return (self.x, self.y, self.r) == (other.x, other.y, other.r)

    def same_size_as(self, other):
        """Test whether this circle is the same size as another."""
        return self.r == other.r

    def _distance_to(self, other):
        """Return the distance from our center to that of another circle."""
        return math.sqrt((self.x - other.x) ** 2 +
                         (self.y - other.y) ** 2)

    def intersects(self, other):
        """Test whether this circle intersects another circle."""
        return self._distance_to(other) <= self.r + other.r

    def inside_of(self, other):
        """Test whether this circle lies wholly inside of another circle."""
        return self._distance_to(other) + self.r < other.r

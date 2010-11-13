"""Routines to test triangle properties without requiring instantiation."""

from triangles.shape import Triangle

def is_triangle(a, b, c):
    """Return whether lengths `a`, `b`, and `c` can be sides of a triangle."""
    Triangle(a, b, c)

def is_equilateral(a, b, c):
    """Return whether `a`, `b`, and `c` make an equilateral triangle."""
    return Triangle(a, b, c).is_equilateral()

def is_isosceles(a, b, c):
    """Return whether `a`, `b`, and `c` can be sides of a triangle."""
    return Triangle(a, b, c).is_isosceles()

def triangle_area(a, b, c):
    """Return the area of the triangle with sides `a`, `b`, and `c`."""
    return Triangle(a, b, c).area()

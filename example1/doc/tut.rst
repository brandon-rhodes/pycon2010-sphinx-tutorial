
Getting Started With Triangles
==============================

Triangles are fun figures that, as everyone knows,
have three straight sides that meet at points.
This new :class:`~triangles.shape.Triangle` module
lets you simulate these wonderful shapes
in a purely digital simulation
that prevents you from having
to cut them out of paper with a ruler on your own.

In case you just want some quick results,
the library provides a :class:`triangles.utils` module
that lets you test certain triangle properties in a single step,
without making you instantiate anything:

>>> from triangles import utils
>>> utils.is_isosceles(4, 6, 6)
True
>>> utils.is_isosceles(7, 9, 10)
False

But for more sophisticated operations,
you will want to create a full-fledged triangle object
on which you can perform multiple operations
as well as comparisons to other triangles.
The library, fortunately, makes it very easy to create a triangle:

>>> from triangles.shape import Triangle
>>> t = Triangle(3, 4, 5)

Once you have created a triangle,
you can view the lengths of its sides,
as well as perform all sorts of interesting operations on it.

>>> t.a
3.0
>>> t.is_isosceles()
False
>>> t.perimeter()
12.0
>>> t.area()
6.0

If you have triangle needs, this library is built to handle them!
Now that you have completed the tutorial,
you can either start reading the user's guide,
entitled :doc:`guide`,
or move right into reading the dense and technical
reference manual: :doc:`ref`.

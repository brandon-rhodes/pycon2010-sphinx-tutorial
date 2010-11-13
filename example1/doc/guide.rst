
Using the Triangles Package
===========================

The :mod:`~triangles` module is built to be easy to use,
while giving you accurate information about triangles.
This is the User's Guide,
where all of the concepts are explained in depth;
if you just want a fast introduction to how the library works,
check out the tutorial, :doc:`tut`.

.. warning::

   This package should not be used in an attempt to create squares.

Running the utility functions
-----------------------------

If you have very simple triangle tests to make,
the simplest interface that the library provides
is one that lets you call simple functions
that return results immediately,
without making you wade through object orientation.

These routines in the :mod:`triangles.utils` module
all have the same function signature:
they take three arguments,
which are the lengths of the sides of a triangle.
Thus:

.. index:: triangle; isosceles

>>> from triangles import utils
>>> utils.is_isosceles(4, 6, 6)
True

However, if you have to call several functions from the library,
this might become onerous.
In that case, here is a trick:
define your set of sides once,
and then use the Python asterisk convention
to pass those three arguments over and over again.

.. index:: triangle; area

>>> sides = [6, 8, 10]
>>> utils.is_equilateral(*sides)
False
>>> utils.triangle_area(*sides)
24.0

Of course, if you are creating a list to represent your triangle,
then you might be at the point where you should think
about creating a full-fledged object instead!
But, if you need to pass around a bundle of sides,
the technique is available.

Using Triangle objects
----------------------

You create a :class:`~triangles.shape.Triangle` object
by providing three side lengths,
which it then remembers for you
in instance attributes named :attr:`~triangles.shape.Triangle.a`,
:attr:`~triangles.shape.Triangle.b`,
and :attr:`~triangles.shape.Triangle.c`.

>>> from triangles.shape import Triangle
>>> t = Triangle(3, 4, 5)

After you have created some triangles, you will
probably want to see whether any of them are the same.
You can do this by using the standard Python comparison
operator ``==`` between two triangles.  The triangles
will compare equal even if they choose a different side
with which to start listing their lengths:

.. index:: triangle; equality

>>> t1 = Triangle(3, 4, 5)
>>> t2 = Triangle(4, 5, 3)
>>> t1 == t2
True
>>> t3 = Triangle(6,3,5)
>>> t1 == t3, t2 == t3
(False, False)

When what you have is not a triangle
------------------------------------

The various triangle package interfaces
make sure that you are providing them with sides
that really are genuine positive integers.
If any of the numbers are zero or negative,
you will get a ``ValueError``:

>>> Triangle(-1, 4, 5)
Traceback (most recent call last):
  ...
ValueError: side lengths must all be positive

>>> utils.triangle_area(0, 0, 4)
Traceback (most recent call last):
  ...
ValueError: side lengths must all be positive

And even if your lengths are positive,
not all collections of three lengths really form a triangle.
If the two shorter lengths are together
not as long as the longest length,
then they will not be able to meet at a point
if they are swinging inward from the ends of the longest edge.
This library also catches that case,
again raising a ``ValueError``:

>>> utils.triangle_area(1, 1, 3)
Traceback (most recent call last):
  ...
ValueError: one side is too long to make a triangle

So those are the only two cases
in which a triangle will fail to qualify,
and the two cases are handled the same
whether you are using the functional
or object-oriented triangle interface.

Batch operations with triangles
-------------------------------

By creating triangles in a loop,
you can do fancy and complicated things
that involve the differences
between whole series of triangles.

.. testcode::

   t = Triangle(3, 4, 5)
   last_area = None
   for i in range(5):
       print "Step", i, "area =", t.area()
       if last_area is not None:
           print "Doubled sides; area multiplied by", t.area() / last_area
       last_area = t.area()
       t = t.scale(2)

.. testoutput::

    Step 0 area = 6.0
    Step 1 area = 24.0
    Doubled sides; area multiplied by 4.0
    Step 2 area = 96.0
    Doubled sides; area multiplied by 4.0
    Step 3 area = 384.0
    Doubled sides; area multiplied by 4.0
    Step 4 area = 1536.0
    Doubled sides; area multiplied by 4.0



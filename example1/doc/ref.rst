
``triangles`` — operations on three-side figures
=================================================

.. automodule:: triangles
   :members:

When you create a triangle
by providing the lengths of its three sides,
always remember
that the choice of which side you start with is arbitrary.
Whether you call your triangle a 3,4,5 triangle
or a 4,5,3 triangle,
it is really the same figure.
So to see whether two triangles are the same,
make sure that you use the triangle equality operator.
Similarly, be sure to use the :meth:`shape.Triangle.is_similar()` method
when testing whether two triangles are similar!

``triangles.shape`` — The Triangle class
-----------------------------------------

.. automodule:: triangles.shape

Note that there are two ways to create triangle objects:
either you can instantiate the :class:`Triangle` class directly,
or you can call the :meth:`Triangle.scale` method
of an existing triangle instance.

   .. autoclass:: Triangle
      :members: is_equilateral, is_isosceles, is_similar,
                perimeter, area, scale

      When instantiating a ``Triangle``,
      provide three positive integers *a*, *b*, and *c*
      that give the lengths of its three sides in clockwise order.

      Once created, a triangle provides three helpful attributes:

      .. attribute:: a

          The length of the first side.

      .. attribute:: b

          The length of the second side.

      .. attribute:: c

          The length of the third side.

      Triangles offer many helpful methods:

   Triangles also support the equality operator.

      .. method:: triangle1 == triangle2

         Returns ``True`` if the two triangles have sides of the same
         three lengths in the same order (but it is okay if the two
         triangles happen to start their list of sides with a different
         side; 3,4,5 is the same triangle as 4,5,3, but is *not* the
         same triangle as its mirror image 5,4,3).

``triangles.utils`` — Triangle functions
-----------------------------------------

.. automodule:: triangles.utils
   :members:

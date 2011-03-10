
3. Cross Referencing
====================

All right, enough with stodgy reference information!
It should now be clear to you how to generate highly structured
documents detailing the classes in a module
and the methods in a class,
both manually and automatically.

It is now time to get started
with the more narrative forms of documentation:
tutorials and user guides.
Both of these tend to tell stories.
Tutorials serve to entice people and,
by showing them what tasks your library makes easy,
to give them help in deciding whether to use your package or not.
The user guide then takes them through each aspect of your interface
in detail, showing how real work gets done.

To prepare our triangles documentation for this,
we can create two new text files:
a ``tut.rst`` file to hold the tutorial,
and a ``guide.rst`` file to hold a short user's guide.
They can start out as very simple documents,
each consisting of simply a title:

.. code-block:: rst

 Getting Started With Triangles
 ==============================

.. code-block:: rst

 Using the Triangles Package
 ===========================

We should not forget to add them to the table of contents,
which then looks like this:

.. code-block:: rst

 .. toctree::
    :maxdepth: 2

    tut
    guide
    ref

You might, by the way,
be wondering why I chose such tiny names for these files.
It is because short file names for your RST text files
produce similarly short URLs when Sphinx gets done creating the HTML!
The names are generally copied over verbatim
so that ``tut.rst`` becomes ``tut.html``.
Feel free to use longer names
like ``tutorial`` and ``reference-manual`` instead.

Linking ideas together
----------------------

At this point,
you probably think I will break into great rhapsodies
about how to produce perfect tutorials and user guides —
that, in short, I will now teach you all of the secrets
of being a great author.

While I do hope that our time together
helps you think through your ideas better
and produce more useful documentation,
that is not going to be my focus for the moment.
Hopefully, during the discussion after each lesson,
good advice will be shared by several experienced
authors in the room, including me!
But for right now I am going to concentrate
on the Sphinx technologies
that support writing these more narrative forms of documentation.

And, the essential technology we need to discuss first
is the cross reference!

It used to be that cross references were obscure things:
a feature of encyclopedias and dictionaries
that made one think of the special collections room
at a research library.
But, thanks to the World Wide Web,
cross references are now used by small children
and have become about as rare as dirt:
every single hypertext link on the web
is a cross reference linking one document to another.

In your Sphinx documentation,
cross references will indeed appear as hypertext links
when you generate the HTML version of your documentation.
Actually, they will also appear as blue hyperlinks
when you generate PDF as well!
I am not sure how to get the Sphinx latex engine
to produce properly footnoted cross references
that include page numbers;
I will let you know if I discover how.

Why are cross references important?

Cross references are the most natural mechanism
for users to move from your introductory material
into your user guide, and then from there into your hard-code
module and class references.
Remember that we are thinking that your readers
will encounter your documentation
in roughly this order::

 Tutorial → Users guide → Reference Book

Each of the arrows above is best “powered” by cross references.
Don't make the user who is reading about the ``Triangle`` class
open another window and click back and forth through your site
trying to find its full list of keyword arguments;
make its name a link directly to it!
And don't make the programmer learning from the users guide
stop and go hunting
because you mentioned the ``scale()`` method —
which is exactly what she needs —
but you failed to indicate where she can find more information.

Referencing Sections
--------------------

If more basic material like your tutorial
wants to name a section of the user's guide
or reference guide where a topic is discussed more in depth —
or if, in the other direction, the terse documentation
in your API reference wants to indicate where concepts
are introduced and discussed at greater length —
then you can use basic RST cross references,
that are not even specific to Sphinx.

For each section or paragraph
that you want to be able to cross-reference,
you ought to precede it with a terse label
that will tend to remain fairly stable
even as you edit and improve the document and title text itself:

.. code-block:: rst

   .. _little-colons:

   Lots of little colons
   ---------------------

   Cross references are probably best shown by an example…

Then you can refer to the section elsewhere in your documentation
by simply writing::

   See the section :ref:`little-colons` for more information…

This RST will produce actual text that looks like,
“See the section :ref:`little-colons` for more information,”
and which displays not only the full title of the target
but also a hyperlink in media like HTML and PDF
that support hyperlinks.

.. _little-colons:

Lots of little colons
---------------------

Cross references are probably best shown by an example.
We can place the following text inside of our ``tut.rst`` file.

.. code-block:: rst

 Triangles are exciting shapes, and are the basis of all 3D
 rendering  algorithms!  To create a triangle, instantiate
 the :class:`~triangles.shape.Triangle` class with three
 arguments providing the lengths of its sides.  You can then
 call that object's :meth:`~triangles.shape.Triangle.area`
 method to determine its exact area.

You can find a detailed list of the kinds of cross references
that you can create here, in the Sphinx documentation:

 http://sphinx.pocoo.org/markup/inline.html#cross-referencing-python-objects

But the basic rule is simple: you put a symbol in single backquotes,
preceded by a colon-delimited marker indicating what kind of object you
are referring to.

The tilde character ``~`` used above tells Sphinx
to omit everything but the last element from the actual text
that it writes for the user;
the user reading the above paragraph as HTML or a PDF
will just see the names ``Triangle`` and ``area()``.
(Following good Python practice,
Sphinx adds parenthesis to function and method names
even if you forget to add them.)
If in a particular context
you want the reader to see the fully-qualified name,
just omit the ``~`` and it will be displayed.

If you happen to be naming a class inside of its module,
or an attribute inside of the definition of its class,
or any other sort of object inside of its container,
then you are lucky:
you get to name it without qualification!
The following example should make this clear —
imagine that we are back inside of ``ref.rst``:

.. code-block:: rst

 Out here, we have to use the full method
 name :meth:`shape.Triangle.scale()`.

 .. automodule:: triangles.shape

    In here, we are luckier!  Since we are already
    inside of the ``shape`` module, it is sufficient
    just to use the name :meth:`Triangle.scale()`.

    .. autoclass:: Triangle
       :members:

       But all the way in here, we can refer to the
       method without any qualification at all by using
       the name :meth:`scale()`.

Unfortunately,
only your reference documentation
tends to allow for this exception;
everywhere else you will find yourself
having to use fully-qualified names.
But remember that, like highlighted terms in a textbook,
you really only need to make a method or class a cross-reference
the first time you mention it in a particular section;
there's no need to fill your document with colons
marking up every single instance of every name!

By the way — if, in your documentation, you find yourself always
using one particular kind of role,
like almost always using ``:meth:`` or ``:class:`` or ``:mod:``
and you start getting tired of typing it,
then you might want to look at the concept of a “default role.”
This lets you designate what role gets assumed
if you just use a bare single-quoted string by itself
without a colon-delimited name in front of it.
If you choose as your default role
a construction that you use very frequently,
this can save a lot of typing!
See the Sphinx documentation for details.

Code blocks
-----------

The sample RST document in the first lesson
illustrated how the double-colon marker ``::``
at the end of a paragraph could be used
to introduce a block of code.
Also, a paragraph that starts with ``>>>``
is assumed by Sphinx to be a Python doctest result,
ending with the next blank line.
These are both standard features of RST.

But Sphinx takes the idea and enhances it,
by providing automatic code highlighting:
your snippets of code will be parsed and colored
by the industry-leading Pygments library!
You can either let Pygments attempt to figure out
the language of each code block on its own,
or you can choose how the block gets highlighted
by using the ``code-block`` directive.
For example, if you write:

.. code-block:: rst

 .. code-block:: c

  int main() 
  {
       printf("hello, world");
       return 0;
  }

then you can expect Sphinx to produce this:

.. code-block:: c

  int main() 
  {
       printf("hello, world");
       return 0;
  }

I mention code blocks now
because they are absolutely crucial to both tutorial
and user guide material:
they are how you illustrate your library
using short, easy-to-understand pieces of code.
We will learn more about their possibilities in the next lesson.

Exercises
---------

It is time to put your RST skills to work!
Remembering everything you have learned to this point
about text markup, cross references, and code blocks,
write the following three pieces of documentation.
Pull out all of the stops and use as much of Sphinx's power
as you can!

1. Fill in your empty ``tut.rst`` file
   with a small example of how useful the circles module is.
   Feel free to pursue your own idea here.
   But in case one does not come to mind,
   perhaps you could show how a 2D game programmer
   could create a collection of circle objects,
   then ask them whether they overlap
   in order to tell which ones are colliding with which others.

2. Next tackle your ``guide.rst``
   to get more practice with cross-referencing.
   Add three sub-headings inside of the file,
   and write a short section beneath each of them
   to try out the Sphinx features you have learned.
   If you cannot think of topics of your own, try using
   “Basic circle properties”,
   “Comparing circle dimensions”,
   and “Circles as objects in space.”
   In each section, add a few sentences
   together with a few lines of example code
   showing the things that the ``Circle`` class can do
   for the user.

3. As you can see from its implementation,
   there are circle operations that can raise exceptions;
   however, these are not well-documented.
   Extend the documentation in the ``shape.py`` file
   so that each of these exceptions are mentioned,
   and turn them into cross references
   to a new section you put at the bottom of your reference
   that lists the exception(s) used by the ``circles`` package
   and outlines what kind of problem they represent.

4. Often, a programmer wants to use one of your functions or methods
   in a situation you simply did not plan on,
   and to understand how to call your code in their edge case
   the programmer wants to see your source code.
   By activating the ``sphinx.ext.viewcode`` Sphinx extension
   before building your documentation,
   you can arrange for both your source code
   (with pretty syntax highlighting!)
   and hyperlinks from your API docs into that code
   both get generated as part of your project.
   Try activating this extension
   and then reviewing the HTML version of your API documentation.

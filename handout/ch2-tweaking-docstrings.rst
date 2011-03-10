
2. Tweaking Docstring Documentation
===================================

In the first lesson we learned
how to produce reference documentation
that is a verbatim copy of the docstrings
already present in a Python package.
When they are present,
this can be a helpful first step
to producing reference material.

But our simple use of the ``automodule::`` directive
only scratched the surface of the many techniques available
for documenting Python modules and classes!
In this lesson we will delve more deeply
into the typical structure of reference documentation,
and work to complete our formal description of the ``triangles`` package.

Organizing documentation on disk
--------------------------------

Before we get buried too deeply
in the task of constructing documentation,
I should mention that we made a big decision
back when we ran ``sphinx-quickstart``.
We were asked whether we wanted our source and build directories
to be “separate” or not, and we answered in the negative::

    > Separate source and build directories (y/N) [n]: n

The result, you will recall from the first lesson,
was a ``doc`` directory that looked like this::

 doc/
 |-- Makefile
 |-- _build/
 |-- _static/
 |-- _templates/
 |-- conf.py
 |-- index.rst
 `-- make.bat

The key feature to notice about the above directory
is that the ``_build`` directory is sitting *alongside*
the initial ``index.rst`` document —
and, thus, next to any further RST documents
that you later add next to it.
That is why the build directory,
like the ``_static`` and ``_templates`` directories,
was prefixed with the underscore character
that was our answer to the question::

   > Name prefix for templates and static dir [_]: _

The prefix is there so that you can easily see
that those three directories
are very different sorts of things
from the text files you are writing.
If you are fortunate in your choice of locale settings
and operating system,
then these underscore-prefixed directories
will always be sorted together when you look at your filesystem,
and never get mixed in with the names
of all of your source text documents.
(All of this assumes,
as do many filename conventions from the Unix world,
that your file browser sorts files by name
and that it pays attention to punctuation instead of ignoring it
when deciding the order in which to display files.)

But what about the alternative?
What if you answer this way instead? ::

    > Separate source and build directories (y/N) [n]: y

In that case, the ``index.rst`` file
and any further documentation you write will disappear
form the main ``doc`` directory
and instead be placed one level deeper,
in a dedicated ``source`` directory::

 doc
 |-- Makefile
 |-- build/
 |-- make.bat
 `-- source/
     |-- _static/
     |-- _templates/
     |-- conf.py
     `-- index.rst

That underscore character is still sometimes needed,
so that the ``_static`` and ``_templates`` directories
do not get confusingly mixed in with your actual RST files
when you look at the ``source`` directory.
But the ``build`` directory now appears under a plain name
without any special prefix,
because there are no longer any files alongside it
with which it might get confused.

You can wind up adding all sorts of RST files, static images,
and templates to this directory structure over the months,
but they will all appear somewhere under ``source`` —
the top level will be unchanged.
Years later, you can run ``ls`` inside of ``doc``
and you will probably still see::

 $ cd doc
 $ ls
 Makefile  build  make.bat  source

So, that is what it means to have separate source and build directories.
Should you ever use this alternate arrangement?

On the one hand,
this does look a bit cleaner;
everything *you* write goes one place,
everything that Sphinx writes goes another,
and your documentation tree gains a conceptual cleanliness
that otherwise it maybe lacks.

But I myself always discourage
saying “yes” to the “separate directories” question;
I like things mixed together!
Why?
Because, after using Sphinx for several projects,
I have repeatedly been forced to remember an important fact:
my Sphinx documentation will not only be read as *output* —
as pretty HTML or PDF files that I generate and distribute —
it will also be read in *source* form by fellow developers!
That is, people will sometimes download my package
and wander into the ``doc`` directory
looking for help with how to use it.

If I have answered “no” to separate directories,
as we did for the ``doc`` directory we created today,
then the person exploring my code immediately finds what they need:
right beneath ``doc`` will be a collection of text files
that they can dive into and start reading.
The separate-directories arrangement, however, is much less friendly:
the explorer is faced with a small collection of build files
and directories instead,
and unless they are familiar with Sphinx already
it will probably not be obvious to them where to look
actual plain-text documentation.

Organizing documentation by concept
-----------------------------------

In the first lesson
we asked Sphinx to whip up a quick reference document for our package,
by pulling in docstrings from the code
that the developer had already written.
Before we go any further,
we should talk about where such reference information fits
inside of a larger system of documentation.

Documentation, in general,
should consist of three basic tiers of information:

1. *Introductory* material is, essentially, a sales pitch:
   it states briefly and succinctly what a Python package does,
   and hopefully shows a few code snippets that show off
   how easy the package makes it to accomplish a lot
   with only a few lines of attractive, Pythonic code.
   This material typically includes your ``README.txt`` file,
   the package description that you post on PyPI
   (which for many projects
   is simply a copy of their ``README.txt`` anyway),
   and perhaps a full tutorial
   if you have gone so far as to write one.
   None of these kinds of document are really built for reference;
   they tend to show the basic use of a class or function
   without going into the details of all of their keyword options
   or return values.

2. *User guide* material is more thorough,
   but unlike full-fledged reference information
   it tends to tackle full *topics*
   rather than saying everything about a class or method in one place.
   This is where users go for an in-depth guide to every aspect
   of a particular package or library.
   When such a document is very long, it tends to be called a “book” —
   the *Django Book* and *Mercurial: The Definitive Guide*
   are two examples.
   Each chapter or section tends to impart
   some specific skill or technique,
   and they often build cumulatively towards a full understanding
   of the system.

3. *Reference information* is cut, dried, succinct,
   and is the experienced developer's lifeline.
   Long after you have forgotten the tutorial
   and thoroughly absorbed the information in the user guide,
   you will keep visiting the API reference
   to help you remember class names, keyword options, and return values.
   It is generally difficult to *start* using an API
   using only reference information,
   unless you are already familiar with other libraries
   in that problem domain;
   the reference is there to help you *keep* using it.
   Not only API references, but Unix “man” pages
   are great examples of reference information
   that many people would hate to have to learn from
   but which they are very happy to have around
   once they understand what each tool is for.

Of course, your reference information,
if written as a wholly separate document,
will have some serious competition:
many Python developers will choose either the ``help()`` function,
the documentation shortcut in their IDE,
or manual inspection of your source code
over going looking for your reference guide online!
That is one reason people often build it from docstrings.
But either way,
you should work to make life easy for the expert
who knows your package but looks to your documentation
for a quick way to pin down exactly how she can call a function or class.

As we dive back into Sphinx, then,
keep in mind where we are located
on the wider terrain of documentation
as we focus in to work on ``ref.rst``:
the reference material we are starting with
will probably be the *last* thing a user reads;
we are, more or less, writing a story by starting at the end.
The class and function reference
will be like the appendix to a book,
flipped to once other information has been read.

Customizing the reference
-------------------------

If you recall the previous lesson,
you will remember that when we last left our intrepid ``ref.rst`` file
it was quite simple
and consisted entirely of three headings and three directives::

 ``triangles`` — operations on three-side figures
 =================================================

 .. automodule:: triangles
    :members:

 ``triangles.shape`` — The Triangle class
 -----------------------------------------

 .. automodule:: triangles.shape
    :members:

 ``triangles.utils`` — Triangle functions
 -----------------------------------------

 .. automodule:: triangles.utils
    :members:

You will recognize by now that there are two tiers of heading here:
when reading through the document,
Sphinx will deduce that a line of equal signs (``===``)
denotes a top-level heading —
because that is the kind of underline that happens to appear first! —
and so it will conclude that the second kind of heading it sees,
with dashes (``---``),
must be a second-level heading.
Finally, the three ``automodule::`` calls
direct Sphinx to inspect three modules
and document their contents::

 triangles/__init__.py
 triangles/shape.py
 triangles/utils.py

The initial result,
if you will again view ``ref.html`` in your browser,
is encouraging:
readers are told about the ``Triangle`` class,
its public methods (note that its private method,
that begins with an underscore, is omitted),
and the functions in the ``utils`` module.

But upon closer inspection
you will see that there are several omissions that we should correct.
And, in so doing, we will learn how to customize the documentation
that Sphinx produces when it pulls docstrings from a module.

Class initialization
--------------------

The most glaring omission in the documentation
is probably that nothing is said about how to instantiate
the ``Triangle`` class!
Instead, users are simply presented with a list of its arguments,
together with its class docstring
(but not the docstring of the ``__init__()`` method itself):

| *class* ``triangles.shape.Triangle``\ (*a*, *b*, *c*)
|  A triangle is a three-sided polygon.

This gives the user no information
about what those arguments actually mean.

There are actually several ways to remedy this problem.
The first is to take the major step of modifying the Sphinx
``conf.py`` configuration file in your documentation root directory.
I call this step “major” because it will affect how *every* class
in your project gets rendered!
Try adding this option somewhere in ``conf.py``::

 autoclass_content = "both"

The result will be an expanded description of the class
that now appends the ``__init__()`` docstring
to the docstring of the class itself:

| *class* ``triangles.shape.Triangle``\ (*a*, *b*, *c*)
|  A triangle is a three-sided polygon.
|
|  Create a triangle with sides of lengths *a*, *b*, and *c*.

This approach has the advantage
of forcing you to pay attention to your code
and make sure that either each class's own docstring
or that of its ``__init__()`` method
has a reasonable description of its arguments.
But if you find this requirement inflexible,
then instead of setting ``autoclass_content`` project-wide
you will probably just want to tweak the documentation
for each class individually.

How are we going to modify the auto-generated class documentation?
We are going to have to remove the ``:members:`` option,
which is pulling in the ``Triangle`` class
automatically and without giving us a chance to intervene,
and replace it with an explicit request
for the class to be documented.
The ``triangles.shape`` section of ``ref.rst``
will now look like this::

 ``triangles.shape`` — The Triangle class
 -----------------------------------------

 .. automodule:: triangles.shape

    .. autoclass:: Triangle
       :members:

       When instantiating a ``Triangle``,
       provide three positive integers *a*, *b*, and *c*
       that give the lengths of its three sides in clockwise order.

This results in a class whose description starts like this:

| *class* ``triangles.shape.Triangle``\ (*a*, *b*, *c*)
|  A triangle is a three-sided polygon.
|
|  When instantiating a ``Triangle``, provide three positive numbers
   *a*, *b*, and *c* that give the lengths of its three sides in
   clockwise order.

In making this switch,
we have turned off the module-level automatic discovery mechanism entirely,
by removing ``:members:`` from the ``automodule::`` directive;
note that if there were ten classes inside of ``triangles.shape``
instead of just one,
we would now have to list every single one of them
in an ``autoclass::`` statement to get them back!
Well, actually, Sphinx provides an easier solution than that:
instead of removing ``:members:`` entirely,
you can just add an additional ``:exclude-members:`` option
that lists the class that you do not want included automatically
because you have to do them yourself to get them right.

If we want to see this in action,
we can try the same trick with the methods of our class
and replace one of the docstrings
with a description written specially for our documentation::

 .. automodule:: triangles.shape

    .. autoclass:: Triangle
       :members:
       :exclude-members: area

       When instantiating a ``Triangle``,
       provide three positive integers *a*, *b*, and *c*
       that give the lengths of its three sides in clockwise order.

       .. method:: area()

          Returns the area of this triangle, in square units of whatever
          unit was used when the lengths of the sides were provided.

If after this adjustment you will rebuild
and then reload the resulting HTML page,
you will see that the ``area()`` docstring is gone
and is replaced by the description we provided instead.

Order is important
------------------

At this point the ability of Sphinx
to generate an API reference
with almost no participation on your part
is probably looking very alluring!
But one default of the “auto” mechanism
should be mentioned:
it normally puts all of your class's methods in alphabetical order —
after all, Python's introspection is not quite strong enough
for it to see the order in which they were originally specified
in your source code.
And, sometimes, that might be an order
that does not make much conceptual sense.

Of course,
you could try to have such strong tutorial and user-guide documents
that by the time programmers reach your reference manual
they can deal with methods described in any old order;
in some cases they might even appreciate
being able to scroll up and down through the alphabetically
ordered methods to find the one they are looking for!
But, in many cases, a class will have another order
in which its methods are much easier to read:
when the order progress from simple methods and attributes,
into behaviors that involve computation,
and finally on into methods that mutate the class.
You have probably seen this before;
the Python standard library is full of classes
documented with simpler and more basic methods shown first.

Anyway, if you dislike the automatic order,
then there are three remedies
(besides just listing them all over again in your documentation
using explicit directives).
First, the ``:autodoc_member_order:`` option
can be given the value ``bysource`` to tell Sphinx
that you want classes, methods, and attributes
to appear in the same order as they do in your source code.

Second, you can set the member order to ``groupwise``
that puts similar things together,
grouping methods with other methods
and attributes with other attributes.

Finally, Sphinx provides an easy solution for manual ordering
while still pulling the actual documentation from your code:
the ``:members:`` option can take an explicit list
giving the order in which you want members to appear.

::

 .. automodule:: triangles.shape

    .. autoclass:: Triangle
       :members: is_equilateral, is_isosceles, is_similar,
                 perimeter, area, scale

       When instantiating a ``Triangle``,
       provide three positive integers *a*, *b*, and *c*
       that give the lengths of its three sides in clockwise order.

You can also use this trick to include private methods
that Sphinx does not normally document.

Documenting operators
---------------------

You will note that a ``Triangle`` knows how to compare itself
to other triangles:

>>> t1 = Triangle(3, 4, 5)
>>> t2 = Triangle(4, 5, 3)
>>> t1 == t2
True

But this does not appear in our auto-generated documentation
at all, because ``__eq__()`` begins with an underscore!
In general, operations are something that you are going to have to
document yourself.
Doing so will now bring our description of the ``Triangle``
class into pretty good shape::

 .. automodule:: triangles.shape

    .. autoclass:: Triangle
       :members: is_equilateral, is_isosceles, is_similar,
                 perimeter, area, scale

       When instantiating a ``Triangle``,
       provide three positive integers *a*, *b*, and *c*
       that give the lengths of its three sides in clockwise order.

    Triangles also support the equality operator.

       .. method:: triangle1 == triangle2

          Returns ``True`` if the two triangles have sides of the same
          three lengths in the same order (but it is okay if the two
          triangles happen to start their list of sides with a different
          side; 3,4,5 is the same triangle as 4,5,3, but is *not* the
          same triangle as its mirror image 5,4,3).

Exercises
---------

1. Add information to your ``ref.rst`` document
   about how to instantiate a circle,
   including warnings about the exceptions
   that doing so incorrectly may raise.
   Then, add an additional entry to your reference
   detailing how one circle can be compared with another
   using Python's equality operator.
   Be prepared to justify your choice
   of whether you actually show the ``==`` operator
   or instead explicitly document the private ``__eq__()`` method.

2. Class documentation usually also provides information
   about instance attributes, not just about methods.
   After reading the documentation on the ``attribute::`` directive
   on the Sphinx documentation page linked below,
   and then checking how the ``email`` standard library module
   lists its methods and instance attributes,
   go yourself and add descriptions of ``x``, ``y``, and ``r``
   to the circles documentation.

    * http://sphinx.pocoo.org/markup/desc.html
    * http://docs.python.org/library/email.message.html

3. Can you get attribute information to appear automatically,
   so that each attribute description appears both in your source code
   and also in the documentation?
   Read about the ``autoattribute`` directive:

    * http://sphinx.pocoo.org/latest/ext/autodoc.html#directive-autoattribute

4. Some people never use docstrings
   in their “real” documentation,
   choosing instead to write it all from scratch.
   What would your ``ref.txt`` look like
   if you did not permit yourself to use any “auto” directives at all?
   At the bottom of the file,
   try creating a second copy of the ``Circle`` class documentation,
   but this time document the module, the class, and its methods
   from scratch.
   Just document one or two of its methods!
   The point of this exercise is not to waste your time
   documenting the whole interface over again,
   but merely to make you consult the Sphinx documentation
   and try out the non-“auto” versions of the module, class,
   and method directives:

    http://sphinx.pocoo.org/markup/desc.html#object-description-units

5. As we move into the next lesson,
   we will prepare to add tutorial and user-guide information
   to our growing collection of documentation.
   Go ahead and create a ``tut.rst`` document
   entitled “Learning To Work With Circles”
   and a ``guide.rst`` document entitled “Circle Fanciness”
   and link them into your table of contents.

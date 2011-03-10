
4. Doctests, Etcetera
=====================

We now know a little about writing documentation
and about hooking it together using cross references.
It is time to learn about a few more features.

Running examples as doctests
----------------------------

In our tutorial file ``tut.rst``,
we will doubtless add all kinds of useful information
about creating and using triangles.
Per standard Python usage,
we will probably express many of these examples
in terms of doctests,
where we show how our class would behave
if used at the Python prompt::

 After you have created some triangles, you will
 probably want to see whether any of them are the same.
 You can do this by using the standard Python comparison
 operator ``==`` between two triangles.  The triangles
 will compare equal even if they choose a different side
 with which to start listing their lengths:

 >>> from triangles.shape import Triangle
 >>> t1 = Triangle(3, 4, 5)
 >>> t2 = Triangle(4, 5, 3)
 >>> t1 == t2
 True
 >>> t3 = Triangle(6,3,5)
 >>> t1 == t3, t2 == t3
 (False, False)

Do you remember how, during Lesson 1, we answered “yes”
to the question of whether we wanted to be able to run code snippets
as doctests? ::

   > doctest: automatically test code snippets ... (y/N) [n]: y

Thanks to our answer, the module ``sphinx.ext.doctest``
was added to the list of ``extensions`` in our ``conf.py``.
(You always have permission to add the module there later,
if you answered “no” then later realized you want it anyway.)
Which means that we can run our file as a doctest,
by asking for our document
to be processed with the “doctest” formatter
(it's not a real formatter;
that's just what it has to call itself
for ``sphinx-build`` to be willing to run it)
through a command like::

 $ sphinx-build -b doctest . test-output
 Document: ref
 -------------
 1 items passed all tests:
    6 tests in default
 6 tests in 1 items.
 6 passed and 0 failed.
 Test passed.

 Doctest summary
 ===============
     6 tests
     0 failures in tests
     0 failures in setup code
 build succeeded.

If you look inside of the ``test-output`` directory
that you named as the build destination on the command line above,
then you will find an ``output.txt`` file in which the same summary
has been written.

Of course, successful tests are not terribly interesting to look at!
By adding the following line to the bottom of our test suite,
we can see how the doctest routine displays an actual error::

 ...
 >>> Triangle(1,1,9)

And here is what we get back::

 Document: ref
 -------------
 **********************************************************************
 File "ref.rst", line 29, in default
 Failed example:
     Triangle(1,1,9)
 Exception raised:
     Traceback (most recent call last):
       ...
     ValueError: one side is too long to make a triangle
 **********************************************************************
 1 items had failures:
    1 of   7 in default
 ...

This ability to test the code snippets in documentation,
which in earlier ages could only be tested
by laboriously cutting and pasting the snippets into their own files,
is a very popular one among documents in the Python community!
Not only does it guarantee that your code examples are correct,
and prevents older parts of your documentation
from becoming inaccurate as your package continues to evolve,
but it encourages you to write only example code
that can truly be executed by the user at a fresh prompt.
It really makes you think through
whether you have imported every last thing
that the code will need before your users read your docs
and try running it!

Thanks to Sphinx,
you can actually be much fancier than just to implement doctests.
Have you ever read a book where they show you a little script —
a real program, like this, without any prompts in the way?

.. testcode::

 for i in range(3):
     print i

And did they then follow it with the program's output, like this?

.. testoutput::

 0
 1
 2

Well, Sphinx makes it possible to include small scripts like this
that are run and then compared with the next nearest block of output!
This can save lots of time and annoyance
if you have small scripts you want to test
and you don't want to have to wade through them
after pasting them into your document,
figuring out where the rules
would require you to put all of the ``>>>`` and ``...`` prompts.
You simply mark up the two blocks as test code and output, like this::

 .. testcode::

  for i in range(3):
      print i

 .. testoutput::

  0
  1
  2

There are other features supported by the doctest module,
including having test setup routines
that are hidden from the document that gets output
(so that you do not have to bore your readers
with the same ``import`` statements at the top of each file).
Here is the Sphinx documentation
that will let you study this feature in even more detail:

 http://sphinx.pocoo.org/ext/doctest.html

Headings and the table of contents
----------------------------------

By this point you should have
at least three active documents in your ``doc`` directory,
whose content is now included on the front ``index.html`` page
of your rendered documentation.
You should be able to see them listed
if you return to ``index.html``, your documentation's front page,
and look over the table of contents.

There are several options for controlling how the table of contents
is displayed; for more information, check the Sphinx documentation:

 http://sphinx.pocoo.org/concepts.html#the-toc-tree

First, notice that each document in the table of contents
is given its real name, *not* its file name
not some local name defined for it in the ``index.rst`` file;
the title is instead the real value,
taken from the heading at the top of its file.
This is significant: it means that Sphinx
is not making you copy metadata like titles between documents.
Instead, it is copying headings around as needed
to make sure that all of your tables of contents,
indexes, and hyperlinks are consistent.

Exercises
---------

1. Try running the doctest module against
   the documentation you have written in the exercises so far
   for the ``circles`` package.
   Do all of your tests run on your first try?
   If not, see if the error output provided by Sphinx
   is sufficient to help you debug and correct them.
   You get bonus points if you find an error
   in my ``circles`` code itself!

2. Create a small multi-line script using ``circles``
   that prints several lines of result,
   and add it to your documentation as a ``testcode::`` block
   that is followed by a ``testoutput::`` block.
   Run the ``doctest`` renderer
   and confirm that Sphinx is really running your script
   and comparing its output with the desired output!
   Then, reload the HTML in your browser
   and compare the code's appearance
   to that you have created in doctest blocks.

3. Try adding some index entries to your documentation,
   and then rebuild and verify that the new terms
   are now appearing in the HTML page for the index.
   This directive can include all sorts of information
   about the section or paragraph that immediately follows it::

    .. index::
    single: geometry; context
    module: triangles
    triple: polygonal; plane; figures

   Focus on things that you can do with circles:
   “circles, comparing size”; “circles, scaling”;
   and so forth.


1. Getting Started with Sphinx
==============================

The Sphinx system is a framework
for converting attractive and robust plain-text files
into hyperlinked systems of documentation.
To understand the attraction of such a system,
we need to understand plain text, markup,
and what exactly it means for something to call itself a “framework”.

Plain text
----------

“Plain text” files are a world all their own.
Complicated proprietary file formats
have risen and fallen through the ages —
blustering on to the historical stage,
bloating as feature was piled upon feature,
and then waning until eventually your old documents
become the equivalent of ancient hieroglyphics,
impossible to read without a converter.
But plain ASCII text remains what it ever was:
a series of characters that are each simply intended to be displayed,
without being encrusted by hidden codes or binary garbage
designed to make parts of the text bold, italic, or indented.

Have you tried recently to open a Microsoft Word file from 1985?
Or perhaps a WordStar document from 1981?
What are the chances of their displaying correctly
in *any* of the viewers or word processors
that you have installed today?
Yet in the Unix world,
we can confidently open files written in the 1970s
and we always expect them to look *exactly* as they did
when they were first authored.

It is both this simplicity and this permanence
which have made “plain text” files
the basis of all serious programming environments
and operating system configurations to this day.

On the mono-spaced terminals of yore,
plain text files were originally a way of decorating
your screen with whatever patterns of text and symbols
could be conceived of in an 80×24 grid.
Because everyone used a mono-spaced font,
and the *n*\ th character on each line
was guaranteed to line up with the *n*\ th
character on every other line,
a certain amount of artistic freedom was available.
Someone typing a file on one terminal screen
knew that the person who viewed it later
would see it on a nearly identical screen::

          \\|%|//
          | ~ ~ |
         ^( @ @ )^
 -----o000o-\_/-o000o-----

More seriously,
the uniform display characteristics of plain text
allowed the creation of files where many normal textual conventions —
like paragraphs with indented first lines,
block quotes with wide margins,
and centered chapter titles —
could be implemented simply by pressing the spacebar enough times
to horizontally position each line of text. ::


                             - 2 -
                 T h e   S i l e n t   V o i d
                        B o o k   O n e
 -------------------------------------------------------------
               Thus spake the master programmer:

 "When you have learned to snatch the error code from the trap
 frame, it will be time for you to leave."
 -------------------------------------------------------------
                              1.1

 Something mysterious is formed, born in the silent void.
 Waiting alone and unmoving, it is at once still and yet in
 constant motion. It is the  source of all programs. I do not
 know its name, so I will call it the Tao of Programming.

The strict spacing of plain text
could even be pressed into the service of formatting poetry::

  A UNIX saleslady, Lenore, 
  Enjoys work, but she likes the beach more. 
    She found a good way 
    To combine work and play: 
  She sells C shells by the seashore.

As we proceed, then,
we should keep in mind the following benefits of plain text files
(and we will ignore edge cases,
like those people who set their tab stops in unusual places):

1. Plain text files are a permanent format.
2. They tend to display uniformly for everyone.
3. They are *very* easy to version control.

That last point bears repeating!
It can be a terrible lot of work
to compare two versions of the same spreadsheet,
or two copies of the same WordPerfect file,
to see how the document has changed over time.
But text files,
if edited in a way that tends to preserve whole lines intact
when their content does not change,
are eminently suited to version control.
Whether you are using hg or git,
svn or cvs,
or simply running diff by hand,
well-edited text files will yield clear, informative output
if you want to see the differences between them.

Markup, and reStructured Text
-----------------------------

Of course,
despite all of the benefits of plain text,
people often want *more* than “plain” when they go to print or view a file!
They want to read text
that has been typeset in a comfortable and attractive variable-width font
instead of seeing something that looks like it was
pounded out on a typewriter.
They want real bold, italics, and headings that are set in a large font.
They might even need images, diagrams, or real math formulae as well.

To serve this desire there emerged all of the proprietary formats
mentioned in the previous section,
that festooned text with machine-readable binary markup
to communicate type settings to a word processor.
These tended to be the answer in the commercial world.

Over in the bright daylight of the Unix world, by contrast,
systems of human-readable, publicly documented *markup* emerged.
You could still open the source file as plain text,
and see normal words interspersed with snippets of symbols and text
intended to change how the document would be display on the printer.
The ``nroff`` command accepted ``\fBtext\fR`` as the mechanism
for switching to bold;
the impressively complex TeX system used ``{\bf text}``;
and, much later, the angle-bracket madness of HTML
taught us to write ``<b>text</b>``.

But all of these symbols and code produced files
that were difficult to read for the untrained eye —
and, sometimes, not that easy even for someone accustomed to the format!

It finally occurred to someone
that a text system could be designed that was much simpler.
All of the above systems of markup, you see, introduced *new* mechanisms
for indicating bold and indentation and so forth.

“But,” someone asked,
“Don't people *already* have conventions
for marking up their text?
Don't they indicate block quotes in email, already,
by hitting the spacebar to indent a paragraph?
Don't they already use \*asterisks* in email
when they want to emphasize something?

“What if we used *those* conventions —
many of which are already practiced with fair consistency —
as the basis for recognizing markup in a text file?”

Obviously, the implications of such a system are revolutionary.
If normal, casual text markup mechanisms become
the way to signal how your text should be displayed,
then a format would result that read well *both* as plain text
in your editor *and* when formatted for the web or the printed page!

Of course, the idea faced an obstacle:
recognizing a block quote by counting the spaces used to indent it
was tantamount to making whitespace *significant*,
a step that a good many programmers are never willing to take.
But here in the Python community
we went ahead and embraced significant indentation long ago!
Extending the idea to our text files
allowed us to take advantage of a unique quirk in our arsenal of Pythonisms
and apply it in a situation where it was a big win:
it allows us to group together lines in a text file
without needing braces, or backslashes, or angle brackets,
simply by teaching the computer to notice
what the human eye notices immediately —
that the left edge of several rows of text are lined up!

Jim Fulton of the Zope project got us started with “Structured Text”.
David Goodger then took the idea further,
developing and refining the format
that we know today as “reStructuredText” (or “RST” for short).

A quick RST example
-------------------

If you are new to the format,
a quick Google search will provide links to several good primers
and introductions explaining now it works.
I myself rarely write a complicated document
without having the useful quick reference page
opened somewhere in a browser tab:

 http://docutils.sourceforge.net/docs/user/rst/quickref.html

But I often learn a new idea best if I see it in action,
so here, to start your off, is a small document explaining RST
by illustrating the format as it goes:

.. literalinclude:: sample.txt
   :language: rst

Running quickstart
------------------

The wonder of a *framework* these days
is that it lets you start your project from a working starting point.
Gone are the days when you would slog through pages of tutorial,
carefully setting up file after file,
hoping that you made no mistakes
before reaching the last page
where it finally said to type “go”
and you got to see whether you set up all those files correctly
to produce a working, interlocking system.

The Sphinx framework is like other modern frameworks:
rather than leaving you to crawl your way towards a working system,
it provides a single quick-start command
to move you to the starting line
where a simple document system is already set up and working.

For this tutorial,
we are going to consider two simple Python packages.
You are being given copies of both of them on the media
provided to you as you enter the classroom.
One package, named ``triangles``, will “belong” to me, the presenter:
during my short lecture segments
I will start adding documentation to it,
to show you the steps.
Then, during the exercises, you will turn your attention
to the ``circles`` package
and try out the techniques yourself by writing documentation for it.

So let's start by looking at the ``triangles`` package!
Besides its simple and standard ``setup.py``,
it contains three files: an empty ``__init__.py``,
a ``shape.py`` module implementing a simple class,
and finally a ``utils.py`` module offering functions
for users who want to do triangle operations
without having to wade into the object-oriented interface.
Here is how all of those files are laid out::

 example1/
 |-- setup.py
 `-- triangles/
     |-- __init__.py
     |-- shape.py
     `-- utils.py

By changing directory to ``example1``
and running a recent version of Python,
you can go ahead and try out
some of the simple operations the module supports::

 >>> from triangles import utils
 >>> utils.is_isosceles(4, 5, 5)
 True
 >>> utils.is_isosceles(4, 5, 6)
 False
 >>> utils.is_isosceles(1, 2, 10)
 Traceback (most recent call last):
   ...
 ValueError: one side is too long to make a triangle

Yes, I know, not rocket science.
But the module's point is, precisely, to be simple:
an easy enough Python product
that we can all understand it instantly on our first reading,
and spend our time in this tutorial writing its documentation
instead of puzzling over how it works!

So how do we add documentation?
After making sure that your current Python environment
has the ``Sphinx`` package installed from PyPI,
move into the ``example1`` directory and run ``sphinx-quickstart``,
answering the questions this way::

   $ sphinx-quickstart
   Welcome to the Sphinx quickstart utility...

   > Root path for the documentation [.]: doc
   > Separate source and build directories (y/N) [n]: n
   > Name prefix for templates and static dir [_]: _
   > Project name: Triangles
   > Author name(s): Brandon
   > Project version: 1.0
   > Project release [1.0]: 
   > Source file suffix [.rst]: .rst
   > Name of your master document (without suffix) [index]: index
   > Do you want to use the epub builder (y/N) [n]: n
   > autodoc: automatically insert docstrings ... (y/N) [n]: y
   > doctest: automatically test code snippets ... (y/N) [n]: y
   > intersphinx: ... (y/N) [n]: n
   > todo: ... (y/N) [n]: n
   > coverage: ... (y/N) [n]: n
   > pngmath: ... (y/N) [n]: n
   > jsmath: ... (y/N) [n]: n
   > ifconfig: ... (y/N) [n]: n
   > viewcode: include links to the source code ... (y/N) [n]: y
   > Create Makefile? (Y/n) [y]: y
   > Create Windows command file? (Y/n) [y]: y

After surviving this barrage of questions,
our project now contains a documentation directory
complete with a working build system ready to be invoked::

 example1/
 |-- doc/
 |   |-- Makefile
 |   |-- _build/
 |   |-- _static/
 |   |-- _templates/
 |   |-- conf.py
 |   |-- index.rst
 |   `-- make.bat
 |-- setup.py
 `-- triangles/
     |-- __init__.py
     |-- shape.py
     `-- utils.py

As you can see, Sphinx has given us everything we need:
a single documentation file to start editing (``index.rst``),
a configuration file that we can edit later
if we repent of any of our answers to its questions (``conf.py``),
and either of two different build files
ready to direct the generation of our documentation
(the ``Makefile`` for Unix folks, and ``make.bat`` for Windows).

Building HTML output
--------------------

If you take a look at ``index.rst``,
you will see that it is simply a title
followed by directives to generate a table of contents
and links to several indexes.
Let's go ahead and test the build system
by converting this simple document
into HTML for consumption through a web browser::

 $ cd doc
 $ pwd
 .../example1/doc
 $ make html
 sphinx-build -b html -d _build/doctrees   . _build/html
 Making output directory...
 Running Sphinx v1.0.7
 ...
 build finished. The HTML pages are in _build/html.

If you examine your directory tree now,
you will see that the number of files present has more than doubled!
Without any further effort on your part,
Sphinx has converted that single tiny ``index.rst`` document
into an ``index.html`` file sitting at the center
of a protective cocoon of CSS files, JavaScript source code,
and images::

 example1/
 |-- doc/
 |   |-- Makefile
 |   |-- _build/
 |   |   |-- doctrees/
 |   |   |   |-- environment.pickle
 |   |   |   `-- index.doctree
 |   |   `-- html/
 |   |       |-- _sources/
 |   |       |   `-- index.txt
 |   |       |-- _static/
 |   |       |   |-- basic.css
 |   |       |   |-- default.css
 |   |       |   |-- doctools.js
 |   |       |   |-- file.png
 |   |       |   |-- jquery.js
 |   |       |   |-- minus.png
 |   |       |   |-- plus.png
 |   |       |   |-- pygments.css
 |   |       |   |-- searchtools.js
 |   |       |   |-- sidebar.js
 |   |       |   `-- underscore.js
 |   |       |-- genindex.html
 |   |       |-- index.html         <-- the resulting output
 |   |       |-- objects.inv
 |   |       |-- search.html
 |   |       `-- searchindex.js
 |   |-- _static/
 |   |-- _templates/
 |   |-- conf.py
 |   |-- index.rst                  <-- our single source file
 |   `-- make.bat
 `-- ...

This example lets us illustrate early an important point:
Sphinx wants you to provide a single ``.rst`` file
for each page of HTML output you want produced,
which will also each be a chapter in the PDF output
if you choose to produce a printed document.
You have no choice about this;
for Sphinx, an HTML page and a book chapter are equivalent,
and your documentation will always have as many of each
as there are ``.rst`` files in your document source.

Sphinx does now offer a build option
for concatenating all of your documentation chapters
into one big single HTML page.
But the point is that you cannot easily
split up the printed chapters one way
while splitting the generated web pages some other way.

Point your browser at the new HTML file,
using a URL something like this::

 file:///home/brandon/.../_build/html/index.html

You will see the result of our successful ``make``:
the text inside of ``index.rst`` is now formatted as an
(admittedly ugly) web page!

Building documentation from docstrings
--------------------------------------

To bring this first lesson to a close,
let's make some documentation appear quickly, using a shortcut:
we can ask Sphinx to pull in the docstrings of our Python module
to create a basic reference to the classes and functions
that our package supports.

Some people are against this practice,
as they think that the “internal” documentation
that docstrings make available for IDEs
(“Integrated Development Environments”, like TextMate,
where you right-click on an identifier and expect to have the option
to “Display documentation” for that method)
and for the use of Python's ``help()`` function
are not adequate to serve as printed documentation on the page.
But for our example today it should serve just fine!

First, we will edit that ungainly ``index.rst``
that the Sphinx quickstart produced
by paring it down to something like this::

 Welcome to the Triangles module
 ===============================

 .. toctree::
    :maxdepth: 2

    ref

This will reduce our title page to a simple table of contents for now,
that attempts to reference a single document named ``ref.rst``.
You will get an error right now if you try running ``make``,
since this file does not exist yet.
Go ahead and create it,
right next to ``index.rst``, and give it this content::

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

If you compare what you have just written in ``ref.rst``
with the sample RST file shown earlier,
you will see that we are talking to Sphinx
by using a feature of RST called *directives* —
lines that look kind of like comments
(and which, indeed, do not show up literally in the output),
but that have a directive name followed by a double-colon
as the first word of the comment (like ``automodule::``).
These tell Sphinx to do special operations,
like, in this case, looking inside of our ``triangles`` package
and pulling the docstrings out and into our document.

Finally, all of those colon-delimited directives
are going to need to be able to *find* our ``triangles`` package
before they can succeed!
As you can see from the directory tree shown above,
our ``doc`` directory lies one level beneath the directory
where the ``triangles`` package itself can be found,
so we have to tell our Sphinx configuration
to look in our parent directory (called ``..`` in Unix)
to find Python packages when it goes looking for them.
To do this, visit the top of ``conf.py``
and, following the instructions in the comment,
add a line that puts the parent directory in ``sys.path``::

 # If extensions (or modules to document with autodoc) are in another directory,
 # add these directories to sys.path here. If the directory is relative to the
 # documentation root, use os.path.abspath to make it absolute, like shown here.
 #sys.path.append(os.path.abspath('.'))
 sys.path.append(os.path.abspath('..'))

When these three changes are complete —
mentioning the ``ref`` document in ``index.rst``,
writing the ``ref.rst`` file itself,
and adding ``..`` in the ``conf.py`` file —
then you can safely run::

 $ make html

The result should be an ``index.html`` file
that now shows the reference document in its table of contents
(hit “reload” in your browser to verify this),
and a reference document ``ref.html``
that has pulled in the package docstrings
as a first attempt to give us some useful documentation.
Bask for a moment in the glory of how much you have accomplished
with, so far, fairly little effort.

Batteries included: search and index
------------------------------------

Before going further, we should notice one more thing
about this tiny documentation system that we have created:
it already has a fully-functioning index
*and* a built-in JavaScript-powered search engine!

Verify this for yourself by clicking the “index” link
in the upper-right of the ugly blue theme
that Sphinx has wrapped around your pages,
and then clicking on some of the index entries
to confirm that they take you into the right location
in your document.
Then, try entering some text —
even a substring like “equi”! —
into the “Quick search” box at the left of each page
and verify that full-text search is already working as well.

Just by bringing Sphinx up and pointing it at our package,
we already have a reference document up and running
that is *both* indexed and searchable
without any further work on our part.

Exercises
---------

1. The instructor will have provided a ``circles`` module,
   similar in many ways to the ``triangles`` module
   with which the above demonstrations were performed.
   Move into its directory, create a ``doc`` subdirectory
   using ``sphinx-quickstart``,
   and verify that you can build documentation there.

2. Add a ``ref.rst`` document for ``circles``
   using the same conventions as we used above.

3. With any extra time you have while the other students
   struggle to get Sphinx
   installed and running on their Windows machines or whatever,
   read through the ``circles`` documentation you have just produced
   and try the package out by calling it from the Python prompt.
   This will prepare you to start documenting the package by hand,
   which is a process we will learn to start in the next lesson.

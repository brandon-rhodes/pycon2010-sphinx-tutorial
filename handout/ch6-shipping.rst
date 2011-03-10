
6. Shipping Your Documentation
==============================

There are several hints and tips
which should help you get copies of your documentation
everywhere that you need it.

Version control
---------------

Whether to only version control your RST files,
or to go all the way and save the HTML output too,
is a more interesting question than you might think.

Many developers only ever use version control on source files,
for several reasons.

First, because not committing the HTML output to version control
saves space,
both physically on the disk
and also conceptually because fewer files are being stored
and re-created with each clone of the repository.
You never, after all, *need* to keep around
the output files produced by Sphinx;
you should be able to delete them
and later regenerate them all from source
simply by re-running ``make``.

And, second, because it is redundant: 
by storing the same information twice,
you can create awkward situations.
For example, what if one developer updates an RST file
and then forgets to run ``make html`` before committing?
Then other collaborators who check the code out
will find two versions of the documentation
that are out of sync with each other,
and when they themselves type ``make html``
then they will have to log a commit
just to get things back to normal.

But against these two prudent warnings
stands the fact that some developers
do not have Sphinx installed at all,
and want to be able to download a package
and read its documentation in their browser
without doing any builds on their own.
By checking the HTML files into version control,
you can guarantee that the docs will always be there,
immediately upon checkout and without your having to remember
to rebuild them.

But if you do want to avoid version controlling the various
compiled versions of the documentation that you produce,
then, thanks to the Sphinx design,
then you will find it easy to convince your
version control system to avert its eyes:
*every* file that Sphinx writes and updates
get written somewhere inside of the ``_build`` directory!
Simply add the ``_build`` directory's name to your version control
system's exclusion list (like the ``svn:ignore`` value
on its parent directory,
or in your ``.hgignore`` file)
and the temptation to commit the built files will go away.

There are actually tricks,
if you are interested,
which can make your documentation browsable
right *inside* of your favorite version control store!
If you have chosen to commit the HTML files,
then many version control systems
that support HTTP or HTTPS as a protocol
have a way to mark each stored file
with the MIME type with which they should be returned to a web browser.
If, for example, you mark all of your ``.html`` documents as ``text/html``,
then you should find that they come up as fully-rendered web pages
when you visit their version control URL.
Not only might this let you avoid setting up a separate web site,
but it means that you can create links
to particular versions of the documentation —
like the documentation from the old 1.2 version of your utility,
or the documentation on a branch
you are developing for a particular client —
and the version control system will give everyone the right
version of the docs without confusion.

Distributing documentation
--------------------------

This is a subject on which I will only say a few words
here in these class notes,
because the situation is a fairly complex one
given the different choices
that the ``distutils`` and ``setuptools`` make
when they decide on what files to distribute with a package.
But it usually seems that documentation
is something that tends to get included
when you download the source version of a package,
but that Python packages leave out
when you install them in binary form.

Now it turns out that I think this is the wrong practice.
After seeing the consequences of both choices over many years,
I have become a firm believer
in the idea that a package should *always* travel with its
documentation, and that the two should never be parted.
Therefore, I *always* move my ``doc`` directory
inside of my package itself.
Since the ``doc`` directory lacks an ``__init__.py`` file,
it is in no danger of being mistaken for one of your own packages!
It can safely sit inside of the ``triangles`` directory
or ``circles`` directory,
and can always be there for the kind of developer, like me,
who looks inside of the Python egg
hoping to find some documentation.

Also, including your documentation when your package is installed
lets users invoke your doctests themselves
to verify whether the way they have the package installed
really supports all of those neat calls in your Tutorial
that they can't quite seem to get working in their own program!

In my popular “PyEphem” project,
I found the following line sufficient in my ``MANIFEST.in``
to make sure that my documentation always gets included
when my package is installed::

 include src/ephem/doc/*

Other formats
-------------

There are several other forms
in which Sphinx can output your documentation
so that you can enjoy it in even more ways!

* Programmers will be interested to know
  that your documentation can be saved in a raw data format,
  so that you can more easily process it with a program.
  The native Python “pickle” format is supported,
  along with the more universal and portable JSON format.

* Documentation can be output in various help-file formats.

* The ``changes`` format, which is primarily for developers,
  lists all directives
  from anywhere in the documentation
  that indicate that a feature is being added, changed,
  or deprecated in the current version;
  this can be useful for writing up changelogs
  and otherwise distilling how your package's API
  is in the process of changing.

* The ``linkcheck`` routine tests every external hypertext link
  in your document, and reports on whether any of them point to
  sites or pages that no longer seem to exist.

* Finally, what documentation system would be complete
  without the ability to print on good, old-fashioned paper?
  Generating a PDF is rather straightforward *if*
  you have a recent version of the TeX typesetting system.
  Specifically, you will need “latex”;
  but on my Ubuntu box,
  I simply installed the ``texlive-full`` package,
  and from then on the following dance has been sufficient
  to turn my documentation into a PDF::

   $ make latex && (cd _build/latex; make all-pdf)

  Obviously, if your system lacks such a conveniently-packaged
  latex, you could wind up spending a good deal of time
  getting it compiled and installed!

But the important thing, in the end,
is to get your documentation into the hands of your users
in *some* form, whether it's perfect yet or not!

Exercises
---------

1. Move your documentation tree beneath the ``circles`` directory
   so that it becomes part of your package.
   First, verify that you can still build the documentation,
   and if not then adjust any paths in ``conf.py`` that are necessary
   to getting it working again.

2. Run the ``setup.py`` commands ``sdist`` and ``bdist``
   in the ``example2`` directory and determine, for each kind
   of distribution, whether your documentation files get
   included in the resulting archives.
   If not, then make the necessary adjustments
   so that the documentation is always distributed with the code,
   and always gets installed beneath it in a ``doc``
   directory beneath the ``circles`` package directory itself.

3. BONUS: Build the documentation you have written as a PDF.

4. BONUS: Export your documentation in a data format
   like pickle or JSON.
   Then write a few lines of Python code
   and read the file back in,
   showing that the data is intact.

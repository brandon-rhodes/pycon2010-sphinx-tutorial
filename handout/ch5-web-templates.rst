
5. Theming Sphinx
=================

Instead of writing an entire chapter here
on how to write CSS and HTML and design for the web,
I am going to plan on this lesson being more interactive.
Using a worked-out example that I will bring along,
we will look at what is involved
in entirely replacing the ugly default Sphinx theme
with a much more elegant one.
This will involve combining a standard browser reset file
with a simple template that is placed in the ``_templates``
directory in the standard Sphinx documentation directory structure —
which, in case you do not recall from earlier, is::

 doc/
 |-- Makefile
 |-- _build/
 |-- _static/
 |-- _templates/
 |-- conf.py
 |-- index.rst
 `-- make.bat

Did you notice how,
when you generated an HTML version of your documentation,
lots of static and template information appeared out of nowhere?
After our build, you will remember,
the HTML directory structure looked like::

 html/
 |-- _sources/
 |   `-- index.txt
 |-- _static/
 |   |-- basic.css
 |   |-- default.css
 |   |-- doctools.js
 |   |-- file.png
 |   |-- jquery.js
 |   |-- minus.png
 |   |-- plus.png
 |   |-- pygments.css
 |   `-- searchtools.js
 |-- genindex.html
 |-- index.html
 |-- objects.inv
 |-- search.html
 `-- searchindex.js

Basically, all of the files you see in ``_static``,
as well as the master page design itself,
are yours to replace
if you will simply create files with the same names
in the ``_static`` and ``_templates`` directories
alongside your source code.
Sphinx looks for files there with its standard names,
and will use them instead of the default template and style sheet
that it normally uses.

Exercises
---------

1. Change the ``html_theme`` specified in your project's ``conf.py``
   from its normal value of ``default``
   to the more edgy value of ``sphinxdoc``.
   This will illustrate how different your documentation can look
   with a simple change of design.
   The online Sphinx documentation
   now provides image previews of how each built-in theme looks:

   http://sphinx.pocoo.org/latest/theming.html#builtin-themes

2. Using pencil and paper if it's easiest,
   and perhaps by looking at other web site designs,
   design how you would want your documentation to look.
   Figure out where things like the search bar,
   current document table of contents,
   and link back to the top document should go.
   How would you arrange the previous, next, and index links
   to make their navigational importance obvious enough?

3. If you have any web skills,
   experiment with adjusting the template and style sheet
   that come with Sphinx by default.
   (Once you have run ``make`` ``html`` once,
   you can just copy them over from the output directory tree
   and into your source tree!)
   What changes are easy to make this way,
   and what kind of changes does Sphinx make hard?

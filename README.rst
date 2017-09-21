This module implements a parser for the Bricks Markup Language (BLM). Bricks is
a Python module that implements HTML as subset of Python, something like this:

.. code-block:: python

    from bricks.html5 import *

    div(class_="example")[
        h1("Title"),
        p("Hello world!"),
    ]

The main goal of Bricks is to replace string based template languages such as 
Jinja or Django templates by regular Python objects as a way of rendering HTML. 
With Bricks, you can use the full power of Python and don't have to learn a 
new Python-like templating language that breaks in subtle and annoying ways.

That said, while Python is a very expressive language, it was not designed to 
represent text. Bricks is an acceptable way to represent HTML, but it is not a 
perfect fit. There are sittuations we may want to compromise, and this is 
Bricks Markup Language (BML): it is a markup language designed to represent 
HTML more compactly that is inspired on Bricks syntax and can emit Bricks 
objects or HTML strings as results.

BML extends HTML with support for variables, functions, conditional evaluation,
loops and some rudimentary data types (the ones you would see in JSON).


The syntax
==========

Consider this generic pseudo-HTML structure

.. code-block:: html 
    
    <a attr1="foo" attr2="bar">
        <b>Some <c>text.</c></b>
        <d><--! a self-closing tag! -->
        Bye!
    </a>

The same structure can be represented in BML as:

.. code-block:: bml

    a(attr="foo", attr="bar")
        b Some \c[text]
        d  // A self closing tag!
        . Bye!

Like Python, BML has meaningful indentation. An indented element in a block 
is considered to be a child for the the opening tag. Each line should start 
with a tag, that optionally can declare attributes using the function call 
syntax::

    h1 Title
    p(class="main-text") Hello world! 

If you want to insert text without any specific parent tag, just put a leading 
dot::

    div
        p Some text inside a <p>
        . This is just plain text

A tag element might be followed by a dot to tell that the containing text may
span several lines

    p. This is a paragraph. It can span several lines.
        But all lines must be indented with a higher level than the starting p.
    p. This is another paragraph.

Tags can be present in a line of text. BML uses the "\tag-name[content]" syntax 
to mark those tags::

    p. A \b[bold] text.
    p. With \span(class="opt")[text]

Writing HTML is generally awful. BML encourages using Markdown when possible::

    p:md. 
        In order to enable *Markdown* mode, simply puts the :md suffix after 
        the tag. It will assume that the contents of the tag are plain Markdown.
        
        * It is more readable.
        * Less typing.
        * Made for humans!
        * It accepts \b[raw] BML.

If you need to insert raw text data, just use the #::

    pre#. 
        # This is verbatim mode. No BML command is recognized.
        
        def fib(x):
            return 1 if x <= 1 else fib(x - 1) + fib(x - 2)

You may combine two levels of nesting using the > operator::

    code > pre#.
        print("Hello World!")


Extensions
==========

Bricks ML can define variables that can later be used to perform substitutions::

    # answer = 42
    # my_class = "Foo"
    p(class=my_class) What is the answer?
    p The answer is $answer

It also accepts functions::

    # f(x: Number) = 2 * x
    # function g(x) 
        div(class=x)
            p $x $x $x

Functions can be called as block or inline::

    g(42)
    p Or inline: \g(42)

Conditional execution::

    # if x == 42
        p The answer!
    # else
        p Answer: $x

Loops::

    div
        # for x in L
            p name: $x.name, age: $x.age.
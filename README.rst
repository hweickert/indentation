===============================
indentation
===============================

Text indentation functions.

-------------------------------
Usage
-------------------------------
Indenting to a specific level:

.. code::

    >>> import indentation
    >>> indentation.set( "hello", 1 )
    '    hello'

    >>> indentation.set( "    hello", 0 )
    'hello'


Indenting to a specific level (and keeping relative lines in place):

.. code::

    >>> import indentation
    >>> print( indentation.set("hello\n    world", 1) )
        hello
            world
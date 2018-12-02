tc
==

``tc`` is a simple console-based tool for the tracking of time. Since it
is at an early stage of development, it has currently just a basic feature
set, which may however change in the future.


Installation
------------

The easiest way to install ``tc`` is via ``pip``:

::

    pip install -U https://github.com/keans/tc/archive/master.zip


Hint: Note that all data will be stored in ``~/.config/tc/``.


Examples
--------

Start a new project ``myproject``

::

  tc start myproject +tag +me


Status check currently running project:

::

  tc status


Stop the currently running project and add it to the list of
completed projects:

::

  tc stop


List all completed projects:

::

  tc list

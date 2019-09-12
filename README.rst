====
joke
====
.. image:: https://img.shields.io/pypi/v/axju-jokes
   :alt: PyPI
   :target: https://pypi.org/project/axju-jokes/

.. image:: https://img.shields.io/pypi/pyversions/axju-jokes
   :alt: Python Version
   :target: https://pypi.org/project/axju-jokes/

.. image:: https://img.shields.io/pypi/wheel/axju-jokes
   :alt: Wheel
   :target: https://pypi.org/project/axju-jokes/

.. image:: https://img.shields.io/pypi/implementation/axju-jokes
   :alt: Implementation
   :target: https://pypi.org/project/axju-jokes/

.. image:: https://img.shields.io/pypi/dm/axju-jokes
   :alt: Downloads
   :target: https://pypi.org/project/axju-jokes/

.. image:: https://img.shields.io/github/license/axju/joke
   :alt: GitHub
   :target: https://pypi.org/project/axju-jokes/

Jokes for python.

I was really sad, no package called joke. So I decided to create one, really
fast. This package have some functions, that return some jokes, quotes or facts.
If you are sad, use the joke packages. :)

Install
-------
::

  pip install axju-jokes

Command line
------------
You can exit the function from the command line. There are two entry points:

.. code-block:: shell

  $ joke
  $ python -m joke

With no arguments, it will return a random joke, quote or fact. You can set one
specifically API. For example some cat facts:

.. code-block:: shell

  $ joke cat

Use help to see the possible API's:

.. code-block:: shell

  $ joke --help

Examples
--------
Some jokes examples

.. code:: python

  from joke.jokes import *
  # This will import all joke-functions (geek, icanhazdad, chucknorris, icndb)
  # Now you can use them to get some jokes.

  # For example you can display 10 Chuck Norris jokes.
  for i in range(10):
      print(chucknorris())

  # Or get a random joke-function.
  from random import choice
  print(choice([geek, icanhazdad, chucknorris, icndb])())

Some quotes examples

.. code:: python

  from joke.quotes import *

  # get a quote from quotesondesign.com
  print(quotesondesign())

  # you can get more then one with one request
  for quote in quotesondesign(5):
      print(quote)

  # and you can get the data
  data = quotesondesign(format='data')
  print(data['quote'])
  print(data['author'])


  # get quote from stormconsultancy.co.uk
  print(stormconsultancy())

  # You can set the ID to get a specific quote
  print(stormconsultancy(id=2))

  # the stormconsultancy-function give you also the data
  data =stormconsultancy(id=2, format='data')
  print(data['quote'])
  print(data['author'])

Check also the example folder.

Import Easter Egg
-----------------
::

  >>> import joke.eggs
  Chuck Norris has to register every part of his body as a separate lethal weapon.
  His spleen is considered a concealed weapon in over 50 states.

API's
-----
To get the jokes, I use some open API's. If you know some missing API's, please
contact me. Until now, the following API's are used.

- https://geek-jokes.sameerkumar.website/api
- https://icanhazdadjoke.com/
- https://api.chucknorris.io/jokes/random
- http://api.icndb.com/jokes/random/
- http://quotesondesign.com/wp-json/posts
- http://quotes.stormconsultancy.co.uk
- https://cat-fact.herokuapp.com/facts/random


Development
-----------
Clone repo::

  git clone https://github.com/axju/joke.git

Create virtual environment for Linux::

  python3 -m venv venv
  source venv/bin/activate

Create virtual environment for Windows::

  python -m venv venv
  .\venv\Scripts\activate

Update dev-tools::

  python -m pip install --upgrade wheel pip setuptools twine tox flake8

Install local::

  python setup.py develop

Run some tests::

  tox
  python -m unittest discover
  python setup.py test

Publish the packages::

  git tag -a 1.0.3 -m '1.0.3'
  git push origin 1.0.3
  python setup.py --version
  python setup.py check
  python setup.py sdist bdist_wheel
  twine upload dist/*

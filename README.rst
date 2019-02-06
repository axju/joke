====
joke
====
Jokes for python.

I was really sad, no package called joke. So I decided to create one, really
fast. This package have some functions, that return some jokes, quotes or facts.
If you are sad, use the joke packages. :)

Install
-------
::

  pip install joke

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

  git clone https://github.com/axju/txt2image.git

Create virtual environment and update dev-tools::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip setuptools twine tox

Install local::

  pip install -e .

Run some tests::

  tox
  python -m unittest discover
  python setup.py test

Publish the packages::

  python setup.py sdist bdist_wheel
  twine upload dist/*

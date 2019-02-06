import argparse
from random import choice

from joke import __summary__
from joke.jokes import *
from joke.quotes import *
from joke.facts import *

map_func = {
    'geek': geek,
    'icanhazdad': icanhazdad,
    'chucknorris': chucknorris,
    'icndb': icndb,
    'storm': stormconsultancy,
    'quote': quotesondesign,
    'cat': cat,
}

def main():
    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument('func', nargs='?', choices=[s for s in map_func])
    args = parser.parse_args()

    if args.func:
        func = map_func.get(args.func)
    else:
        func = choice([f for s, f in map_func.items()])
    print(func())

if __name__ == '__main__':
    main()

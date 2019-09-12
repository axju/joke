import argparse
from random import choice

from joke.jokes import geek, icanhazdad, chucknorris, icndb
from joke.quotes import quotesondesign, stormconsultancy
from joke.facts import cat

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
    parser = argparse.ArgumentParser(description='Jokes for python')
    parser.add_argument('func', nargs='?', choices=[s for s in map_func])
    args = parser.parse_args()

    if args.func:
        func = map_func.get(args.func)
    else:
        func = choice([f for s, f in map_func.items()])
    print(func())


if __name__ == '__main__':
    main()

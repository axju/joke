from joke.jokes import geek, icanhazdad, chucknorris, icndb
from random import choice

# display a random joke if the module are imported
# >>> import joke.eggs
# Chuck Norris doesn't read books. He stares them down until he gets the
# informati on he wants.
print(choice([geek, icanhazdad, chucknorris, icndb])())

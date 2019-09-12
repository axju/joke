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
data = stormconsultancy(id=2, format='data')
print(data['quote'])
print(data['author'])

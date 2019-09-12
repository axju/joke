from requests import get
from random import randint


__all__ = ['quotesondesign', 'stormconsultancy']


def get_quotesondesign():
    r = get('https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand')
    result = []
    if r.status_code == 200:
        data = r.json()
        for d in data:
            result.append({
                'id': d['id'],
                'quote': d['content']['rendered'],
                'author': d['title']['rendered'],
            })
    return result


def quotesondesign(n=1, format='txt'):
    """
    Get some quotes. The default arguments return one quote as a string.
    You can also get a list of quotes if you change n.
    If You want the data uses format='data'.
    """
    result = []
    quotes = get_quotesondesign()
    while len(result) < n and quotes:
        result += [quotes.pop()]
        if not quotes:
            quotes = get_quotesondesign()

    if format == 'txt':
        result = list(map(lambda x: '{}\n\n--{}'.format(x['quote'], x['author']), quotes))

    if len(result) == 1:
        return result[0]
    return result


def get_stormconsultancy(id):
    r = get('http://quotes.stormconsultancy.co.uk/quotes/{}.json'.format(id))
    if r.status_code == 200:
        data = r.json()
        return {
            'quote': data['quote'],
            'author': data['author'],
            'id': id}


def stormconsultancy(id=None, format='txt'):
    if not id or id <= 0 or id > 44:
        id = randint(1, 44)
    data = get_stormconsultancy(id)
    if format == 'txt':
        return '{}\n\n--{}'.format(data['quote'], data['author'])
    return data

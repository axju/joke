from requests import get
from html2text import html2text
from random import randint

__all__ = ['quotesondesign', 'stormconsultancy']

def get_quotesondesign(n):
    r = get(f'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]={n}')
    if r.status_code == 200:
        data = r.json()
        for d in data:
            yield {
                'quote': html2text(d['content']).replace('\n', ' ').strip(),
                'author': d['title'],
                'id': d['ID'],}

def quotesondesign(n=1, format='txt'):
    """
    Get some quotes. The default arguments return one quote as a string.
    You can also get a list of quotes if you change n.
    If You want the data uses format='data'.
    """
    if n == 1:
        data = list(get_quotesondesign(1))[0]
        if format == 'txt':
            return '{}\n\n--{}'.format(data['quote'], data['author'])
        return data

    if format == 'txt':
        return ['{}\n\n--{}'.format(data['quote'], data['author']) for data in get_quotesondesign(n)]
    else:
        return [data for data in get_quotesondesign(n)]


def get_stormconsultancy(id):
    r = get(f'http://quotes.stormconsultancy.co.uk/quotes/{id}.json')
    if r.status_code == 200:
        data = r.json()
        return {
            'quote': data['quote'],
            'author': data['author'],
            'id': id,}

def stormconsultancy(id=None, format='txt'):
    if not id or id<=0 or id>44:
        id = randint(1, 44)
    data = get_stormconsultancy(id)
    if format == 'txt':
        return '{}\n\n--{}'.format(data['quote'], data['author'])
    return data

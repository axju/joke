from requests import get


__all__ = ['geek', 'icanhazdad', 'chucknorris', 'icndb']


def geek():
    r = get('https://geek-jokes.sameerkumar.website/api')
    if r.status_code == 200:
        return r.text[1:-2]


def icanhazdad():
    headers = {'Accept': 'text/plain'}
    r = get('https://icanhazdadjoke.com/', headers=headers)
    if r.status_code == 200:
        return r.text


def chucknorris():
    r = get('https://api.chucknorris.io/jokes/random')
    if r.status_code == 200:
        return r.json()['value']


def icndb():
    r = get('http://api.icndb.com/jokes/random/')
    if r.status_code == 200:
        return r.json()['value']['joke']

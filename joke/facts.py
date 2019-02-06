from requests import get


def cat():
    r = get('https://cat-fact.herokuapp.com/facts/random')
    if r.status_code == 200:
        return r.json()['text']

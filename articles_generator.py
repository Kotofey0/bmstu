# coding: utf-8

import urllib


AVAILABLE_ARTICLE_THEMES = [
    'astronomy',
    'geology',
    'gyroscope',
    'literature',
    'marketing',
    'mathematics',
    'music',
    'polit',
    'agrobiologia',
    'law',
    'psychology',
    'geography',
    'physics',
    'philosophy',
    'chemistry',
    'estetica'
]


def generate_title():
    raw_title = urllib.urlopen('https://referats.yandex.ru/creator/write/').read()
    return raw_title.decode('utf-8').capitalize()


def generate_article(themes):
    for topic in themes:
        assert topic in AVAILABLE_ARTICLE_THEMES
    url_template = 'https://referats.yandex.ru/referats/write/?%s'
    url = url_template % urllib.urlencode({'t': '+'.join(themes)})
    raw_text = urllib.urlopen(url).read().decode('utf-8')
    article = '<p>%s' % '<p>'.join(raw_text.split('<p>')[1:])
    return article




def create_article_json():
    articles = []

    for i in range(100):
        articles.append({'name':generate_title().encode('utf-8'), 'text':generate_article(AVAILABLE_ARTICLE_THEMES).encode('utf-8'), 'author':'Yandex R.'})

    import json

    try:
        json.dump(articles, open('articles.json', 'w'))
    except IOError:
        print 'IOError'

create_article_json()



# coding: utf-8
import json


try:
    list = json.load(open('articles.json', 'r'))
except IOError:
    print 'File not found!'
    print 'Stop'
    exit()


with open('test.html', 'w') as f:
    for article in list:
        f.write('<h1>' + article['name'].encode('cp1251') + '</h1>')
        f.write('<div>' + article['text'].encode('cp1251') + '</div>')
        f.write('<h5>' + article['author'] + '</h5>')


def page_output(page, page_max, way, list0):
    if way == 'console':
        for article in list0[page_max*(page - 1): page_max*page]:
            print article['name'] + u'                                  Author: ' + article['author']
            print article['text'] + ' #'
            print '* * *\n'

    else:

        with open(way, 'w') as f:
            for article in list[page_max*(page - 1): page_max*page]:
                
                f.write('<h1>' + article['name'].encode('cp1251') + '</h1>')
                f.write('<div>' + article['text'].encode('cp1251') + '</div>')
                f.write('<h5>' + article['author'] + '</h5>')


def search(text):

    return [a for a in list if text in a['name']]



articles = [{'name':'using NSString', 'author':'Medin F.', 'text':'If you don''t need NSString''s methods like -(CGFloat)floatValue use "char *" with simple code : "char * myString = nsstringObject.UTF8string;" !!!'},
            {'name':'NSArray class overview', 'author':'Apple inc.', 'text':'rihdlgfilughsjrrufyetagsufodhgydftgsoadfyuargfeaorilgyhslrigugruyotsgerht;sogrihhgsr1488'}]


import json

json.dump(articles, open('articles.json', 'w'))



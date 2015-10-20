EMAILS = [{'from': 'bmstu.py@gmail.com', 'title': 'Notes', 'important': False},
          {'from': 'bmstu.py@gmail.com', 'title': 'Spam', 'important':False},
          {'from': 'bmstu.py@gmail.com', 'title': 'Hello', 'important':True},
          {'from': 'postmaster@gmail.com', 'title': 'Some', 'important':False},
          {'from': 'postmaster@gmail.com', 'title': 'Welcome', 'important':False}]

important_labels = {True:'[!] ', False:'[ ] '}


def print_emails(emails):
    print
    froms = [a['from'] for a in emails]
    for _from in set(froms):
    
        print '->', _from
        for email in emails:
            if email['from'] == _from:
                print important_labels[email['important']] + email['title']
    print

if __name__ == '__main__':
    print_emails(EMAILS)


          

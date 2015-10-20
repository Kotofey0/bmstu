MESSAGES = [{'from': 'Bob', 'text': 'Hi!', 'timestamp': '2015-10-10T12:59:32'},
            {'from': 'Max', 'text': 'Hello!', 'timestamp':'2015-10-10T03:45:20'},
            {'from': 'Max', 'text': 'How are u?', 'timestamp':'2015-10-10T13:00:32'},
            {'from': 'Bob', 'text': 'no...', 'timestamp':'2015-10-10T13:25:57'},
            {'from': 'Bob', 'text': 'but i can bring it to her', 'timestamp':'2015-10-10T13:26:04'},
            {'from': 'Alice', 'text': 'Hey!!', 'timestamp':'2015-10-10T21:20:45'},
            {'from': 'Bob', 'text': 'OK)', 'timestamp':'2015-10-10T03:59:32'},
            {'from': 'Alice', 'text': 'where is my phone??', 'timestamp':'2015-10-10T21:20:59'}]


def compare_message_by_date(message):
    return message['timestamp']


if __name__ == '__main__':

    sorted_messages = sorted(MESSAGES, key = compare_message_by_date)
    
    from_string = raw_input('Name -> ')
    if from_string not in [mess['from'] for mess in MESSAGES]:
        print 'No messages ...'
        exit()
    for string in ['[' + mess['timestamp'][10:] + ']' + mess['text'] for mess in sorted_messages if mess['from'] == from_string]:
        print string






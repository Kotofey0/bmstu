audios = [
    {'title':'Second song', 'band':'Second band' }, 
    {'title':'Fist song', 'band':'First band'}, 
    {'title':'Second song', 'band':'First band'}, 
    {'title':'First song','band':'Second band'} 
]


def print_audio(audios):
    for counter, audio in enumerate(audios):
        
        print str(counter + 1) + '. ' + audio['title'] + ' - ' + audio['band']
        

def count_artists(audios):
    dict = {}
    bands = []

    for audio in audios:
        if audio['band'] not in bands: 
            bands.append(audio['band'])

    for audio in audios:
        if audio['band'] not in dict: 
            dict[audio['band']] = 1
        else: 
            dict[audio['band']] += 1

    return dict

def test_count_artists():
    test_arg = []
    from random import randint
    ii, jj = randint(1,10), randint(1, 10)
    for i in range(ii):
        for j in range(jj):
            test_arg.append({'title':str(i) + 'song', 'band':str(j) + 'band'})

    bands = []
    dict = {}
    for audio in test_arg:
        if audio['band'] not in bands:
            bands.append(audio['band'])

    for audio in test_arg:
        if audio['band'] not in dict:
            dict[audio['band']] = 1
        else:
            dict[audio['band']] += 1
    return (dict == count_artists(test_arg))
	
print audios






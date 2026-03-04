acronyms = {'LOL' : 'laugh out loud',
            'IDK' : 'I dont know',
            'SMH' : 'shake my head'}

print(acronyms['LOL'])

anime = {}

anime['Eren Yeager'] = 'Attack On Titan'
anime['Gon Freese'] = 'HunterXHunter'
anime['Moa Moa'] = 'Apothocary Diaries'

print(anime)

sentence = 'IDK' + ' what happened the last episode of '+ 'Eren Yeager'
translation = acronyms.get('IDK') + ' what happened on ' + anime.get('Eren Yeager')

print(sentence)
print(translation)
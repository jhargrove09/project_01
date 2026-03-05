current_movies = {'Demon Slayer' : '11:00am',
                  'Jujuitsu Kaisen' : '1:00pm',
                  'My Hero Academia' : '3:00pm',
                  'Ponyo' : '5:00pm'}

print('We are currently playing the following movies:')
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print('Movie unavailable')
else:
    print(movie, 'is playing at', showtime)
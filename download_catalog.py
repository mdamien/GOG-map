import requests, json

games = []

for i in range(1, 80):
	print('page', i)
	resp = requests.get('https://www.gog.com/games/ajax/filtered?mediaType=game&page=%d&sort=popularity' % i)
	games += resp.json()['products']
	print('games', len(games))

open('games.json', 'w').write(json.dumps(games, indent=2))
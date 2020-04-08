import requests, json, os.path

for game in json.load(open('games.json')):
	print(game['slug'])

	filepath = 'reviews/' + game['slug'] + '.json'
	if os.path.exists(filepath):
		print('already done')
		continue

	url = "https://reviews.gog.com/v1/products/%s/reviews?language=in:en-US,fr-FR&limit=200&order=desc:votes"
	url = url % game['id']

	resp = requests.get(url)

	reviews = resp.json()['_embedded']['items']
	print('reviews', len(reviews))

	open(filepath, 'w').write(json.dumps(reviews, indent=2))
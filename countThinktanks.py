import json

print('Loading JSON file...')
with open('saevInMedia.json') as f:
	articles = json.load(f)
print('Done.')

thinktanks = []
with open('thinktanks.tsv') as f:
	lines = f.readlines()
for l in lines:
	variations = [s.strip() for s in l.split('\t')]
	thinktanks.append(variations)

thinktankCount = {}
tot = len(articles)
i = 0
for a in articles:
	i += 1
	if i % 100 == 0:
		print('%i / %i' % (i, tot))
	for t in thinktanks:
		match = False
		for variant in t:
			if variant.lower() in str(a['Article text']).lower():
				match = True
				break
		if match:
			if t[0] in thinktankCount.keys():
				thinktankCount[t[0]] += 1
			else:
				thinktankCount[t[0]] = 1

print('\n\nRESULT:\n')
for t in thinktankCount.keys():
	print('%s: %i' % (t, thinktankCount[t]))
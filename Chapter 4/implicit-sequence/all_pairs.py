def all_pairs(s):
	for item1 in s:
		for item2 in s:
			yield (item1, item2)

list(all_pairs([1, 2, 3]))
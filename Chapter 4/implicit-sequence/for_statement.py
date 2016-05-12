counts = [1, 2, 3]


"""for statement"""
for item in counts:
	print(item)

"""while statement analogy"""

items = counts.__iter__()
try:
	while True:
		item = items.__next__()
		print(item)
except StopIteration:
	pass

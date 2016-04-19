def count(s, value):
	"""Count the number of the occurrence of value in sequence s."""
	total = 0
	for elem in s:
		if elem == value:
			total = total + 1
	return total

digits = [1, 8, 2, 8]
print(count(digits, 8))
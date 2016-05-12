def letters_generator():
	current = 'a'
	while current <= 'd':
		yield current # yield statement indiates generator function
		current = chr(ord(current)+1)

for letter in letters_generator():
	print(letter)

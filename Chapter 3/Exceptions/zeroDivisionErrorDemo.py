try:
	x = 1/0
except ZeroDivisionError as e:
	print('handling a', type(e))
	x = 0
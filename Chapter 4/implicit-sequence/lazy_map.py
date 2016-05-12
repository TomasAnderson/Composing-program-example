def double_and_print(x):
	print('***', x, '=>', 2*x, '***')
	return 2*x
s = range(3, 7)
doubled = map(double_and_print, s)
next(doubled)
next(doubled)
next(doubled)
next(doubled)
# next(doubled)

"""
The filter, zip and reversed 
functions also return iterators
"""

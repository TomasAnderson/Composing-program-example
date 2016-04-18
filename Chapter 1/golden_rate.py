def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess

"""
golden rate can be computed by
repeatedly summing the inverse of any positive number with 1
and it is one less than its square
"""

def golden_update(guess):
	return 1/guess + 1

def square_close_to_successor(guess):
	return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
	return abs(x - y) < tolerance

golden_rate = improve(golden_update, square_close_to_successor)

apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

from functools import reduce
from operator import mul
def product(s):
	return reduce(mul, s)

result = product([1, 2, 3, 4, 5])
print(result)

""" it is more common to use list comprehensions direclt rather that 
higher-order functions, but both approaches to sequence processing are widly used"""


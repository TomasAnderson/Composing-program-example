def apply_to_all(map_fn, s):
	return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
	return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
	reduced = initial
	for x in s:
		reduced = reduce_fn(reduced, x)
	return reduced

def mul(x, y):
	return x * y 

# print(reduce(mul, [2, 4, 8], 1))

def divisors_of(n):
	divides_n = lambda x: n % x == 0
	return [1] + keep_if(divides_n, range(2, n))

# print(divisors_of(12))

from operator import add

def sum_of_divisors(n):
	return reduce(add, divisors_of(n), 0)

# print(sum_of_divisors(12))

def perfect(n):
	return sum_of_divisors(n) == n

print(keep_if(perfect, range(1, 1000)))

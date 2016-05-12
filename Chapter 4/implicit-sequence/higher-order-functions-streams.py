from stream import Stream
from integer_stream import integer_stream

def map_stream(fn, s):
	if s is Stream.empty:
		return s
	def compute_rest():
		return map_stream(fn, s.rest)
	return Stream(fn(s.first), compute_rest)

def filter_stream(fn, s):
	if s is Stream.empty:
		return s
	def compute_rest():
		return filter_stream(fn, s.rest)
	if fn(s.first):
		return Stream(s.first, compute_rest)
	else:
		return compute_rest() 

def first_k_as_list(s, k):
	first_k = []
	while s is not Stream.empty and k > 0:
		first_k.append(s.first)
		s, k = s.rest, k-1
	return first_k

def primes(pos_stream):
	def not_divible(x):
		return x % pos_stream.first != 0
	def compute_rest():
		return primes(filter_stream(not_divible, pos_stream.rest))
	return Stream(pos_stream.first, compute_rest)

prime_numbers = primes(integer_stream(2))
print(first_k_as_list(prime_numbers, 7))



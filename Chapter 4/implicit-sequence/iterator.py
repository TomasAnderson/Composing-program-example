class LetterIter:
	def __init__(self, start='a', end='e'):
		self.next = start
		self.end = end
	def __next__(self):
		current = self.next
		if current > self.end:
			raise StopIteration
		self.next = chr(ord(self.next)+1)
		return current

class Positives:
	def __init__(self, current=1):
		self.current = current
	def __next__(self):
		current = self.current
		self.current += 1
		return current

class Letters:
	def __init__(self, start='a', end='z'):
		self.next = start
		self.end = end
	def __iter__(self):
		return LetterIter(self.next, self.end)


# letters = Letters('a', 'e')
# letters_iter = letters.__iter__()
# b_to_k = Letters('b', 'k')
# letters_b_to_k = [x.upper() for x in b_to_k]

new_range = map(lambda x: x*2, range(2, 4))
# print(next(new_range))

def letter_generator():
	current = 'a'
	while current <= 'z':
		yield current
		current = chr(ord(current)+1)

# letters = letter_generator()

def all_pairs(s):
	for item1 in s:
		for item2 in s:
			yield(item1, item2)

# one_to_three_pairs = all_pairs([1,2,3])

class LettersWithYield():
	def __init__(self, start='a', end='z'):
		self.next = start
		self.end = end
	def __iter__(self):
		while self.next <= self.end:
			yield self.next
			self.next = chr(ord(self.next)+1)

# list(all_pairs(LettersWithYield()))[:5]

class Stream:
	class Empty:
		def __repr__(self):
			return 'Stream.empty'
	empty = Empty()
	def __init__(self, first, compute_rest:lambda:empty):
		self.first = first
		self._compute_rest = compute_rest
	@property
	def rest(self):
		if self._compute_rest is not None:
			self._rest = self._compute_rest()
			self._compute_rest = None
		return self._rest
	def __repr__(self):
		return 'Stream ({0}, <...>)'.format(repr(self.first))


s = Stream(1, lambda: Stream(2+3, lambda: Stream(9)))
# print(repr(s.rest.first))



def integer_stream(start):
	def compute_next():
		return integer_stream(start + 1)
	return Stream(start, compute_next)


# print(integer_stream(2).first)

def map_stream(fn, s):
	if s is Stream.empty:
		return s
	def compute_next():
		return map_stream(fn, s.rest)
	return Stream(fn(s.first), compute_next)

def filter_stream(fn, s):
	if s is Stream.empty:
		return s
	def compute_next():
		return filter_stream(fn, s.rest)
	if fn(s.first):
		return Stream(s.first, compute_next)
	else:
		return compute_next()


def first_k_as_list(k, s):
	if s is Stream.empty:
		return s
	result = []
	while k >= 0:
		result.append(s.first)
		k, s = k-1, s.rest
	return result

# print(first_k_as_list(5, integer_stream(2)))

def primes(pos_stream):
	def not_divible(x):
		return x % pos_stream.first != 0
	def compute_rest():
		return primes(filter_stream(not_divible, pos_stream.rest))
	return Stream(pos_stream.first, compute_rest)

# prime_numbers = primes(integer_stream(2))
# print(first_k_as_list(5, prime_numbers))

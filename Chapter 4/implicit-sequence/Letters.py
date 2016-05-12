from LetterIterator import *

class Letters:
	def __init__(self, start='a', end='e'):
		self.start = start
		self.end = end
	def __iter__(self):
		return LetterIterator(self.start, self.end)

b_to_k = Letters('b', 'k')
caps = map(lambda x: x.upper(), b_to_k) # map function is lazy
# print(next(caps))
# print(next(caps))
# print(next(caps))


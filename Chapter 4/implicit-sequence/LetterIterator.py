class LetterIterator:
	def __init__(self, start='a', end='e'):
		self.next_letter = start
		self.end = end
	def __next__(self):
		if self.next_letter == self.end:
			raise StopIteration
		letter = self.next_letter
		self.next_letter = chr(ord(letter)+1)
		return letter
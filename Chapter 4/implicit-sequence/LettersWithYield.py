from all_pairs import all_pairs

class LettersWithYield:
	def __init__(self, start='a', end='e'):
		self.start = start
		self.end = end
	def __iter__(self):
		next_letter = self.start
		while next_letter < self.end:
			yield next_letter
			next_letter = chr(ord(next_letter)+1)

letters = LettersWithYield()
list(all_pairs(letters))[:5]
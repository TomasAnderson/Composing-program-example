class Positives:
	def __init__(self):
		self.current_number = 1
	def __next__(self):
		next = self.current_number
		self.current_number += 1
		return next
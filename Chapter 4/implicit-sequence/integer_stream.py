from stream import Stream

def integer_stream(first):
	def compute_rest():
		return integer_stream(first+1)
	return Stream(first, compute_rest)

positives = integer_stream(1)

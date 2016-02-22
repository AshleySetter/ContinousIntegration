def fibonacci(n):
	"""
	Return n-th value of fibonacci sequence
	"""
	if n < 2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)
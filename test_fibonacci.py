def test_fibonacci():
	"""
	In this function we import fibonacci.py
	and test the function inside it against
	known values"""

	import fibonacci as fb
	assert fb.fibonacci(10) == 55
	assert fb.fibonacci(5) == 5
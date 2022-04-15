def false_position(f, a, b, e1, e2, n):

	if abs(f(a)) < e2 or abs(f(b)) < e2:
		return f(a)
	
	k = 1
	m = f(a)

	while(True):
		x = (a * f(b) - b * f(a)) / (f(b) - f(a))

		if abs(f(x)) < e2 or (b - a) < e1 or k > n:
			return x

		if m * f(x) > 0:
			a = x
		else:
			b = x

		k += 1

def bisection(f, a, b, e1, e2, n):

	if abs(f(a)) < e2 or abs(f(b)) < e2:
		return f(a)
	
	k = 1
	m = f(a)

	while(True):
		x = (a + b) / 2

		if abs(f(x)) < e2 or (b - a) < e1 or k > n:
			return x

		if m * f(x) > 0:
			a = x
		else:
			b = x

		k += 1
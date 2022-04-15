def find_valid_range(function, a, b):
	a_tabulated = a
	b_tabulated = a + 0.5

	while((function(a_tabulated) * function(b_tabulated)) > 0):

		if(a_tabulated >= b):
			return None, None
		a_tabulated += 0.5
		b_tabulated += 0.5
	return a_tabulated,b_tabulated
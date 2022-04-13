from numerical_methods import false_position
from functions import find_valid_range

def f1(x):
	return x**3 - 9*x + 3

minimum_value_range = int(input("Digite o valor do início do intervalo: "))
maximum_value_range = int(input("Digite o valor do fim do intervalo: "))
acceptable_approximation = float(input("Digite a aproximação desejável (Ex: 0.00001): "))
maximum_iterations = int(input("Digite a quantidade máxima de iterações: "))

a, b = find_valid_range(f1, minimum_value_range, maximum_value_range)

if a == None:
	print("Não existe raiz nesse intervalo, ou essa função não contínua")
else:
	false_position(f1, a, b, acceptable_approximation, maximum_iterations)
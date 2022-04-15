from numerical_methods import false_position
from functions import find_valid_range

def f1(x):
	return x**2 - x - 2

minimum_value_range = int(input("Digite o valor do início do intervalo: "))
maximum_value_range = int(input("Digite o valor do fim do intervalo: "))
precision1 = float(input("Digite o valor em que os intervalos A e B estarão suficiente próximos (Ex: 0.00001): "))
precision2 = float(input("Digite a aproximação desejável (Ex: 0.00001): "))
maximum_iterations = int(input("Digite a quantidade máxima de iterações: "))

a, b = find_valid_range(f1, minimum_value_range, maximum_value_range)

if a == None:
	print("Não existe raiz nesse intervalo, ou essa função não contínua")
else:
	x = false_position(f1, a, b, precision1, precision2, maximum_iterations)
	print("A raiz aproximada da função é: ", x)
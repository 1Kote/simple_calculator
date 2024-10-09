#Caculadora 

#############
from unittest import result
while True:
    number1 = input("Digite um numero: ")
    number2 = input("Digite outro numero: ")
    operator = input("Digite o operador(+,-,/,*): ")
    
    valid_numbers = None
    num_1_floa = 0
    num_2_float = 0
    
    try:
        num_1_float = float(number1)
        num_2_float = float(number2)
        valid_numbers = True
    except Exception:
        valid_numbers = None

    if valid_numbers is None:
        print("Um ou ambos os numeros digitados são invalidos")
        continue

    valid_operators = '+-/*'

    if operator not in valid_operators:
        print("Operador invalido.")
        continue

    if len(operator) > 1:
        print("Digite apenas um operador.")
        continue

    if operator == "+":
        print(f"{num_1_float} + {num_2_float} =", num_1_float + num_2_float)
    elif operator == "-":
        print(f"{num_1_float} - {num_2_float} =", num_1_float - num_2_float)
    elif operator == "/":
        print(f"{num_1_float} / {num_2_float} =", num_1_float / num_2_float)
    elif operator == "*":
        print(f"{num_1_float} * {num_2_float} =", num_1_float * num_2_float)
    


    exit_calculator = input("Digite 's' para sair: ").lower().startswith('s')

    if exit_calculator is True:
        print("Saindo da calculadora.")
        break
    elif exit_calculator is False:
        print("Continuando a calculadora.")
       
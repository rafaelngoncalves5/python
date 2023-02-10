# Aula 6

# A sintaxe de importação é -> from module import function
# import math   -> Se eu desejasse importar o módulo inteiro (não recomendado)
# from math import *    -> Se eu desejasse importar o módulo inteiro, porém não quero sempre especificar o math.method()
from math import sqrt
import math

# Definindo funções
def my_func():  # Assinatura da função
    print("Esta é uma função! ")    # Especificação -> 'Faça isso!'

my_func()   # Chamando a função

# Usando parâmetros
def my_func2(num1, num2):
    return num1 + num2

result_my_func2 = my_func2(5, 5)    # Argumentando num1 = 5 e num2 = 5
print(result_my_func2)

# Retornando uma função dentro de outra
def nested_func(num1, num2):
    return my_func2(num1, num2)

print(nested_func(10, 10))

# Raiz quadrada
# Em caso de módulo inteiro seria -> math.sqrt(25)
print(sqrt(25))

# Mostrando todo o conteúdo dentro de math
print(dir(math))

# Métodos relevantes

'''
1 - max() -> Retorna o maior número de uma lista de argumentos;
2 - min() -> Retorna o menor número de uma lista de argumentos;
3 - abs() -> Retorna o valor absoluto de um único argumento;
4 - type() -> Retorna o tipo do valor argumentado;
'''
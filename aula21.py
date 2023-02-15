# Aula 21

# Exemplo named tuple
from collections import namedtuple
from functools import reduce

country = namedtuple("country", ["name", "capital", "continent"])

france = country("France", "Paris", "Europe")
japan = country("Japan", "Tokyo", "Asia")
senegal = country("Senegal", "Dakar", "Africa")

countries = (france, japan, senegal)

print(japan.name)
print(france.capital)
print(senegal.continent)

'''
Algumas funções de alta-ordem do Python. Estas funções recebem um iterável e uma função de processamento, retornando outro iterável
    - map()
    - filter() 
    - reduce()
'''

# filter()

nums = (1, 2, 3, 4, 5)

print(tuple(filter(lambda x: x % 2 == 0, nums)))    # Imprime (2, 4)

# map()
print(tuple(map(lambda x: x ** 2, nums)))   # Imprime (1, 4, 9, 16, 25)

# reduce() -> O reduce aceita um iterável e uma função de de dois parâmetros, e não mais de dois (chamada acumulator)
# o reduce() usa o acumulador para 'reduzir' os valores da tupla recursivamente até retornar um único valor
# Podemos usar o reduce para somar todos os valores de uma tupla, por exemplo
print(reduce(lambda x, y: x + y, nums))     # Imprime 15

# Para mapearmos valores filtrados -> map(mapping_function, filter(predicate, iterable))
map_filter = map(lambda x: x ** 2, filter(lambda y: y > 2, nums))   # Primeiro executa o map para elevar todos os valores ao quadrado, depois filtra só os valores maiores que 2, no caso: 3, 4, 5, o que imprime (9, 16, 25)
print(tuple(map_filter))
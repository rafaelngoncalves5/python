# Aula 12

my_dict = {1: 'one', 2: 'two', 3: 'three'}

# O método items() -> Retorna os pares chave/valor em formato de tupla
print(my_dict.items())

# O método keys() -> Retorna as chaves do dicionário
print(my_dict.keys())

# O método values() -> Retorna os valores dos dicionários
print(my_dict.values())

# O conceito de list comprehension é útil para gerarmos uma lista (como fazemos com o range()) com uma lógica específica
# A sintaxe básica de list comprehension é
my_list = [x for x in range(1, 6)]      # Pode ser separada em |x| (que é a regra) depois um loop normal |for x in range(1, 6)|
print(my_list)

# Usando alguma lógica
my_logic_list = [x * 2 for x in range(1, 6) if x % 2 == 0]  # Veja que o if é o terceiro membro
print(my_logic_list)

# Lista de 'C's
my_c_list = ['C' for x in range(1, 6)]
print(my_c_list)

# Fatiando listas -> my_list[start:end:stride]
my_list[1:6:2]      # Imprime [2, 4]

# Omitindo
to_five = ['A', 'B', 'C', 'D', 'E']
 
print(to_five[3:])
# prints ['D', 'E'] 
 
print(to_five[:2])
# prints ['A', 'B']
 
print(to_five[::2])     # ::2 implica em stride
# print ['A', 'C', 'E']

'''
1 - The default starting index is 0.
2 - The default ending index is the end of the list.
3 - The default stride is 1.
'''

# Usando o stride para reverter a lista
backwards = my_list[::-1]

# Functional programming -> Você pode usar funções como variáveis ou valores
sum_lambda = lambda num1, num2: num1 + num2

# É o mesmo que
def sum(num1, num2):
    return num1 + num2

print(sum_lambda(2, 2))
print(sum(2, 2))
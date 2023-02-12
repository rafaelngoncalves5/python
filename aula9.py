# Aula 9

# No Python a função de range é um atalho pra gerar uma lista
print(range(6))

# O range() tem três diferentes versões
'''
1 - range(stop)
2 - range(start, stop)
3 - range(start, stop, step)
'''
# Mesmo que lista = [0, ... , 5]
for i in range(0, 6):
    print(i)


print('\n')

# Mesmo que lista = [0, ... 9] de 2 em 2
for i in range(0, 10, 2):
    print(i)

# Argumento 1 -> Início do índice, argumento 2 -> Até onde vai, argumento 3 -> De quanto em quanto a contagem vai progredir
# Podemos então entender que temos duas formas de iterar em listas
my_list = ['a', 'b', 'c']

# Iterando em elementos através do índice, igual o for do JavaScript e C#
print("Iterando por índice")
for i in range(0, len(my_list)):
    print(my_list[i])

# Iterando em elementos tipo o map(() => ...) do JavaScript
print("Iterando por elementos")
for i in my_list:
    print(i)

# Lista de listas
double_list = [[1, 2, 3], [4, 5, 6]]

# A lógica aqui é -> Itero dentro das listas primeiro, e depois itero com o j dentro dos elementos de CADA LISTA (que são o i)
for i in double_list:
    for j in i:
        print(j)
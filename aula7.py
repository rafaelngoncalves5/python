# Aula 7

# Listas tem sintaxe
numbers = [1, 2, 3, 4, 5]

# Acessando por índice
print(numbers[0] + numbers[4])      # Somando 1 + 5

# Associando
numbers[0] = 0

# O método append() adiciona um valor no final da lista
numbers.append(6)

# Fatiando
print(numbers[0:len(numbers)])

# Omissão dos índices da esquerda e direita implicam em do 0 e do len(list_name) respectivamente
print(numbers[:])

# Insert insere um item x no índice y -> list_name.insert(1, "nome_item")
# numbers.insert(2, "Três")
print(numbers)

# O método index() -> Retorna o índice do item passado como argumento
# print(numbers.index('Três'))
numbers.insert(2, 3)

# Laços de repetição tem sintaxe -> for var in list_name: código a ser executado por var
# Exemplo
for values in numbers:
    print(values * 2)   # Multiplica cada um dos itens da lista por 2
# Idêntico o map((values) => ...) ou foreach((values) => ...)

# O método sort() -> Retorna à lista em ordem alfabética
numbers.sort()

# Dicionários
d = {'num1': 2, 'num2': 5, 'num3': 8}

print(d)

# Pega o valor do item com chave igual 'num1'
print(d['num1'])

# Adicionando valores a um dicionário
d["num4"] = 10

# Itens de um dicionário podem ser removidos com a palavra-chave del
del d["num1"]

# Listas em dicionários
d["numbers"] = [1, 2, 3]
# Puxando um item da lista dentro do dicionário
num_2 = d["numbers"][1]
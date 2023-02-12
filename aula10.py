# Aula 10

# Usando o Random
from random import randint

print(randint(0, 5))    # Printa um número aleatório entre 0 e 5

# Laços de repetição while tem sintaxe -> while condicao: // faça isso
# Exemplo
cont = 0
cont2 = 0
while cont <= 10:
    print(cont)
    cont += 1
    break   # Forma alternativa de finalizar o laço. Significa "Sair do laço"

print("---")

# While/Else
# Obs: Se o laço finalizar com o break, o else não será executado
while cont2 <= 10:
    print(cont2)
    cont2 += 1
    if cont2 == 5:
        print("I love 5! ")

# \ interpreta duas linhas como uma. , interpreta os prints como inline

# Comparando cadeia de caracteres
phrase = "A bird in the hand..."

# Exemplo
for char in phrase:
  if char in "aA":
    print('X'),
  else:
    print(char),

# Laços de repetição em dicionário
my_dict = {'a': 'item a', 'b': 'item b', 'c': 'item c'}
# Exemplo iterando dentro das chaves (k) e dos valores my_dict[k]
for k in my_dict:
   print("%s - %s" %(k, my_dict[k]))

# Caso precise iterar sabendo os índices dos elementos pode usar o enumerate
# Exemplo usando enumerate
for index, item in enumerate(my_dict):
   print("%s - %s" %(index, item))

print('---')

# Para iterar em duas listas podemos usar o zip. O zip -> O zip cria pares de elmentos e para de iterar no tamanho da lista mais curta
# Exemplo
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]


for a, b in zip(list_a, list_b):
   print("%s - %s" %(a, b))

# Exemplo elegante de For/Else
my_string = "ola mundo!"

for i in range(1, len(my_string)):
  print(i)
  if i:
    pass
else:
  print("Fim")
# Aula 8

# Você pode usar o for loop assim
for value in [1, 2, 3, 4, 5]:
    print(value)

# Você pode usar o for loop para iterar em chaves em dicionários
my_dict = {"Chave 1": 1}

for k in my_dict:
    # Isso aqui printa cada um dos elementos par chave/valor
    print(my_dict)
    # Isso aqui printa apenas os valores buscados através da chave 'k' que itera em todas as chaves
    print(my_dict[k])

# Obs -> Se você tiver listas com chaves iguais, você pode iterar nas duas através de um mesmo loop
# Obs -> Itera com my_dict[i] no caso de dicionário e i apenas em caso de lista

# Iterando com o range
lst = ["a", "b", "c"]

for i in range(0, len(lst)):
    print(lst[i])

for j in lst:
    print(lst)
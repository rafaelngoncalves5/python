# Aula 14
my_list = ["1, 2, 3, 4, 5, 6, 7, 8"]

# Diz ao Python para abrir o test.txt em 'w' write mode
f = open("test.txt", "w")

r = open("test.txt", "r")  # 'r' diz ao Python para entrar em read mode. 'r+' diz ao Python para entrar e read e write mode

# Escrevendo
for i in my_list:
    f.write(i + "\n")

# ou
for i in range(0, 5):
    f.write("Esta e a linha %s \n" %(i))

# Lendo
print(r.read())

# Ou você pode ler linha por linha
print(r.readline())
print(r.readline())
print(r.readline())

# Sempre lembre-se de fechar o filestream no final
f.close()

# Usando o __exit__(), tem sintaxe com with e as
# with open("file", "mode") as variable:

# Exemplo
with open("av.txt", "r") as av:
    print(av.read())

# Checando se o arquivo está fechdo
print(f.closed)
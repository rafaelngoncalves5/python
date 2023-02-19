# Aula 2

# Caracteres de escape
# Arrumando 'There's a snake in my boot!'
print('There\'s a snake in my boot!')

# Acessando string por índica
python = 'python'
print(python[0])
print(python[1])
print(python[2])
print(python[3])
print(python[4])
print(python[5])

# Métodos de string relevantes
'''
1 - len() -> Recebe o tamanho da string
2 - lower() -> Transforma à string em minúsculo
3 - upper() -> Transforma à string em maiúsculo
4 - str() -> Converte em string
'''
# Obs: métodos que usam . apenas funcionam com string, já os outros, funcionam com demais tipos

# Concatenando string com variáveis usando %
month = 10
day = 2
print("02 - %s - 2023" %(month))    # O %s concatena uma string, que é posteriormente passada com %(var)
# ou
print("02 - %03d - 2023" %(month))  # Usa o "pad with zeros" para concatenar a variável com três casas em um inteiro
# ou com múltiplas palavras
print("%02d - %s - 2023" %(day, month))
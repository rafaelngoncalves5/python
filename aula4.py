# Aula 4

# Controle de fluxo -> Nos permite controlar o fluxo do nosso programa baseado no que está acontecendo no nosso programa

# Operadores de comparação

# Igualdade ==
# Desigualdade !=
# Menor <
# Menor ou Igual <=
# Maior >
# Maior ou Igual >=

# Operadores Booleanos

# AND -> Verifica se ambas as declarações são verdadeiras
# OR -> Verifica se ALGUMA das declarações são verdadeiras
# NOT -> Entrega o oposto da declaração

# A ordem de avaliação dos operadores booleanos é -> NOT, AND, OR
# Podemos usar parênteses para avaliar primeiro a expressão desejada

# Condicionais
# IF tem a seguinte sintaxe
if 4 > 2:   # Expressão para ser avaliada
    print(True)   # Execute isso aqui caso a expressão seja verdadeira

# If/Else tem a seguinte sintaxe
if 4 != 4:
    print(True)     # Se 4 não for igual a 4 faça isso
else:
    print(False)    # Ou faça isso caso contrário

# If/Elif/Else tem a seguinte sintaxe
if 4 != 4:
    print(True)     # Se 4 não for igual a 4 faça isso
elif 4 == 4:
    print(True)
else:
    print(False)    # Ou faça isso caso nenhum dos dois
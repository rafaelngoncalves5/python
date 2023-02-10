'''
Python é uma linguagem de uso de geral, de tipagem dinâmica e forte e que 
possui coletor de lixo.
Python foi criada por Guido van Rossum e lançada em 20 de fevereiro de 1991.

'''
# Aula 1

# Estou usando -> Python 3.10 e as extensões do Python VSCode;

# O print do Python 3 tem parênteses

# Imprimindo
print("ola mundo!")

# Strings podem ter '' ou "", mas devem ser concatenadas de forma equivalente
# EOL -> End Of Line

# Concatenando
print("ola mundo!" + " bom dia!")

# Variáveis
todays_date = '10/02/2023'

# Operações aritméticas no Python seguem o princípio da ordem de operações
# O operador de módulo (%) retorna o resto de uma divisão
odd_number = 15 % 2     # Retorna 1

# Exemplo de multiplicação
product = 2 * 2

# Exemplo de potenciação
power = 2 ** 2      # Mesmo que 2²

# Divisão
remainder = 1398 % 11

# Operadores de incremento e decremento
fish_pond = 30
# Peguei 12 peixes!
fish_pond += 12     # Mesmo que -> fish_pond = fish_pond + 12
# Perdi alguns peixes!
fish_pond -= 6      # Mesmo que -> fish_pond = fish_pond - 12

# Tipos de variáveis
# Inteiro
int1 = 12
# Decimal
float1 = 5.6
# Você pode definir um número de ponto flutuante ou inteiro usando notação científica
float2 = 5.1e2  # E indica elevado a dez, ou seja: 5.1e2 -> Mesmo que 5.1 elevado a 10

# Para operar resultados float sem arrendodar para baixo: Segue os exemplos
quotient1 = 5.1/5
quotient2 = 5/4.9
quotient3 = 10./5.
# Ou em caso de inteiros inexatos
quotient4 = float(7)/2

# Strings de múltiplas linhas
mult_line_string = """ 
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad 
minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum. 
"""

# Booleanos
verdadeiro = True
falso = False

# Convertendo
item = 12
# String
print(str(item))
# Float
print(float(item))
# Integer
print(int(item))
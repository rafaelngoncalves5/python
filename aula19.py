# Aula 19

'''
Generators nos permite criar iterators sem o uso do .__iter__() e do .__next__(), temos dois tipos de generators
    1 - Generator Functions
        -> São similares a funções normais, no entarnto retornamos no final um generator com o yield
    2 - Generator Expressions

Generators não ocupam espaço na memória, o que significa que podem trabalhar com estruturas infinitas de forma performática
'''

# Generator Functions

# Exemplo de generator function
def items_func():
    # Obs: Diferenças yield e return -> No yield o que vem depois é executado e são preservadas as variáveis pós retorno, no return não
    yield "Item 1"
    yield "Item 2"
    yield "Item 3"

items = items_func()

for item in items:
    print(item)     # Retorna -> Item 1 Item 2 Item 3


# Generator Expressions são uma forma mais limpa e inline de criarmos um generator. Tem sintaxe similar as list comprehension

# List comprehension
my_list = [i for i in range(0, 10)]

# Generator expression
my_gen_exp = (i for i in range(0, 10))

# Alguns métodos relevantes de iterators são -> send(), throw() e close()

# Podemos combinatar iterators com o método chain()
# Aula 18

import itertools

'''
Os componentes que abrangem o processo de loop são
    - iter() -> Função que cria um objeto de iteração, do seu iterável
    - next() -> Função que captura cada valor individual durante o processo de iteração
    - StopIteration() -> Exceção que força o loop a parar quando não há mais elementos
'''
my_list = ["Item 1", "Item 2", "Item 3"]

# 1 - O for chama o iter() para criar um objeto de iteração do iterável (no caso a lista my_list)
# Usando o iter() função global
print(iter(my_list))    # Imprime -> <list_iterator object at 0x000001FE7463A560>

# ou usando o dunder method .__iter__()
print(my_list.__iter__())   # Imprime -> <list_iterator object at 0x000001FE7463A560>

# Obs a função global 'iter()' usa o dunder method .__iter__(), mesma coisa com 'next()' e .__next__()

# 2 - O next() pega o próximo valor do iterável em sequência
iterable_my_list = iter(my_list)
print(iterable_my_list.__next__())  # Imprime Item 1
print(next(iterable_my_list))   # Imprime Item 2 e assim em diante...

print("---")

my_list2 = my_list
iterable_my_list2 = iter(my_list2)

for i in range(len(my_list2)):
    print(next(iterable_my_list2))  # Imprime -> Item 1 Item 2 Item 3

# 3 - O next() para de executar assim que for gerada a excessão 'StopIteration', que ocorre toda vez que não há mais itens no nosso iterável
# Se chamarmos o next() fora do range do iterável, receberemos exatamente essa excessão

# print(next(iterable_my_list2)) Imprime -> O traceback da excessão com o raise StopIteration()

'''
Sumarizando, o iterator protocol 

1 - The for loop will first retrieve an iterator object for the dog_foods dictionary using iter().

2 - Then, next() is called on each iteration of the for loop to retrieve the next value. This value is set to the for loop’s variable, food_brand.

3 - On each for loop iteration, the print statement is executed, until finally, the for loop executes a call to next() that raises the StopIteration exception. The for loop then exits and is finished iterating.
'''

'''
Custom Iterators devem ter um método .__iter__() e um método .__next__()

    - O método iter() deve retornar o objeto de iteração, no caso self, deve também conter um membro de classe inicializado
    - O método next() deve retornar o próximo valor ou elevar a excessão StopIteration
'''

# Exemplo de custom iteration
class CustomerCounter:
  # Checkpoint 1
  def __iter__(self): 
    self.count = 0
    return self
  # Checkpoint 2
  def __next__(self):
    self.count +=1 
    # Checkpoint 4 & 5
    if self.count > 100:
      raise StopIteration
    return self.count

# Checkpoint 3
customer_counter = CustomerCounter()

# Checkpoint 6
for customer_count in customer_counter:
  print(customer_count)

# O Python tem uma forma de manipular iteradores chamada itertools

'''
O itertools possui três categorias

    - Infinite -> Iteram infinitamente, sem o StopIteration. Exige alguma condição para parar
        - count(), cycle(), repeat()
    - Input-Dependent -> Vai terminar o loop baseado no menor número passado como parâmetro
        - chain(), compress(), filterfalse()
    - Combinatoric -> São combinatórios, onde funções matemáticas acontecem no iterável
        - product(), permutation(), combination()
'''

# Infinite iterators

# count() -> Conta até determinarmos condicionalmente seu fim, tem sintaxe count(start, [step])

# Exemplo count()
for i in itertools.count(start=0, step=1):
    print(i)
    # Printa infinitamente começando de 0, de 1 em 1 até chegar em 10
    if i >= 10:     # Stop condition
       break

# Input-Dependent iterators

# chain() -> Recebe um ou mais iterators e os combina em apenas um

# Exemplo chain()
my_list3 = [1, 2, 3]
my_list4 = [4, 5, 6]
my_tuple = [7, 8, 9]
my_dict = {"Ten": 10}

all_ds = itertools.chain(my_list3, my_list4, my_tuple, my_dict)

for i in all_ds:
   print(i)

# Combinatoric iterators

# combinations() -> Recebe uma tupla e a quantidade de combinações por tupla e retorna as combinações possíveis dos itens no conjunto com tamanho = do arg2

# Exemplo combinations()
even = [2, 4, 6]

# Obs: Sempre transforme em lista antes ao usar o combinations
even_combinations = list(itertools.combinations(even, 2))

print(even_combinations)
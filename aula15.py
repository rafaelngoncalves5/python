# Aula 15

'''
Os 4 pilares de POO são:

1 - Herança
2 - Polimorfismo
3 - Abstração
4 - Encapsulamento
'''

# Format simplificado Pytho 3
var = 'ola'
var2 = 'mundo!'
print("var = {}, var2 = {}".format(var, var2))

# Usando u super de novo
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def get_animal(self):
        return self.name + ' says ' + self.sound
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Bark!")   # Você pode inicializar o construtor da classe pai com valores da classe filha ou personalizados. Caso não seja passado, o construtor padrão da classe pai será inicializado
    
dog = Dog("Chulix")
print(dog.get_animal())

class Cat(Animal):
    pass


# Herança múltipla
class DogCat(Dog, Cat):     # Se Cat tivesse get_animal assim como Dog, o primeiro a ser executado seria o do primeiro parâmetro
    pass

# O Dunder method __add__() serve para especificar o que ocorre como somamos nossas instâncias
# Um exemplo de polimorfismo Ad hoc é o operador +, que trabalha de forma diferente dependendo do tipo de dado que está sendo usado

# Exemplo de polimorfismo com overloa
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    # Usando overload para alterar o comportamento do len nas minhas instâncias
    return len(self.attendees)
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

# Encapsulamento

# Python não possui modificadores de acesso internos, usamos a conveniência _ antes da prop, para identificá-la como protegida/privada
# _ implica em um aviso (use com cuidado) e __ é o name mangling, que é útil para previnir name clashing em subclasses

# O raise, fuciona igual o throw error -> raise TypeError, por exemplo
# Interessante usar ABC -> Abstract Base Class em projetos mais complexos
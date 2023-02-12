# Aula 13

# A sintaxe básica de classes é essa
class Animal:
    pass

# Init serve para inicializar os objetos que a classe cria
class Animal(object):
    def __init__(self):     # A convenção self, serve para referenciar o objeto que está sendo criado
        pass

# Atributos
class Animal(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Trabalhando com métodos
    def description(self):   # Sempre passe o self nos métodos
        print("%s " %(self.name))
        print(str(self.age) + " anos")
    
    def test_with_child(self, age):
        print("Sou um método da classe pai! ")
        print("Idade -> ", self.age)

# Instanciando
dog = Animal("Pedrinho", 12)    # Alterando o atributo da instância usando o método construtor
print(dog.name)

dog.description()

# Herança
# A sintaxe de herança pode ser -> class Child(Parent): ...
class Bear(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

b = Bear("B", 25)
# Usando método da classa pai na class filha. Obs: Poderia dar override no description tbm
b.description()

# Exemplo usando o super()
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def call_parent(self):
        return(super(Dog, self).test_with_child(self.age))
    
dg = Dog("PP", 90)
dg.call_parent()
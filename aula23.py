# Aula 23

# Trabalhando com *args -> Usamos o * quando não sabemos quantos argumentos receberemos
def say_string(*args):
    print(args)

say_string("String 1", "String 2")

# Usamos o **kwargs para obrigarmos o usuário a nomear seus argumento antes
def unkwnown_dict(**kwargs):
    for k, v in kwargs.items():
        print("{0}: {1}".format(k, v))

my_dict = {1: "Item 1", 2: "Item 2", 3: "Item 3"}
unkwnown_dict(dicio = my_dict)  # O usuário é obrigado a dar nome ao argumento. Printa -> dicio: {1: 'Item 1', 2: 'Item 2', 3: 'Item 3'}

# Decoradores
# Os decoradores são uma forma de açúcar sintático, são funções que recebem como parâmetro uma outra função, e retornam uma função
def func_decorator(func):
    print("Chamando o decorador toda execução! ")
    
    def wrapper_func(*args, **kwargs):
        # Retorna a função func com os atributos da wrapper
        return func(*args, **kwargs)

    return func

# Agora toda vez que eu chamar o @func_decorator(func), ele vai executar uma função envelopada com nome = func
@func_decorator
def sum(num1, num2):
    return num1 + num2

print(sum(5, 5))

@func_decorator
def sub(num1, num2):
    return num1 - num2

print(sub(10, 5))

# Todas as funções são nomeadas func e chamadas pelo decorator
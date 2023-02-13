# Aula 16

'''
Temos dois tipos de erros em Python -> Syntax Errors e Exception

    - Syntax Errors -> Ocorrem durante o estágio de parsing do Python, antes da execução do programa;
    - Exceptions -> Ocorrem durante a fase de execução (runtime error), apenas quando o código defeituoso
    é acessado. NameError, por exemplo;

O Python utiliza o Traceback para nos informar sobre erros de excessão. O traceback é um sumário
que contém -> Uma mensagem de erro, uma série de funções que precedem à excessão, seguido de 
nomes de arquivo e linhas numéricas;
'''

# Todas as excessões são direta ou indiretamente herdadas da class BaseException 

# Examinando a classe base com o __bases__
print(NameError.__base__)   # Printa <class 'Exception'>
print(Exception.__base__)   # Printa <class 'BaseException'>

# Podemos usar o raise com construtor personalizado ou usar o base
# raise NameError
# Usando mensagem personalizada
# raise NameError("Erro personalizado!")

# Podemos usar uma excessão genérica também, com mensagem de erro personalizada
# raise Exception("Erro personalizado!")

# O fluxo de execução do try/except pode ser ilustrado da seguinte forma
'''
                                                        Yes -> Execute Except Clause -> End
Start -> Execute Try Clause -> Exception Encountered? ->                                                               Finally -> Executed regardless of which of both situations is happening
                                                        No  -> Execute Else Clause (if existent) -> End
Note que o End aqui implica que como a excessão foi lidade, o fluxo do programa continua normalmente, mesmo com o erro.                                                        
'''

# Podemos usar o except para lidar com erros específicos também
try:
    print(True)
except SyntaxError as errorObject:     # Except só é chamado em caso de erro de sintaxe. Usamos um alias como um objeto que armazena o erro
    print("Erro de sintaxe")
    print(errorObject)

# Podemos lidar com múltplas excessões numa única linha -> except SyntaxError, NameError: ...

# Excessões definidas pelo usuário
class CustomException(Exception):
    def CustomExceptionMsg(self, num):
        if num != 2:
            raise CustomException("Custom error 555")
        else:
            print("Tudo Ok!")

cs = CustomException()
cs.CustomExceptionMsg(3)    # Imprime __main__.CustomException: Custom error 555


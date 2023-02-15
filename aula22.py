# Aula 22

from time import sleep
from ansicolors import AnsiColors
import threading

'''
A sintaxe básica de uma thread no Python é

import threading

example_thread = Thread(target_some_func, args=(some_args))

target_some_func -> É a função que você deseja executar com a thread
args -> Argumento(s) que você deseja passar na função targer, por padrão é uma tupla com valor None

Exemplo

t = Thread(target = analyze_list(), args=(l1, l2, l3))

Depois de instanciarmos a Thread com os construtores corretos, devemos usar o método 'start()' para iniciar a Thread
t.start()
'''

# Usando múltiplas threads
def lavar_roupas(s):
    frase = AnsiColors.fg_bright_cyan + "Lavando roupas... " 
    print(frase)
    sleep(2)
    print(frase)
    sleep(2)
    print("Terminei de lavar roupas! ")

def cozinhando(s):
    frase = print(AnsiColors.fg_bright_green + "Cozinhando... ")
    print(frase)
    sleep(4)
    print(frase)
    sleep(4)
    print(AnsiColors.fg_bright_green + "Terminei de cozinhar! ")
    AnsiColors.reset_terminal()

lavar_roupas_thread = threading.Thread(target=lavar_roupas)
conzinhando_thread = threading.Thread(target=cozinhando)

lavar_roupas_thread.start()
conzinhando_thread.start()

print('\n --- \n')

# usamos o .join() como await no threading -> cozinhando.join()

# Temos o asyncio também como alternativa
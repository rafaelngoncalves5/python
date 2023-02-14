# Aula 17

# Podemos automatizar nossos testes com o assert  que tem sintaxe -> assert <condition>, "Message if condition is not met"

import unittest

# Exemplo
def sum(num1, num2):
    result = num1 + num2
    # Exemplo sem nexo só pra testar o assert
    # assert result == 100, "Erro!"

# Testando o assert acima
# sum(5, 5)

# Função de teste unitário
def test_sum():
    # Testando o que acontece se o sum() receber 0, 0 como input, por exemplo
    assert sum(0, 0) == 0, "Erro, o valor retornado deveria ser 0! "
    # Poderíamos adicionar uma multitude de testes abaixo para testar o sum
    # ...

# Testando o test_sum()
# sum(0, 0)

# test_sum()

# Usando o unittest do Python

# Primeiro precisamos herdar o unittest.TestCase
# Obs: Essa classe centraliza todos os nossos testes
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'middle'
  return location

class NearestExitTests(unittest.TestCase):
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
  
  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
  
  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

unittest.main()

''' 
Os métodos de asserção mais comuns do unittest são
    - self.assertEqual(value1, value2) -> Checa se dois valores são iguais. Mesmo que -> assert value2 == value2
    - self.assertIn(value, container) -> Checa se o arg1 está contido dentro do arg2. Mesmo que -> assert value in [value1, value2, value3]
    - self.assertTrue(value) -> Checa se o valor é True. Mesmo que -> assert bool(value) is True
'''
'''
Os métodos de asserção quantitativos são:
    - self.assertLess(valor1, valor2) -> Checa se o valor1 é menor que o valor2
    - self.assertAlmostEqual(value1, value2) -> Faz um teste matemático para checar se são números próximos
'''

'''
Os métodos de asserção de Exceções e Avisos são:
    - self.assertRaises(exceptionType, functionReference, functionArguments...) -> Recebe tipo de excessão no arg1, referencia uma função no arg2, recebe valores arbitrários argumentados na função do arg2, no arg3. Verifica se a chamada da função gera ou não um erro
    - self.assertWarns(specificWarningException, function, functionArguments...) -> Mesma coisa só que com avisos (warnings)
'''

# Você pode usar um mecanismo do unittest chamado 'test parameterization' para diminuir repetição
# Usamos 'subTest context manager' para test parameterization no Python
# self.subTest() tem sintaxe -> class TestClass(unittest.TestCase): ... for num in [0, 1000000, -10]: with self.subTest(num): self.assertTestThis(num, list_to_compare)

# 'Test Fixture' é um mecanismo para garantir uma configuração correta dos testes, bem como garantir 'test teardown'

# Exemplo de Test Fixture

# Testando power_cycle_device()
def power_cycle_device():
  print('Power cycling bluetooth device...')
 
class BluetoothDeviceTests(unittest.TestCase):
  # O setUp() é semanticamente identificado como o PRIMEIRO método a ser executado pelo unittest
  # Poderíamos ter usado o cls no lugar do self, junto do decorator @classmethod para executarmos uma única vez os métodos
  def setUp(self):
    power_cycle_device()
 
  def test_feature_a(self):
    print('Testing Feature A')
 
  def test_feature_b(self):
    print('Testing Feature B')
   # O tearDown() é semanticamente identificado como o ÚLTIMO método a ser executado pelo unittest
   # Poderíamos ter usado o cls no lugar do self, junto do decorator @classmethod para executarmos uma única vez os métodos
  def tearDown(self):
    power_cycle_device()

'''
Podemos pular testes unitário de duas formas no unittest
    - @unittest -> Decorador do unittest
    - skipTest()  -> Método para pular testes
'''
# Exemplo de sintaxe -> Tudo em cima do método de teste: @unittest.skipIf(meth_to_test, "String to return")

# Podemos usar o decorador expectedFailure() para trabalharmos com erros esperados (o teste não é engartilhado como 'falho')
# O expectedFailure() tem sintaxe -> Em cima do método: @unittest.expectedFailure # Método abaixo def always_fail(self):         raise Exception("This test is going to fail")

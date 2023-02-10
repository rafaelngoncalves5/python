# Aula 3

# Importando
from datetime import datetime

# Puxando a data atual
print(datetime.now())

# Printando individualmente ano, mês, dia, etc
# Ano
year = datetime.now().year
# Mês
month = datetime.now().month
# Dia
day = datetime.now().day
print("%02d/%02d/%04d" %(month, day, year))

now = datetime.now()

hour = now.hour
minute = now.minute
second = now.second

print("%s:%s:%s" %(hour, minute, second))


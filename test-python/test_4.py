"""
  4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
"""
#!/usr/bin/python3
from operator import itemgetter
from data import Data

data = Data()
names = data.get_thirds()
result = sorted(names, key=itemgetter("identificationNumber"))
print(result)
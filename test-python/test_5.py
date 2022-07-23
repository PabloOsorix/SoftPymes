"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""
#!/usr/bin/python3
from operator import itemgetter
from data import Data
data = Data()
companies = data.get_companies()
branches = data.get_branches()
thirds =  data.get_thirds()
result = sorted(thirds, key=itemgetter("firstname"))
for i in range(len(companies)):
  companyBranches = companies[i].get("branches")
  for j in range(len(result)):
    if result[i].get("companyId") == companies[i].get(id):
      result[i]["company"] = companies[i].get("name")

print(result)
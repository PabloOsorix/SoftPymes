"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales por su id, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""
#!/usr/bin/python3
from data import Data

def Branches(companies, branches):
  result = []
  for company in range(len(companies)):
    companyBranches = companies[company].get("branches")
    new_company = {}
    new_company["company"] = companies[company].get("name")
    new_company["branches"] = []
    for branch in range(len(branches)):
      if branches[branch].get("id") in companyBranches:
        new_company["branches"].append(branches[branch])
        result.append(new_company)
  return result


data = Data()
companies = data.get_companies()
branches = data.get_branches()

result = Branches(companies, branches)

print(result)
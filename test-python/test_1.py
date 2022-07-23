""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
#!/usr/bin/python3
from data import Data

data = Data()
companies = data.get_companies()
branches = data.get_branches()
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



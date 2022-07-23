"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
#!/usr/bin/python3
from data import Data

data = Data()
names = data.get_thirds()
result = []
for i in range(len(names)):
  new = []
  if names[i].get("tradename") != "":
    information = names[i]["tradename"] + " " + names[i]["lastname"] + " " + names[i]["maidenname"]
    new.append(information)
    result.append(new)
  else:
    information = names[i]["firstname"] + " " + names[i]["lastname"] + " " + names[i]["maidenname"]
    new.append(information)
    result.append(new)

result = sorted(result)
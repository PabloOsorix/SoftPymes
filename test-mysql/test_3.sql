# Generar scripts que realicen las siguientes eliminaciones

-------* Eliminar los items de la compañía Con ID #1 *-------
DELETE * FROM items
WHERE items.companyId = 1;

-------* Eliminar los items que tengan el costo menor a 10.000 *-------

DELETE * FROM items WHERE items.cost < 10.000;
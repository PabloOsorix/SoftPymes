# Generar scripts para las siguientes solicitudes

-------* Eliminar los datos de la tabla colors *-------
DELETE * FROM colors;

-------* Agregar un campo llamado Description en la tabla items, que permita ser NULL, y que tenga un máximo de 200 caracteres *-------

ALTER TABLE items
ADD [COLUMN] description VARCHAR(200) AFTER cost;

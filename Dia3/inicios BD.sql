-- esto es un comentario
-- SQL es un lenguaje de sentencias estructurado en el cual mendiante
-- unas sentencias podemos extraer,agregar, aliminar, actualizar infor, BD
# es es otro comentario

create database pruebas;

# use es para usar la base de datos creada
use pruebas;


create table alumnos(
 # aca ahora vendra todas las columnas de esa tabla alumnos
 nombre varchar(40),
 apellido varchar(25),
 sexo varchar(10),
 numer_emergencia int,
 religion varchar(10),
 fecha_nacimiento date
);
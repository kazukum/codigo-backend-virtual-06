
create database if not exists empresa;
use empresa;

-- crear una base de datos para la gestion de los empleados de una empresa, en la 
-- cual esta distribuida por departamentos (informatica, publicdidad, mkt, creditos)
-- ademas se requiere controlar al personal(nombre, apellido, identificador, pertenece
-- a un dpto), ademas un empleado tiene varios subordinados, cada dpto tiene su nombre,
-- su nivel(en que piso de la empresa se encuentra)

create table if not exists departamentos(

 id int  not null unique auto_increment primary key,
 nombre varchar(40),
 piso varchar(25)
 
);

create table if not exists personal(

 id int primary key not null unique auto_increment,
 nombre varchar(40),
 apellido varchar(40),
 identificador int,
 
 supervisor_id int,
 constraint presonal_personales
 foreign key (supervisor_id ) references personal(id),
 
departamentos_id int,
constraint relacion_personal_departamento
foreign key(departamentos_id) references departamentos(id) 
);


INSERT INTO departamentos (nombre, piso)VALUES 
                         ('Ventas',1),
                            ('Administracion',2),
                            ('Finanzas',2),
                            ('Marketing',3);


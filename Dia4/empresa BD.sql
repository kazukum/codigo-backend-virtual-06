
drop database if exists empresa;
set Sql_safe_updates = 1;
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
 piso int
 
);

create table if not exists personales(

 id int not null unique auto_increment,
 nombre varchar(40),
 apellido varchar(40),
 identificador text,
 departamentos_id int,
 supervisor_id int,
 
 
 
 constraint presonales_personales
 foreign key (supervisor_id ) references personales(id),
 

constraint relacion_personales_departamento
foreign key(departamentos_id) references departamentos(id) 
);


INSERT INTO departamentos (nombre, piso)VALUES 
                         ('Ventas',1),
                            ('Administracion',2),
                            ('Finanzas',2),
                            ('Marketing',3);
                            
select * from departamentos;
select * from personales;



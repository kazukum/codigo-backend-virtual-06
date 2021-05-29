
create database zapateria;

use zapateria;



create table categorias(
id int not null unique auto_increment,
nombre varchar (40),
abbr varchar(20),
imagen text

);


create table productos(
id int not null unique auto_increment,
nombre varchar (40),
precio decimal(5,2), # para guardar precios hasta 999.00
disponible boolean, # un boolean es un tinyint cual 1 = true y 0 = False

# constraint sirve para modificar el nombre en el cual se creara la relacion
# la tabla categoria y la tabla producto, el valor es defecto es:
# cateorias_prodructos_..... 

categoria_id int,
constraint relacion_producto_categoria
foreign key(categoria_id) references categorias(id) 

);

INSERT INTO categorias (nombre, abbr, imagen) VALUE
                        ("ZAPATO","ZAP", "url1"),
                        ("ZAPATILLA","ZAPT","url2"),
                        ("BOTIN","BOT","url3"),
                        ("BOTA","BOTA","url4");
 
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES
					  ("ZAPATO VERANO", 99.90, true, 1),
                      ("ZAPATO HOMBRE", 120.00, true, 1),
                      ("ZAPATO MUJER", 199.00, false, 1),
                      ("ZAPATILLA TREKKIN HOMBRE", 189.90, true, 2),
                      ("ZAPATILLA RUN MUJER", 220.00, true, 2),
                      ("ZAPATILLA OFFROAD MUJER", 320.89, true, 2),
                      ("BOTIN TACO 4", 520.00, true, 3),
                      ("BOTA TACO 10", 710, false, 4);
                      
                      
select * from categorias where nombre like "ZAPATO";
select * from categorias where nombre like "ZA%"; #QUE EMPIEZE
select * from categorias where nombre like "%A"; #QUE TERMINE
 
 
 select * from productos where precio < 250 and precio > 100;
 
 select * from productos where disponible;
 
 select * from productos where nombre like "%TACO 4";
 
 select * from productos where nombre like "%HOMBRE";
 
 select * from productos where nombre like "ZAPATILLA%";
 
 select * from productos where precio > 500 and disponible = "false";
 
 select * from productos where nombre like "%ZAPATILLA%" or nombre like "%BOTA%";
 
 
 
 
 
select * from categorias;

select * from  productos;


-- INNER JOIN

iNSERT INTO CATEGORIAS (nombre, abbr, imagen) VALUE
                        ("BEBES","BEB", "url5");
select * from categorias inner join productos on categorias.id = productos.categoria_id;


-- LEFT JOIN

select * from categorias LEFT join productos on categorias.id = productos.categoria_id;


-- RIGHT JOIN

iNSERT INTO PRODUCTOS (nombre, precio, disponible) VALUE
                        ("SANDALIAS BOB TORONJA","19.90", TRUE);
                        
select * from categorias RIGHT join productos on categorias.id = productos.categoria_id;
 


select *
from categorias join productos on categorias.id = productos.categoria_id
where categorias.nombre = "ZAPATO";

-- ALIAS => AS                        
select cat.nombre as nombrecito
from categorias as cat join productos as prod on cat.id = prod.categoria_id
where cat.nombre = "ZAPATO";

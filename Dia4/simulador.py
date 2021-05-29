
from faker import Faker
from faker.providers import internet, misc


fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)


# genera gracias al provide de internet una imagen cuyo ancho y alto sera de 100px
# print(fake.image_url(width=100, height=100))

# genera 500 empleados
# print(fake.unique.first_name())


# genera un apellido aleatorio
# print(fake.last_name())

# print(fake.first_name())

# print(fake.random_int(min=1,max=501))
# print(fake.uuid())


for id in range(1,501):
    nombre = fake.first_name()
    apellido = fake.last_name()
    identificador = fake.uuid4()
    departamento_id= fake.random_int(min=1,max=5)
    if id == 1:
        supervisor_id ="null"
    else:
        # se le pone id porque tiene q ser menor al original id
        supervisor_id = fake.random_int(min=1,max=id)
        # haremos que el numero random pueda ir desde el -10 hasta < id actual, luego si el numero es menor ao igual
        # a 0 entonces el empleado no tendra supervisor (null)
        if supervisor_id <= 0:
            supervisor_id= "null"

    print("insert into personales values({},'{}','{}','{}',{},{});".format(id, nombre,apellido,identificador,departamento_id,supervisor_id))
create DATABASE hitop2;
use hitop2;
create Table clientes(

    id_cliente int AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25),
    apellidos VARCHAR(25),
    email VARCHAR(50),
    edad INT not NULL
    

);

create table planes(
    id_cliente INT,
    PlanBase SET('Basico','Estandar','Premium'),
    PaquetesAdicionales SET('Deporte','Cine','Infantil'),
    Duracion SET('Mensual','Anual'),
    Foreign Key (id_cliente) REFERENCES clientes(id_cliente)
);

INSERT INTO clientes (nombre,apellidos,email,edad) VALUES
("Pepe","Arias",'asd@asd.com',20);

INSERT INTO planes VALUES
(1,'Estandar','Deporte,Cine','Mensual');
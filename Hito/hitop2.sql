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

INSERT INTO clientes (nombre, apellidos, email, edad) VALUES
("Pepe", "Arias", "pepe.arias@example.com", 20),
("Ana", "Gomez", "ana.gomez@example.com", 25),
("Luis", "Martinez", "luis.martinez@example.com", 30),
("Maria", "Lopez", "maria.lopez@example.com", 22),
("Carlos", "Perez", "carlos.perez@example.com", 28),
("Laura", "Garcia", "laura.garcia@example.com", 27),
("Jorge", "Sanchez", "jorge.sanchez@example.com", 35),
("Elena", "Diaz", "elena.diaz@example.com", 24),
("Miguel", "Fernandez", "miguel.fernandez@example.com", 29),
("Sara", "Ruiz", "sara.ruiz@example.com", 26),
("David", "Hernandez", "david.hernandez@example.com", 32),
("Lucia", "Morales", "lucia.morales@example.com", 23),
("Alberto", "Ortega", "alberto.ortega@example.com", 31),
("Cristina", "Ramos", "cristina.ramos@example.com", 21),
("Pablo", "Vazquez", "pablo.vazquez@example.com", 33),
("Marta", "Romero", "marta.romero@example.com", 34),
("Sergio", "Navarro", "sergio.navarro@example.com", 36),
("Patricia", "Molina", "patricia.molina@example.com", 37),
("Juan", "Castro", "juan.castro@example.com", 38),
("Isabel", "Suarez", "isabel.suarez@example.com", 39);

INSERT INTO planes (id_cliente, PlanBase, PaquetesAdicionales, Duracion) VALUES
(1, 'Estandar', 'Deporte,Cine', 'Anual'),
(2, 'Premium', 'Cine,Infantil', 'Anual'),
(3, 'Basico', 'Deporte', 'Anual'),
(4, 'Estandar', 'Infantil', 'Anual'),
(5, 'Premium', 'Deporte,Cine', 'Anual'),
(6, 'Basico', 'Cine', 'Anual'),
(7, 'Estandar', 'Deporte,Infantil', 'Anual'),
(8, 'Premium', 'Cine', 'Anual'),
(9, 'Basico', 'Infantil', 'Mensual'),
(10, 'Estandar', 'Deporte', 'Anual'),
(11, 'Premium', 'Deporte,Cine', 'Anual'),
(12, 'Basico', 'Cine,Infantil', 'Anual'),
(13, 'Estandar', 'Deporte', 'Anual'),
(14, 'Premium', 'Infantil', 'Anual'),
(15, 'Basico', 'Deporte,Cine', 'Anual'),
(16, 'Estandar', 'Cine', 'Anual'),
(17, 'Premium', 'Deporte,Infantil', 'Anual'),
(18, 'Basico', 'Cine', 'Anual'),
(19, 'Estandar', 'Infantil', 'Mensual'),
(20, 'Premium', 'Deporte', 'Anual');

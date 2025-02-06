create DATABASE HitoTareas2T;

create Table usuarios(
    email VARCHAR(25) PRIMARY KEY,
    usuario VARCHAR(25),
    passw VARCHAR(255),
    rol set('admin','user')
);

create table tareas(

    id_tarea int AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25),
    titulo VARCHAR(25),
    descripcion VARCHAR(255),
    estado set('Completada','En_curso','Pausada','Cancelada'),
    Foreign Key (email) REFERENCES usuarios(email)

);

insert into usuarios values('1admin@admin.com','admi1','$2y$10$S2ZVNqU/8YSTqkJHvLXMOOOlvXxtKvh.gwqDqFOM7fkhHj4j4lefm','admin');


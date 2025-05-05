CREATE table categoria(
id_categoria int PRIMARY key,
    catg varchar(50)
);


CREATE TABLE Pelicula (
    id_pelicula INT PRIMARY KEY,
    Titulo VARCHAR(50),
    Valoraciones INT,
    Categoria INT,
    Lanzamiento DATE,
    FOREIGN KEY (Categoria) REFERENCES Categoria(id_categoria)
);


INSERT INTO categoria (id_categoria, catg) VALUES (1, 'Acción');
INSERT INTO categoria (id_categoria, catg) VALUES (2, 'Comedia');
INSERT INTO categoria (id_categoria, catg) VALUES (3, 'Drama');
INSERT INTO categoria (id_categoria, catg) VALUES (4, 'Terror');
INSERT INTO categoria (id_categoria, catg) VALUES (5, 'Ciencia Ficción');


INSERT INTO Pelicula (id_pelicula, Titulo, Valoraciones, Categoria, Lanzamiento)
VALUES (101, 'Explosión Final', 85, 1, '2023-07-14');

INSERT INTO Pelicula (id_pelicula, Titulo, Valoraciones, Categoria, Lanzamiento)
VALUES (102, 'Ríe Hasta Caer', 78, 2, '2022-11-05');

INSERT INTO Pelicula (id_pelicula, Titulo, Valoraciones, Categoria, Lanzamiento)
VALUES (103, 'Lágrimas del Pasado', 91, 3, '2021-03-22');

INSERT INTO Pelicula (id_pelicula, Titulo, Valoraciones, Categoria, Lanzamiento)
VALUES (104, 'La Noche del Miedo', 74, 4, '2020-10-31');

INSERT INTO Pelicula (id_pelicula, Titulo, Valoraciones, Categoria, Lanzamiento)
VALUES (105, 'Universos Paralelos', 88, 5, '2024-01-15');

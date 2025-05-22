USE formulario;

CREATE TABLE IF NOT EXISTS estudiantes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  edad INT,
  sexo ENUM('Hombre', 'Mujer'),
  carrera ENUM('ITI', 'ITEM', 'LAG', 'LMI', 'ISTI', 'ITMA'),
  semestre VARCHAR(3),
  matricula BIGINT,
  fecha DATE,
  fecha_nacimiento DATE,
  lugar_nacimiento VARCHAR(100)
);
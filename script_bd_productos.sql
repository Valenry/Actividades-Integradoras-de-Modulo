USE big_bread_production;

CREATE TABLE productos (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  codigo_barras VARCHAR(50),
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  stock INT,
  precio DECIMAL(10,2),
  unidad_medida VARCHAR(50),
  fecha_creacion DATE,
  peso_unitario DECIMAL(10,2)
);


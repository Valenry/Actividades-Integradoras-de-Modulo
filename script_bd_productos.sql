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


_______________________________________________

--INSERT Y SELECT TABLA PRODUCTOS

USE big_bread_production;
INSERT INTO productos (codigo_barras, nombre, descripcion, stock, precio, unidad_medida, fecha_creacion, peso_unitario)
VALUES
  ('1234567890', 'Pan', 'Pan hecho con harina de trigo', 50, 2.99, 'kilo', '2022-01-01', 0.5),
  ('2345678901', 'Torta', 'Torta de chocolate con crema', 20, 12.99, 'unidad', '2022-02-01', 1.5),
  ('3456789012', 'Galletas', 'Galletas con avena y pasas', 30, 5.99, 'paquete', '2022-03-01', 0.2),
  ('4567890123', 'Croissant', 'croissant relleno pulpa de frutilla', 40, 2.49, 'unidad', '2022-04-01', 0.1),
  ('5678901234', 'Bizcochuelo', 'Bizcochuelo de vainilla con glaseado', 25, 8.99, 'unidad', '2022-05-01', 1.0),
  ('6789012345', 'Masas finas', 'Masas finas de manteca', 15, 4.99, 'kilo', '2022-06-01', 0.3);

SELECT * FROM productos;

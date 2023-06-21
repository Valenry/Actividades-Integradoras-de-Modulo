show databases;
use big_bread_production;
CREATE TABLE recetas (
  id_receta INT PRIMARY KEY AUTO_INCREMENT,
  id_producto INT,
  id_insumo INT,
  cantidad_requerida INT,
  orden_preparacion INT,
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
  FOREIGN KEY (id_insumo) REFERENCES insumos(id_insumo)
);
.....................................................................
use big_bread_production;

INSERT INTO recetas (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta)
VALUES
  ((SELECT id_producto FROM productos WHERE codigo_barras = '1234567890' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Harina' AND descripcion = 'Harina de trigo para uso en panadería' LIMIT 1), 500, 1, 'Receta de Pan'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '1234567890' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Agua' AND descripcion = 'Agua templada para uso en panadería' LIMIT 1), 250, 2, 'Receta de Pan'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '1234567890' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Levadura' AND descripcion = 'Levadura seca para uso en panadería' LIMIT 1), 10, 3, 'Receta de Pan'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '1234567890' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Azúcar' AND descripcion = 'Azúcar refinada para uso en panadería' LIMIT 1), 50, 4, 'Receta de Pan'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '1234567890' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Manteca' AND descripcion = 'Manteca animal para uso en panadería' LIMIT 1), 30, 5, 'Receta de Pan');

INSERT INTO recetas (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta)
VALUES
  ((SELECT id_producto FROM productos WHERE codigo_barras = '2345678901' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Harina' AND descripcion = 'Harina de trigo para uso en panadería' LIMIT 1), 800, 1, 'Receta de Torta'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '2345678901' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Azúcar' AND descripcion = 'Azúcar refinada para uso en panadería' LIMIT 1), 100, 2, 'Receta de Torta'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '2345678901' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Huevo' AND descripcion = 'Huevo de color para uso en panadería' LIMIT 1), 5, 3, 'Receta de Torta'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '2345678901' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Leche' AND descripcion = 'Leche de vaca para uso en panadería' LIMIT 1), 200, 4, 'Receta de Torta'),
  ((SELECT id_producto FROM productos WHERE codigo_barras = '2345678901' LIMIT 1), (SELECT id_insumo FROM insumos WHERE nombre = 'Chocolate' AND descripcion = 'Chocolate blanco para uso en panadería' LIMIT 1), 150, 5, 'Receta de Torta');

SELECT r.id_receta, p.nombre AS nombre_producto, i.nombre AS nombre_insumo, r.cantidad_requerida, r.orden_preparacion
FROM recetas r
JOIN productos p ON r.id_producto = p.id_producto
JOIN insumos i ON r.id_insumo = i.id_insumo;


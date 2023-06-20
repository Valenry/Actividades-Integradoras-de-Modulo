use actividad3;
-- -----------------------------------------------------
-- Table `big_bread_productos`.`insumos`
-- -----------------------------------------------------
CREATE TABLE insumos (
  id_insumo INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  precio DECIMAL(10,2),
  cantidad INT,
  proveedor VARCHAR(50)
);



-- INSERT Y SELECT TABLA INSUMOS

use big_bread_production;
INSERT INTO insumos (nombre, descripcion, precio, cantidad, proveedor)
VALUES 
  ('Harina', 'Harina de trigo para uso en panadería', 10.99, 100, 'Proveedor A'),
  ('Harina', 'Harina de maíz para uso en panadería', 9.99, 80, 'Proveedor B'),
  ('Harina', 'Harina de arroz para uso en panadería', 11.99, 90, 'Proveedor C'),
  ('Azúcar', 'Azúcar refinada para uso en panadería', 5.99, 50, 'Proveedor D'),
  ('Azúcar', 'Azúcar brown para uso en panadería', 6.99, 60, 'Proveedor E'),
  ('Azúcar', 'Azúcar impalpable para uso en panadería', 7.99, 70, 'Proveedor F'),
  ('Manteca', 'Manteca animal para uso en panadería', 8.99, 80, 'Proveedor G'),
  ('Manteca', 'Manteca vegetal para uso en panadería', 9.99, 90, 'Proveedor H'),
  ('Levadura', 'Levadura seca para uso en panadería', 3.99, 30, 'Proveedor I'),
  ('Levadura', 'Levadura fresca para uso en panadería', 4.99, 40, 'Proveedor J'),
  ('Levadura', 'Levadura química para uso en panadería', 2.99, 20, 'Proveedor K'),
  ('Huevo', 'Huevo de color para uso en panadería', 2.99, 60, 'Proveedor L'),
  ('Huevo', 'Huevo blanco para uso en panadería', 2.99, 70, 'Proveedor M'),
  ('Leche', 'Leche de vaca para uso en panadería', 4.99, 80, 'Proveedor N'),
  ('Leche', 'Leche de almendras para uso en panadería', 5.99, 90, 'Proveedor O'),
  ('Leche', 'Leche de soja para uso en panadería', 6.99, 100, 'Proveedor P'),
  ('Vainilla', 'Esencia de vainilla para uso en panadería', 6.99, 20, 'Proveedor Q'),
  ('Vainilla', 'Esencia de vainilla para uso en panadería', 5.99, 30, 'Proveedor R'),
  ('Pulpa', 'Pulpa de frutilla para uso en panadería', 4.99, 40, 'Proveedor S'),
  ('Pulpa', 'Pulpa de manzana para uso en panadería', 4.99, 50, 'Proveedor T'),
  ('Pulpa', 'Pulpa de durazno para uso en panadería', 4.99, 60, 'Proveedor U'),
  ('Pulpa', 'Pulpa de mango para uso en panadería', 4.99, 70, 'Proveedor V'),
  ('Colorante', 'Colorante en gel para uso en panadería', 2.99, 30, 'Proveedor W'),
  ('Colorante', 'Colorante en pasta para uso en panadería', 2.99, 40, 'Proveedor X'),
  ('Chocolate', 'Chocolate blanco para uso en panadería', 3.99, 50, 'Proveedor Y'),
  ('Chocolate', 'Chocolate negro para uso en panadería', 3.99, 60, 'Proveedor Z'),
  ('Aceite', 'Aceite de oliva para uso en panadería', 7.99, 50, 'Proveedor A'),
  ('Aceite', 'Aceite de maíz para uso en panadería', 6.99, 60, 'Proveedor B'),
  ('Aceite', 'Aceite de girasol para uso en panadería', 5.99, 70, 'Proveedor C'),
  ('Agua', 'Agua templada para uso en panadería', 0.99, 100, 'Proveedor D'),
  ('Agua', 'Agua de rosas para uso en panadería', 2.99, 50, 'Proveedor E'),
  ('Agua', 'Agua de azahar para uso en panadería', 2.99, 60, 'Proveedor F');
  
  SELECT * FROM insumos;

UPDATE insumos
SET nombre = CONCAT(nombre, '_', id_insumo)
WHERE id_insumo IN (
  SELECT id_insumo
  FROM (
    SELECT MIN(id_insumo) AS id_insumo
    FROM insumos
    GROUP BY nombre
    HAVING COUNT(*) > 1
  ) AS duplicates
);








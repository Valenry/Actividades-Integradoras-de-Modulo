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

use actividad3;
INSERT INTO insumos (id_insumo, nombre, cantidad)
VALUES 
   (1, 'harina', '10 kg'),
   (2, 'huevo', '12 unidades'),
   (3, 'azucar', '5 kg'),
   (4, 'margarina', '500 g'),
   (5, 'leche', '1 litro'),
   (6, 'sal', '1 kg'),
   (7, 'levadura', '25 g'),
   (8, 'manteca', '200 g'),
   (9, 'esencia de vainilla', '100 ml');
   
   SELECT * FROM actividad3.insumos;










use actividad3;
-- -----------------------------------------------------
-- Table `actividad3`.`insumos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `insumos` (
  `id_insumo` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_insumo`)
)
ENGINE = InnoDB;

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










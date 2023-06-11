
-- Table `actividad3`.`recetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `actividad3`.`recetas` (
  `id_recetas` INT NOT NULL AUTO_INCREMENT,
  `insumos_id_insumo` INT NOT NULL,
  `productos_id_producto` INT NOT NULL,
  `cantidad_requerida` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_recetas`),
  CONSTRAINT `fk_recetas_insumo`
    FOREIGN KEY (`insumos_id_insumo`)
    REFERENCES `actividad3`.`insumos` (`id_insumo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recetas_productos1`
    FOREIGN KEY (`productos_id_producto`)
    REFERENCES `actividad3`.`productos` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB
DEFAULT CHARSET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

CREATE INDEX `fk_recetas_insumo_idx` ON `actividad3`.`recetas` (`insumo_id_insumo` ASC) VISIBLE;
CREATE INDEX `fk_recetas_productos1_idx` ON `actividad3`.`recetas` (`productos_id_producto` ASC) VISIBLE;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
use actividad3;

INSERT INTO recetas (insumo_id_insumo, productos_id_producto, cantidad_requerida)
SELECT i.id_insumo, p.id_producto, '500 g'
FROM insumos i
JOIN productos p ON p.nombre = 'medialuna'
WHERE i.nombre IN ('harina', 'manteca', 'azucar');


INSERT INTO recetas (insumo_id_insumo, productos_id_producto, cantidad_requerida)
SELECT i.id_insumo, p.id_producto, '1 kg'
FROM insumos i
JOIN productos p ON p.nombre = 'pan'
WHERE i.nombre IN ('harina', 'sal', 'levadura');


INSERT INTO recetas (insumo_id_insumo, productos_id_producto, cantidad_requerida)
SELECT i.id_insumo, p.id_producto, '800 g'
FROM insumos i
JOIN productos p ON p.nombre = 'criollos'
WHERE i.nombre IN ('harina', 'manteca', 'sal', 'levadura');


INSERT INTO recetas (insumo_id_insumo, productos_id_producto, cantidad_requerida)
SELECT i.id_insumo, p.id_producto, '1 kg'
FROM insumos i
JOIN productos p ON p.nombre = 'tartas'
WHERE i.nombre IN ('harina', 'huevo', 'azucar', 'manteca');


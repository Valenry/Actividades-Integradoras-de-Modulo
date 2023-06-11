
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

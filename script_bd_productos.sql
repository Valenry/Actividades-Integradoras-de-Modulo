use actividad3;
-- -----------------------------------------------------
-- Table `actividad3`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS actividad3.productos (
id_producto INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(45) NOT NULL,
PRIMARY KEY (id_producto))
ENGINE = InnoDB;

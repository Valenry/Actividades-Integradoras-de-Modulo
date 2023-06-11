use actividad3;
-- -----------------------------------------------------
-- Table `actividad3`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS actividad3.productos (
id_producto INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(45) NOT NULL,
PRIMARY KEY (id_producto))
ENGINE = InnoDB;


_________________________________________________________


use actividad3;

INSERT INTO productos (id_producto,nombre)VALUES
('1','Pan');

INSERT INTO productos (id_producto,nombre)VALUES
('2','Medialunas');

INSERT INTO productos (id_producto,nombre)VALUES
('3','Criollos');

INSERT INTO productos (id_producto,nombre)VALUES
('4','Tortas');

INSERT INTO productos (id_producto,nombre)VALUES
('5','Tartas');

INSERT INTO productos (id_producto,nombre)VALUES
('6','Masas finas');

INSERT INTO productos (id_producto,nombre)VALUES
('7','Grisines');

INSERT INTO productos (id_producto,nombre)VALUES
('8','Croissants');

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema pulp_fiction_dialogue
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pulp_fiction_dialogue
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pulp_fiction_dialogue`;
CREATE SCHEMA IF NOT EXISTS `pulp_fiction_dialogue` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `pulp_fiction_dialogue` ;

-- -----------------------------------------------------
-- Table `pulp_fiction_dialogue`.`actors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pulp_fiction_dialogue`.`actors` (
  `actor_id` INT NOT NULL AUTO_INCREMENT,
  `film_character` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`actor_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `pulp_fiction_dialogue`.`place`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pulp_fiction_dialogue`.`place` (
  `place_id` INT NOT NULL AUTO_INCREMENT,
  `place` VARCHAR(80) NULL DEFAULT NULL,
  PRIMARY KEY (`place_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `pulp_fiction_dialogue`.`line_quotes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pulp_fiction_dialogue`.`line_quotes` (
  `line_id` INT NOT NULL AUTO_INCREMENT,
  `line_quote` VARCHAR(10000) NULL DEFAULT NULL,
  `actors_actor_id1` INT NOT NULL,
  `place_place_id` INT NOT NULL,
  PRIMARY KEY (`line_id`),
  INDEX `fk_line_quotes_actors1_idx` (`actors_actor_id1` ASC) VISIBLE,
  INDEX `fk_line_quotes_place1_idx` (`place_place_id` ASC) VISIBLE,
  CONSTRAINT `fk_line_quotes_actors1`
    FOREIGN KEY (`actors_actor_id1`)
    REFERENCES `pulp_fiction_dialogue`.`actors` (`actor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_line_quotes_place1`
    FOREIGN KEY (`place_place_id`)
    REFERENCES `pulp_fiction_dialogue`.`place` (`place_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

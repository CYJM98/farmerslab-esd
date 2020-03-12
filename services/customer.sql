SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Customer`

CREATE DATABASE IF NOT EXISTS `Customer` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Customer`;

-- --------------------------------------------------------
-- Table structure for table `Customer`

DROP TABLE IF EXISTS Customer;
CREATE TABLE IF NOT EXISTS Customer (
  CustID int(6) NOT NULL AUTO_INCREMENT,
  CustEmail varchar(100) NOT NULL,
  FirstName varchar(50) NOT NULL,
  LastName varchar(50) NOT NULL,
  Birthdate date NOT NULL,
  Gender char(1) NOT NULL,
  MobileNum int(10) NOT NULL,
  Address varchar(100) NOT NULL,
  UnitNum varchar(10) NOT NULL,
  PostalCode int(10) NOT NULL,
  Country varchar(100) NOT NULL,
  RegistrationDate date NOT NULL,
  Username varchar(50) NOT NULL,
  Password varchar(50) NOT NULL,
  PRIMARY KEY (`CustID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customer`
--

INSERT INTO Customer (CustEmail, FirstName, LastName, Birthdate, Gender, MobileNum, Address, UnitNum, PostalCode, Country, RegistrationDate, Username, Password) VALUES
("jeffkua@gmail.com", "Jeff", "Kua", "1998-01-11", "F", 99998888, "10 Punggol Rd", "11-72", 560123, "Singapore", "2019-12-12", "jefflovetae", "greenunicorn1!"),
("samquek@gmail.com", "Sam", "Quek", "1996-01-17", "M", 98457489, "134 Lakeside St", "11-50", 560134, "Singapore", "2019-12-12", "samquek", "greenunicorn1!"),
("sebastianng@gmail.com", "Sebastian", "Ng", "1993-03-11", "M", 94567448, "54 Pasir Ris Rd", "11-23", 560123, "Singapore", "2019-12-12", "sebasng", "greenunicorn1!");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
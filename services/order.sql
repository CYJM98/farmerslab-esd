SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Orders`

CREATE DATABASE IF NOT EXISTS `Orders` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Orders`;

-- --------------------------------------------------------
-- Table structure for table `Orders'

DROP TABLE IF EXISTS `Orders`;
CREATE TABLE IF NOT EXISTS `Orders` (
  OrderID int(6) NOT NULL,
  CustEmail varchar(100) NOT NULL,
  ProductName varchar(100) NOT NULL,
  OrderQuantity int NOT NULL,
  DeliveryID int(6) NOT NULL,
  OrderDate date NOT NULL,
  PRIMARY KEY (`OrderID`, `ProductName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Orders`
--

INSERT INTO `Orders` (OrderID, CustEmail, ProductName, OrderQuantity, DeliveryID, OrderDate) VALUES
("909211", "jeffkua@gmail.com", "Onion", "2" ,"128374", "2020-01-03 21:43:23"),
("909211", "jeffkua@gmail.com","Leek", "1", "128374", "2020-01-03 21:43:23"),
("909222", "samquek@gmail.com", "Carrot","3","128375", "2020-01-05 21:43:23"),
("909233", "sebastianng@gmail.com", "Kale", "1","128376", "2020-01-06 21:43:23"),
("909244", "sebastianng@gmail.com", "Garlic", "2","128377", "2020-01-07 21:43:23");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
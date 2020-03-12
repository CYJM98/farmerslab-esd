SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Delivery`

CREATE DATABASE IF NOT EXISTS `Delivery` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Delivery`;

-- --------------------------------------------------------
-- Table structure for table `Delivery`

DROP TABLE IF EXISTS Delivery;
CREATE TABLE IF NOT EXISTS Delivery (
  DeliveryID int(6) NOT NULL AUTO_INCREMENT,
  OrderID int(6) NOT NULL,
  OrderTrackingID varchar(100),
  DeliveryDate date NOT NULL,
  PRIMARY KEY (`DeliveryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Delivery`
--

INSERT INTO Delivery (DeliveryID, OrderID, OrderTrackingID, DeliveryDate) VALUES
("000001", "TP410051419SG", "2020-04-22"),
("000002", "", "");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
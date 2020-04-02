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
  DeliveryID int(6) NOT NULL,
  OrderID int(6) NOT NULL,
  OrderTrackingID varchar(100) NULL,
  DeliveryDate date NOT NULL,
  DeliveryStatus int(1) NOT NULL, 
  PRIMARY KEY (`DeliveryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Delivery`
--

INSERT INTO Delivery (DeliveryID, OrderID, DeliveryDate, DeliveryStatus) VALUES
("128374", "909211", "2020-01-10", "1"),
("128375", "909222", "2020-01-11", "1"),
("128376", "909233", "2020-02-12", "1"),
("128377", "909244", "2020-02-13", "0");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
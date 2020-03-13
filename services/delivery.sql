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
  PurchaseID int(6) NOT NULL,
  PurchaseTrackingID varchar(100) NOT NULL,
  DeliveryDate date NOT NULL,
  PRIMARY KEY (`DeliveryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Delivery`
--

INSERT INTO Delivery (DeliveryID, PurchaseID, PurchaseTrackingID, DeliveryDate) VALUES
("000001", "000001", "128374", "2020-01-10"),
("000002", "000002", "128375", "2020-01-11"),
("000003", "000003", "128376", "2020-02-12"),
("000004", "000004", "128377", "2020-02-13"),
("000005", "000005", "128378", "2020-01-14");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
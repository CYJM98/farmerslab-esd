SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Order`

CREATE DATABASE IF NOT EXISTS `Order` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Order`;

-- --------------------------------------------------------
-- Table structure for table `Order`

DROP TABLE IF EXISTS Order;
CREATE TABLE IF NOT EXISTS Order (
  OrderID int(6) NOT NULL AUTO_INCREMENT,
  CustID int(6) NOT NULL,
  ProductID int(6),
  OrderDate date NOT NULL,
  PRIMARY KEY (`OrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Order`
--

INSERT INTO Order (OrderID, OrderID, OrderTrackingID, OrderDate) VALUES
("000001", "TP410051419SG", "2020-04-22"),
("000002", "", "");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
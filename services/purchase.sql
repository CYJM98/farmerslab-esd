SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: ``

CREATE DATABASE IF NOT EXISTS `Purchase` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Purchase`;

-- --------------------------------------------------------
-- Table structure for table `Purchase'

DROP TABLE IF EXISTS Purchase;
CREATE TABLE IF NOT EXISTS Purchase (
  PurchaseID int(6) NOT NULL AUTO_INCREMENT,
  CustID int(6) NOT NULL,
  ProductID int(6) NOT NULL,
  PurchaseTrackingID int(6) NOT NULL,
  PurchaseDate datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`PurchaseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Purhcase`
--

INSERT INTO Purchase (CustID, ProductID, PurchaseTrackingID, PurchaseDate) VALUES
("128374", "000001","128374", "2020-01-03 21:43:23:523"),
("128375", "000002","128375", "2020-01-04 21:43:23:523"),
("128376", "000003","128376", "2020-01-05 21:43:23:523"),
("128377", "000004","128377", "2020-01-06 21:43:23:523"),
("128378", "000001","128378", "2020-01-07 21:43:23:523");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Payment`

CREATE DATABASE IF NOT EXISTS `Payment` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Payment`;

-- --------------------------------------------------------
-- Table structure for table `Payment`

DROP TABLE IF EXISTS Payment;
CREATE TABLE IF NOT EXISTS Payment (
  PaymentID int(6) NOT NULL,
  OrderID int(6) NOT NULL,
  PaymentAmount float(10,2) NOT NULL,
  PaymentDateTime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PaymentType varchar(50) NOT NULL,
  PRIMARY KEY (`PaymentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Payment`
--

INSERT INTO Payment (OrderID, PaymentAmount, PaymentDateTime, PaymentType) VALUES
("1", "59.90", "2020-01-03 21:43:23:523", "Visa"),
("2", "22.75", "2020-01-04 21:43:23:523", "Visa"),
("3", "33.22", "2020-01-05 21:43:23:523", "Mastercard"),
("4", "12.11", "2020-01-06 21:43:23:523", "Visa"),
("5", "123.90", "2020-01-07 21:43:23:523", "Mastercard");

COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
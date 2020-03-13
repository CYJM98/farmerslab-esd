SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Product`

CREATE DATABASE IF NOT EXISTS `Product` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Product`;

-- --------------------------------------------------------
-- Table structure for table `Product`

DROP TABLE IF EXISTS Product;
CREATE TABLE IF NOT EXISTS Product (
  ProductID int(6) NOT NULL AUTO_INCREMENT,
  ProductName varchar(100) NOT NULL,
  ProductType varchar(100),
  ProductDescription varchar(999),
  Quantity int NOT NULL,
  UnitPrice float(10,2) NOT NULL,
  UnitWeight float(10,2) NOT NULL,
  ProductImage varchar(50),
  PRIMARY KEY (`ProductID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Product`
--
INSERT INTO Product (ProductName, ProductType, ProductDescription, Quantity, UnitPrice, UnitWeight, ProductImage) VALUES
("Onion", "Vegetable", "An onion is a round vegetable with a brown skin that grows underground. Compatabile with almost every dish.", 5, 3, 2, "onion.jpg"),
("Tomato", "Vegetable", "Tomatoes are small, soft, red fruit that you can eat raw in salads or cooked as a vegetable.", 10, 4, 2, "tomato.jpg"),
("Carrot", "Vegetable", "Carrots are long, thin, orange-coloured vegetables.", 15, 3, 3, "carrot.jpg"),
("Broccoli", "Vegetable", "Broccoli is a vegetable with green stalks and green or purple tops.", 20, 3, 4, "broccoli.jpg"),
("Cauliflower", "Vegetable", "Cauliflower is a large round vegetable that has a hard white centre surrounded by green leaves.", 20, 3, 3, "cauliflower.jpg"),
("Corn", "Vegetable", "Corn is used to refer to crops such as wheat and barley.", 20, 2, 2, "corn.jpg"),
("Cabbage", "Vegetable", "A cabbage is a round vegetable with white, green, or purple leaves that is usually eaten cooked.", 30, 2, 3, "cabbage.jpg"),
("Asparagus", "Vegetable", "Asparagus is a vegetable that is long and green and has small shoots at one end. It is cooked and served whole.", 20, 4, 2, "asparagus.jpg"),
("Leek", "Vegetable", "Leeks are long thin vegetables which smell similar to onions.", 30, 2, 1, "leek.jpg"),
("Kale", "Vegetable", "Kale is a vegetable that is similar to a cabbage.", 40, 2, 2, "kale.jpg"),
("Spinach", "Vegetable", "Spinach is a vegetable with large dark green leaves that you chop up and boil in water before eating.", 30, 3, 2, "spinach.jpg"),
("Coriander", "Vegetable", "Coriander is a plant with seeds that are used as a spice and leaves that are used as a herb.", 50, 2, 1, "coriander.jpg"),
("Lettuce", "Vegetable", "A lettuce is a plant with large green leaves that is the basic ingredient of many salads.", 47, 2, 3, "lettuce.jpg"),
("Mushroom", "Vegetable", "Mushrooms are fungi that you can eat.", 30, 4, 2, "mushroom.jpg"),
("Garlic", "Vegetable", "Garlic has a very strong smell and taste and is used in cooking.", 20, 4, 2, "garlic.jpg"),
("Ginger", "Vegetable", "Ginger is the root of a plant that is used to flavour food. It has a sweet spicy flavour and is often sold in powdered form.", 30, 3, 2, "ginger.jpg"),
("Radish", "Vegetable", "Radishes are small red or white vegetables that are the roots of a plant. They are eaten raw in salads.", 15, 3, 4, "radish.jpg"),
("Yam", "Vegetable", "A yam is a root vegetable which is like a potato, and grows in tropical regions.", 15, 4, 1, "yam.jpg"),
("Turnip", "Vegetable", "A turnip is a round vegetable with a greenish-white skin that is the root of a crop.", 27, 5, 3, "turnip.jpg"),
("Potato", "Vegetable", "Potatoes are quite round vegetables with brown or red skins and white insides. They grow under the ground.", 18, 4, 5, "potato.jpg");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
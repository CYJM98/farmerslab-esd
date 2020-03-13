SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `Newsletter`

CREATE DATABASE IF NOT EXISTS `Newsletter` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Newsletter`;

-- --------------------------------------------------------
-- Table structure for table `Newsletter`

DROP TABLE IF EXISTS Newsletter;
CREATE TABLE IF NOT EXISTS Newsletter (
  NewsletterID int(6) NOT NULL AUTO_INCREMENT,
  Content varchar(999) NOT NULL,
  PRIMARY KEY (`NewsletterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Newsletter`
--

INSERT INTO Newsletter (Content) VALUES
("
ONIONS: Packed with vibrant flavor, onions are a staple food throughout the world. Familiar bulb onions are easy to cultivate as long as you plant varieties adapted to your climate, and you can expand your onion season by growing leeks, scallions, and other non-bulbing varieties. Fertile, well-drained soil that’s slightly acidic (a pH between 6.0 and 6.8) is best for growing onions of all types.
Onion Growing Tips:
Choose the least weedy section of your garden for growing onions. You can start seeds early, because onion seedlings are easy to hold in containers until it’s time to plant them. Delay planting until the last cold spell has passed. Exposure to prolonged cold can cause bulb onions to bolt, and plants grown from sets are more prone to bolting than those grown from seedlings. 
Cooking with Onions:
Does a cook ever have enough onions? Pungent bulb onions and mild leeks are best for soups, stews, and other dishes that cook for a long time. Use tender young scallions when you need bright punches of raw onion flavor. Leeks are great for drying. Flawed bulb onions that are not likely to store well can be added to summer pickles.
"),
("
TOMATOES: The exquisite flavor and irresistible juiciness of homegrown tomatoes put them at or near the top of most gardeners’ planting lists. Fruit size, color and flavor differ with each variety, but all tomatoes grow best under warm conditions. For the best flavor, provide fertile, organically enriched soil with a pH between 6.0 and 6.5, and plant your tomatoes in a site that gets plenty of sun.
Tomato Types to Try:
Many organic gardeners include varieties of the following three types of tomatoes in their gardens each year.
Cherry tomatoes and salad tomatoes produce small fruits in a rainbow of colors and an array of shapes, including round, pear-shaped and teardrop-shaped.
Slicing tomatoes are round and juicy, making them ideal for eating fresh. Fruit size and color vary, and some varieties produce surprisingly large fruits.
Paste tomatoes, also called canning tomatoes, have dense flesh and little juice, so they are the best type for cooking, canning and drying.
");
COMMIT;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
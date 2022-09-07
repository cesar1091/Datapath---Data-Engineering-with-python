*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`datapath_project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `datapath_project`;

DROP TABLE IF EXIST `order_items`;

CREATE TABLE `order_items` (
    `order_item_id` int(11) NOT NULL,
    `order_item_order_id` int(11) NOT NULL,
    `order_item_product_id` int(11) NOT NULL,
    `order_item_quantity` smallint(4) NOT NULL,
    `order_item_subtotal` decimal(10,2) DEFAULT NULL,
    `order_item_product_price` decimal(10,2) DEFAULT NULL,
    PRIMARY KEY (`order_item_id`),
    KEY `order_item_order_id` (`order_item_order_id`),
    KEY `order_item_product_id` (`order_item_product_id`),
    CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_item_order_id`) REFERENCES `orders` (`order_id`),
    CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`order_item_product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/data/order_items'
INTO TABLE `order_items` COLUMNS TERMINATED BY '|';

DROP TABLE IF EXIST `orders`;

CREATE TABLE `orders` (
    `order_id` int(11) NOT NULL,
    `order_date` date NOT NULL,
    `order_customer_id` int(11) NOT NULL,
    `order_status` varchar(45) DEFAULT NULL,
    PRIMARY KEY (`order_id`),
    KEY `order_customer_id` (`order_customer_id`),
    CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`order_customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/data/orders'
INTO TABLE `orders` COLUMNS TERMINATED BY '|';

DROP TABLE IF EXIST `customers`;

CREATE TABLE `customers` (
    `customer_id` int(11) NOT NULL,
    `customer_fname` varchar(45) DEFAULT NULL,
    `customer_lname` varchar(45) DEFAULT NULL,
    `customer_email` varchar(45) NOT NULL,
    `customer_password` varchar(45) NOT NULL,
    `customer_street` varchar(45) DEFAULT NULL,
    `customer_city` varchar(45) DEFAULT NULL,
    `customer_state` varchar(45) DEFAULT NULL,
    `customer_zipcode` varchar(45) DEFAULT NULL,
    PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/data/customer'
INTO TABLE `customers` COLUMNS TERMINATED BY '|';

DROP TABLE IF EXIST `products`;

CREATE TABLE `products` (
    `product_id` int(11) NOT NULL,
    `product_category_id` int(11) NOT NULL,
    `product_name` varchar(45) DEFAULT NULL,
    `product_description` varchar(45) DEFAULT NULL,
    `product_price` decimal(10,2) NOT NULL,
    `product_image` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`product_id`),
    KEY `product_category_id` (`product_category_id`),
    CONSTRAINT `products_ibfk_1` FOREIGN KEY (`product_category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/data/products'
INTO TABLE `products` COLUMNS TERMINATED BY '|';

DROP TABLE IF EXIST `categories`;

CREATE TABLE `categories` (
    `category_id` int(11) NOT NULL,
    `category_department_id` int(11) NOT NULL,
    `category_name` varchar(45) DEFAULT NULL,
    PRIMARY KEY (`category_id`),
    KEY `category_department_id` (`category_department_id`),
    CONSTRAINT `categories_ibfk_1` FOREIGN KEY (`category_department_id`) REFERENCES `departments` (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/data/categories'
INTO TABLE `categories` COLUMNS TERMINATED BY '|';

DROP TABLE IF EXIST `departments`;

CREATE TABLE `departments` (
    `department_id` int(11) NOT NULL,
    `department_name` varchar(45) NOT NULL,
    PRIMARY KEY (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/data/departments'
INTO TABLE `departments` COLUMNS TERMINATED BY '|';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
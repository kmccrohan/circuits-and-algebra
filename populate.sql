SET sql_mode = STRICT_ALL_TABLES;

DROP TABLE IF EXISTS `checkout`;
DROP TABLE IF EXISTS `member`;
DROP TABLE IF EXISTS `copy`;
DROP TABLE IF EXISTS `book`;
DROP TABLE IF EXISTS `librarian`;
DROP TABLE IF EXISTS `library`;

CREATE TABLE `library` (
  `library_id` int NOT NULL AUTO_INCREMENT,
  `library_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  PRIMARY KEY (`library_id`)
) ENGINE = InnoDB;

CREATE TABLE `librarian` (
  `librarian_id` int NOT NULL AUTO_INCREMENT,
  `library_id` int NOT NULL,
  `librarian_name` varchar(50) NOT NULL,
  PRIMARY KEY (`librarian_id`),
  FOREIGN KEY (`library_id`) REFERENCES `library` (`library_id`)
) ENGINE = InnoDB;

CREATE TABLE `book` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE = InnoDB;

CREATE TABLE `copy` (
  `copy_id` int NOT NULL AUTO_INCREMENT,
  `library_id` int NOT NULL,
  `book_id` int NOT NULL,
  PRIMARY KEY (`copy_id`),
  FOREIGN KEY (`library_id`) REFERENCES `library` (`library_id`),
  FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`)
) ENGINE = InnoDB;

CREATE TABLE `member` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `member_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE = InnoDB;

CREATE TABLE `checkout` (
  `librarian_id` int NOT NULL,
  `copy_id` int NOT NULL,
  `member_id` int NOT NULL,
  `checkout_date` DATE NOT NULL,
  `checkin_date` DATE,
  PRIMARY KEY (`librarian_id`, `copy_id`, `member_id`, `checkout_date`),
  FOREIGN KEY (`librarian_id`) REFERENCES `librarian` (`librarian_id`),
  FOREIGN KEY (`member_id`) REFERENCES `member` (`member_id`),
  FOREIGN KEY (`copy_id`) REFERENCES `copy` (`copy_id`)
) ENGINE = InnoDB;

INSERT INTO `library` (`library_name`, `address`, `phone`) VALUES
('Kenmore Library', '445 W 1st ave Kenmore WA', '4257789023'),
('Brier Library', '9708 223rd st Brier WA', '4258859783');

INSERT INTO `librarian` (`library_id`, `librarian_name`) VALUES
(1, 'Mary'),
(1, 'Thomas'),
(2, 'Michael');

INSERT INTO `book` (`author`, `title`) VALUES
('Dr Suess', 'Green Eggs and Ham'),
('Dr Suess', 'One Fish Two Fish'),
('George Orwell', 'Animal Farm'),
('George Orwell', '1984'),
('Shakespeare', 'MacBeth'),
('Susan Collins', 'The Hunger Games');

INSERT INTO `copy` (`library_id`, `book_id`) VALUES
(1, 1),
(2, 1),
(2, 2),
(1, 3),
(1, 3),
(2, 4),
(2, 6);

INSERT INTO `member` (`member_name`, `address`, `phone`) VALUES
('Jimmy', '123 Nora St Kenmore WA', '2067344555'),
('Margaret', '234 Nora St Kenmore WA', '2069980123'),
('Evan', '345 Bora Rd Kenmore WA', '2068899637');

INSERT INTO `checkout` VALUES
(1, 3, 2, '2017-11-01', NULL),
(2, 1, 1, '2017-11-02', '2017-11-05'),
(2, 4, 1, '2017-10-14', '2017-10-15'),
(3, 2, 3, '2017-11-13', NULL),
(2, 4, 2, '2017-09-30', '2017-10-01');

SELECT * FROM `library`;
SELECT * FROM `librarian`;
SELECT * FROM `book`;
SELECT * FROM `copy`;
SELECT * FROM `member`;
SELECT * FROM `checkout`;

-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2020 at 05:13 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


--
-- Database: `pro_library`
--

-- --------------------------------------------------------

--
-- 

Table structure for table `tbl_books`


--

CREATE TABLE `tbl_books` 
(
  `Book_Id` int(11) NOT NULL AUTO INCREMENT,
  
`Book_Name` varchar(150) DEFAULT NULL,
  
`Author` varchar(100) DEFAULT NULL,
  
`Publisher` varchar(100) DEFAULT NULL,
  
`Edition` varchar(100) DEFAULT NULL,
  
`Book_Count` int(11) NOT NULL
) 
ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Dumping data for table `tbl_books`


--

INSERT INTO `tbl_books` 
(`Book_Id`, `Book_Name`, `Author`, `Publisher`, `Edition`, `Book_Count`) 
VALUES

(1, 'Python for Everybody for XI', 'Charles R. Severance', 'Elliott Hauser', '2016-Jul-05', 27),

(2, 'Software Engineering for XII', 'Ian Sommerville', 'Pearson', '9th Edition, 2011', 40),

(3, 'Concepts of Physics for X', 'H. C. Verma', 'Verma', '2019', 32),

(4, 'Chemistry for XII', 'Rashmi', 'Arihant', '2019', 10),

(5, 'Geography for XI', 'Graphein', 'Pearson', '2018', 76),

(6, 'History for VII', 'Bipan Chandra', 'Altis Vortex', '2017', 24),

(7, 'Business Studies for XII', 'S Chand Wason', 'Disha Publications', '2019', 45),

(8, 'Mathematics for XII', ' Paul Erdos', 'Arihant', '2018', 26);



-- ---------------------------------- Table structure for table `tbl_issued_books`
-------------------

-- ----------------------------

--
-- Table structure for table `tbl_students`
----------------

--

CREATE TABLE `tbl_students` 
(
  `Student_Id` int(11) NOT NULL,
  
`Student_Name` varchar(150) NOT NULL,
  
`Class` int(11) NOT NULL,
  
`Section` varchar(1) NOT NULL
) 
ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Dumping data for table `tbl_students`


--

INSERT INTO `tbl_students` 
(`Student_Id`, `Student_Name`, `Class`, `Section`) 
VALUES

(101, 'Anuj Kumar Dixit', 12, 'A'),

(102, 'Prateek Sah', 12, 'B'),

(103, 'Jyoti Dixit', 11, 'A'),

(104, 'Suryansh Dixit', 10, 'D'),

(105, 'Akhilendra', 10, 'A'),

(106, 'Pranshu', 11, 'C'),

(107, 'Rohit Sharma', 12, 'E'),

(108, 'Vedalam', 7, 'B');



--

CREATE TABLE `tbl_issued_books` 
(
  `Issue_Id` int(11) NOT NULL AUTO INCREMENT,
  
`Book_Id` int(11) NOT NULL
REFERENCES tbl_books(Book_Id) 
REFERENCES tbl_students(Student_Id),  
`Student_Id` int(11) DEFAULT NULL,
  
`Student_Name` varchar(100) DEFAULT NULL,
  
`Issue_Date` date DEFAULT NULL,
  
`Due_Date` date DEFAULT NULL,
  
`Return_Date` date DEFAULT NULL,
  
`Status_If_Returned` int(11) DEFAULT NULL
) 
ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Dumping data for table `tbl_issued_books`


--

INSERT INTO `tbl_issued_books` 
(`Issue_Id`, `Book_Id`, `Student_Id`, `Student_Name`, `Issue_Date`, `Due_Date`, `Return_Date`, `Status_If_Returned`) 
VALUES

(15, 1, 101, 'Anuj Kumar Dixit', '2020-01-05', '2020-01-15', '2020-01-15', 1),

(16, 2, 105, 'Akhilendra', '2019-12-18', '2019-12-28', '2019-12-28', 1),

(17, 1, 102, 'Prateek Sah', '2020-01-05', '2020-01-15', '2020-01-15', 1),

(18, 1, 101, 'Anuj Kumar Dixit', '2020-01-23', '2020-01-31', '2020-01-31', 1),

(21, 8, 107, 'Rohit Sharma', '2020-01-08', '2020-01-18', NULL, 0),

(22, 5, 103, 'Jyoti Dixit', '2020-01-01', '2020-01-11', NULL, 0);



--
-- Indexes for dumped tables
--

--
-- 

Indexes for table `tbl_books`


--
ALTER TABLE `tbl_books`
  
ADD PRIMARY KEY (`Book_Id`);



--
-- Indexes for table `tbl_issued_books`


--
ALTER TABLE `tbl_issued_books`
  
ADD PRIMARY KEY (`Issue_Id`),
  
ADD KEY `fk_book_id` (`Book_Id`),
  
ADD KEY `fk_student_id` (`Student_Id`);



--
-- Indexes for table `tbl_students`


--
ALTER TABLE `tbl_students`
  
ADD PRIMARY KEY (`Student_Id`);



--
-- AUTO_INCREMENT for dumped tables
--

--
-- 

AUTO_INCREMENT for table `tbl_books`


--
ALTER TABLE `tbl_books`
  
MODIFY `Book_Id` int(11) NOT NULL AUTO_INCREMENT, 
AUTO_INCREMENT=9;



--
-- AUTO_INCREMENT for table `tbl_issued_books`


--
ALTER TABLE `tbl_issued_books`
  
MODIFY `Issue_Id` int(11) NOT NULL AUTO_INCREMENT, 
AUTO_INCREMENT=23;



--
-- Constraints for dumped tables
--

--
-- 

Constraints for table `tbl_issued_books`


--
ALTER TABLE `tbl_issued_books`
  
ADD CONSTRAINT `fk_book_id` FOREIGN KEY (`Book_Id`) REFERENCES `tbl_books` (`Book_Id`),
  
ADD CONSTRAINT `fk_student_id` FOREIGN KEY (`Student_Id`) REFERENCES `tbl_students` (`Student_Id`);


COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

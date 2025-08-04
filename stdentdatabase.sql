CREATE TABLE `studentdb`.`students` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NAME` VARCHAR(45) NOT NULL,
  `AGE` INT NOT NULL,
  `EMAIL` VARCHAR(45) NULL,
  `COURSE` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));

USE studentdb;

INSERT INTO students (name, age, email, course) VALUES
('Aarya Shah', 20, 'aarya.shah@email.com', 'CS'),
('Rahul Mehta', 22, 'rahul22@email.com', 'IT'),
('Sneha Reddy', 19, 'sneha.reddy@email.com', 'Mechanical'),
('Kabir Verma', 21, 'kabir.v@email.com', 'Civil'),
('Meera Iyer', 20, 'meera.iyer@email.com', 'Electrical'),
('Aman Kapoor', 23, 'aman.kapoor@email.com', 'CS'),
('Ritu Jain', 18, 'ritu.jain@email.com', 'Electronics'),
('Omkar Patil', 22, 'omkar.p@email.com', 'IT'),
('Priya Deshmukh', 21, 'priya.d@email.com', 'CS'),
('Aditya Joshi', 20, 'aditya.j@email.com', 'Civil');

SELECT * FROM students;

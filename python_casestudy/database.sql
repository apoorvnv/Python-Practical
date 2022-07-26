create database demo;
use demo;
create user 'apoorv' @'localhost'IDENTIFIED BY '3000';
grant all on demo.*to 'apoorv'@'localhost';
create table student(PRN varchar(12),First_Name varchar(20),Middle_Name varchar(20),Last_Name varchar(20),Address varchar(30),
Mobile_Number int, Email_ID varchar(20),DOB date);
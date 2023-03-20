create database APH;

use APH;

create table Admin(User_id int auto_increment primary key,Name varchar(20),Phone_number varchar(15),Email_id varchar(40),Password varchar(30));
create table Disease_Datas(User_id int,Result int);
create table User_details(User_id int auto_increment primary key,Name varchar(20),Phone_number varchar(15),Email_id varchar(40),Password varchar(30));
select * from Disease_Datas;
select * from User_details;

create database BankTrainsaction;

use BankTrainsaction;


create table Users(
	User_id int auto_increment,
    Account_number int not null,
    Passward varchar(10) not null,
    Name varchar(50) not null,
    Phone_number varchar(11),
    Age int check(age >= 18),
    Balance int,
    
    CONSTRAINT PK_Person PRIMARY KEY (User_id, Account_number)
) auto_increment = 1001;


create table Trainsaction(
	Trainsaction_id int auto_increment,
    User_id int not null,
    Account_number int not null,
    Transfer_Date date,
    Amount int,
    
    constraint transfer_pk primary key(Trainsaction_id),
    constraint user_fk foreign key(User_id, Account_number) references Users(User_id, Account_number) on delete cascade

) auto_increment = 100;
create database courseEnroll;

use courseEnroll;

create table student(
	student_id int primary key auto_increment,
    first_name varchar(50) not null,
	last_name varchar(50) not null,
    age int check(age > 15)
) auto_increment = 1001;



create table course(
	course_id int primary key auto_increment,
    course_name varchar(50) not null,
    course_price int
) auto_increment = 1001;



create table enrollment(
	enrollment_id int primary key auto_increment,
    who_enroll int,
    which_course_id int,
    
    constraint studentid_fk foreign key(who_enroll) references student(student_id) on delete cascade,
    constraint courseid_fk foreign key(which_course_id) references course(course_id) on delete cascade
);
##################################################################################################################################
### --------------------------------------------------- mysql connection ------------------------------------------------------###
##################################################################################################################################


import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='***********',
    database='courseEnroll'
)


cursor = connection.cursor()


##################################################################################################################################
### -------------------------------------------- mysql query use by python ----------------------------------------------------###
##################################################################################################################################

# Admit student in institute
def admission(f_name, l_name, age):
    query = """
        INSERT INTO student(first_name, last_name, age)
        VALUES
        (%s, %s, %s);
    """
    
    cursor.execute(query, (f_name, l_name, age))
    connection.commit()
    
    print('Admition successfully complete ✅')
    
    
def studentid(f_name, l_name, age):    
    query1 = """
        SELECT student_id
        FROM student
        WHERE first_name = %s AND last_name = %s AND  age = %s
    """

    cursor.execute(query1, (f_name, l_name, age))
    id = cursor.fetchone()
    
    print(f'\nYour student id is : {id[0]}\n')



# Check Rgisted student or not.    
def isregister(id):
    query = """
            SELECT first_name FROM student
            WHERE student_id = %s;
        """
    cursor.execute(query, id)
    playerid = cursor.fetchone()
    return playerid
    

# show my course
def mycourse(id):
    query = """
        SELECT e.which_course_id, c.course_name
        FROM enrollment AS e
        INNER JOIN course AS c
        ON e.which_course_id = c.course_id
        WHERE e.who_enroll = %s;
    """
    
    cursor.execute(query, id)
    allcourse = cursor.fetchall()
    
    print('\ncourse_id || course_name \n')
    for i in allcourse:
        for j in i:
            print(j, end='\t\t')
        print()
    print()
    
    

# Show all aviable course
def showAllCourse():
    query = """
        select *
        FROM course;
    """
    
    cursor.execute(query)
    allcourse = cursor.fetchall()
    
    print('\ncourse_id || course_name || course_price\n')
    for i in allcourse:
        for j in i:
            print(j, end='\t\t')
        print()
    print()


# Show course price
def coursePrice(course_id):
    query = """
        SELECT course_price FROM course
        WHERE course_id = %s;
    """
    
    cursor.execute(query, course_id)
    price = cursor.fetchone()
  
    return price[0]



# A student enroll a new course
def enrollCourse(id, course_id):
    query = """
        INSERT INTO enrollment(who_enroll, which_course_id)
        VALUES
        (%s, %s);
    """
    
    cursor.execute(query, (id, course_id))
    connection.commit()
    
    print('\nSuccessfully you enroll a new course ✅\n')



# Drop a course
def dropCourse(id, course_id):
    query = """
        DELETE FROM enrollment
        WHERE who_enroll = %s AND which_course_id = %s;
    """
    cursor.execute(query, (id, course_id))
    connection.commit()
    
    print('\nSuccessfully you Drop a course ✅\n')

# add new course
def addNewCourse(course_name, course_price):
    query ="""
        INSERT INTO course(course_name, course_price)
        VALUES
        (%s, %s)
    """
    
    cursor.execute(query, (course_name, course_price))
    connection.commit()
    
    print(f'\nSuccessfully {course_name} course added ✅\n')
    
    

# Show registred but not enrolled  student
def notenroll():
    query = """
        SELECT s.*
        FROM student AS s
        LEFT JOIN enrollment AS e
        ON s.student_id = e.who_enroll
        WHERE e.who_enroll IS NULL;
    """

    cursor.execute(query)
    alldata = cursor.fetchall()
    
    print('\nstudent_id || First_name || Last_name ||   Age\n')
    for i in alldata:
        for j in i:
            print(j, end='\t\t')
        print()
    print()





# show all student
def showallstudent():
    query = """
        SELECT *
        FROM student;
    """

    cursor.execute(query)
    alldata = cursor.fetchall()
    
    print('\nstudent_id || First_name || Last_name ||   Age\n')
    for i in alldata:
        for j in i:
            print(j, end='\t\t')
        print()
    print()



# drop student
def dropstudent(stid):
    query = """
        DELETE FROM student
        WHERE student_id = %s;
    """
    cursor.execute(query, stid)
    connection.commit()
    
    print('\nSuccessfully you Drop a student ✅\n')


# maximum enroll course
def maximumenrollcourse():
    query = """
    WITH cte AS
    (
        SELECT which_course_id, COUNT(*) AS count
        FROM enrollment
        GROUP BY which_course_id
    ),
    cte2 AS
    (
        SELECT which_course_id
        FROM cte
        WHERE count = (SELECT MAX(count) FROM cte)
    )

    SELECT *
    FROM course
    WHERE course_id IN (SELECT which_course_id FROM cte2);
    """

    cursor.execute(query)
    allcourse = cursor.fetchall()
    
    print('\ncourse_id || course_name || course_price\n')
    for i in allcourse:
        for j in i:
            print(j, end='\t\t')
        print()
    print()


# minimum enroll course
def minimumenrollcourse():
    query = """
    WITH cte AS
    (
        SELECT which_course_id, COUNT(*) AS count
        FROM enrollment
        GROUP BY which_course_id
    ),
    cte2 AS
    (
        SELECT which_course_id
        FROM cte
        WHERE count = (SELECT MIN(count) FROM cte)
    )

    SELECT *
    FROM course
    WHERE course_id IN (SELECT which_course_id FROM cte2);
    """

    cursor.execute(query)
    allcourse = cursor.fetchall()
    
    print('\ncourse_id || course_name || course_price\n')
    for i in allcourse:
        for j in i:
            print(j, end='\t\t')
        print()
    print()



# NOT enroll course anyone
def noenroll():
    query = """
        SELECT c.*
        FROM course AS c
        LEFT JOIN enrollment AS e
        ON c.course_id = e.which_course_id
        WHERE e.who_enroll IS NULL;
    """
    cursor.execute(query)
    allcourse = cursor.fetchall()
    
    print('\ncourse_id || course_name || course_price\n')
    for i in allcourse:
        for j in i:
            print(j, end='\t\t')
        print()
    print()



##################################################################################################################################
### ------------------------------------------------------- python ------------------------------------------------------------###
##################################################################################################################################

while True:
    print('\nWelcome to our institute 🏫\n')
    print('1. Student\n2. Admin\n3. Exist\n')
    
    op = int(input('Enter your choice : '))
    
    if op == 1:
        while True:
            print('\n1. Registration\n2. Login\n3. Exist\n')
            
            op1 = int(input('Enter your choice : '))
            
            if op1 == 1:
                f_name = input("Enter your first name : ")
                l_name = input("Enter your last name : ")
                age = int(input('Enter your age : '))
                
                if age > 15:
                    admission(f_name, l_name, age)
                    studentid(f_name, l_name, age)
                
                else:
                    print('\nYou are under 15 ⬇️. Please try again later\n')
                    break
            
            elif op1 == 2:
                id = int(input('Enter your student id : '))
                
                if isregister(id) == None:
                    print('\nYou need first Registration\n')
                
                else:
                    print('\nWELCOME OUR INSTITUTE 🏫 \n')
                    while True:
                        print('1. My course\n2. Show all course\n3. Start new course\n4. Drop a course\n5. Exist\n')
                        
                        op2 = int(input('Enter your choice : '))
                        
                        # My course
                        if op2 == 1:
                            mycourse(id)
                        
                        # Show all course
                        elif op2 == 2:
                            print('\nNow aviable course are __________ \n')
                            showAllCourse()
                        
                        # Start new course
                        elif op2 == 3:
                            course_id = int(input('Enter course id, which you want to enroll : '))
                            
                            price = coursePrice(course_id)
                            
                            print(f"\nSend the amount of {price} TK \n")
                            submit = int(input('Send : '))
                            
                            if submit == price:
                                print('\nSuccessfully send money ✅\n')
                            
                                enrollCourse(id, course_id)
                            
                            else:
                                print('\nyou send wrong number of amount\n')
                        
                        # Drop a course
                        elif op2 == 4:
                            course_id = int(input('Enter a course id , tahat want to drop : '))
                            
                            dropCourse(id, course_id)
                        
                        # Exist
                        elif op2 == 5:
                            break
                        
                        else:
                            print("\nInvalid number ❌ please enter currect number\n")
            
            elif op1 == 3:
                print('\nThanks for Visiting Application 🔲\n')
                break
            
            else:
                print("\nInvalid number ❌ please enter currect number\n")

    
    elif op == 2:
        print('\nWELCOME OUR INSTITUTE 🏫 \n')
        while True:
            print('\n1. Add course\n2. Show all course\n3. Show registred but not enrolled\n4. Show all student\n5. Drop student\n6. Maximum enroll course\n7. Minimum enroll corse\n8. NOT enroll course anyone\n9. Exist')

            op3 = int(input('Enter your choice : '))
            
            # Add course
            if op3 == 1:
                course_name = input('Enter new course name : ')
                course_price = int(input('Enter course price: '))
                addNewCourse(course_name, course_price)
                        
            # Show all course
            elif op3 == 2:
                print('\nNow aviable course are __________ \n')
                showAllCourse()
                   
            # Show registred but not enrolled     
            elif op3 == 3:
                notenroll()
                      
            # Show all student            
            elif op3 == 4:
                showallstudent()
                      
            # Drop student            
            elif op3 == 5:
                stid = int(input('Enter student id, that you want to drop : '))
                dropstudent(stid)
            
            # Maximum enroll course            
            elif op3 == 6:
                maximumenrollcourse()
            
            # Minimum enroll corse            
            elif op3 == 7:
                minimumenrollcourse()
                
            
            # NOT enroll course anyone
            elif op3 == 8:
                noenroll()
            
            # Exist
            elif op3 == 9:
                break
                        
            else:
                print("\nInvalid number ❌ please enter currect number\n")
                
            
    elif op == 3:
        print('\nThanks for Visiting Application 🔲\n')
        break
    
    else:
        print("\nInvalid number ❌ please enter currect number\n")

    
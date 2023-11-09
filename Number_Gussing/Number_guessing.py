import random

##################################################################################################################################
### --------------------------------------------------- mysql connection ------------------------------------------------------###
##################################################################################################################################

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='***********',
    database='GussingNumber'
)

cursor = connection.cursor()


##################################################################################################################################
### -------------------------------------------- mysql query use by python ----------------------------------------------------###
##################################################################################################################################

# Registration a player at first one time in this game.
def addplayer(pname, pasrd):
    query = """
        INSERT INTO Players(name, passward)
        VALUES
        (%s, %s)
    """
    try:
        cursor.execute(query,(pname, pasrd))
        connection.commit()
        print('\nSuccessfully Registration complete ✅\n')
    except pymysql.Error as e:
        print(f"Invalid Age. Error: {e}")
        
# Check Rgisted player or not.    
def isregister(pname, pasrd):
    query = """
            SELECT playerid FROM Players
            WHERE name = %s AND passward = %s;
        """
    cursor.execute(query, (pname, pasrd))
    playerid = cursor.fetchone()
    return playerid
    

# When i complete a game then my game info save a database.
def addrecord(playerid, lower, upper, count):
    query = """
        INSERT INTO Record(playerid, lower_bound, upper_bound, try_count)
        VALUES
        (%s, %s, %s, %s)
    """
    try:
        cursor.execute(query,(playerid, lower, upper, count))
        connection.commit()
        print('\nSuccessfully complete Game ✅\n')
    except pymysql.Error as e:
        print(f"Error: {e}")
        
    

# FInd maximum Score in a player    
def find_max_score(a):
    query = """
        select lower_bound, upper_bound, try_count
        from record
        where playerid = %s AND ROUND(((upper_bound - lower_bound)/try_count)*100, 2) =
            (SELECT ROUND(MAX(((upper_bound - lower_bound)/try_count)*100), 2) FROM record Where playerid = %s);
    """

    try:
        cursor.execute(query, (a, a))
        max_data = cursor.fetchone()
        
        print('\nlower_lound || upper_bound || try_count\n')
        for i in max_data:
            print(i, end=" \t\t")
        print()
        
    except pymysql.Error as e:
        print(f'Error: {e}')
        
        

# FInd all the result in a player        
def playing_statistics(a):
    query = """
        select lower_bound, upper_bound, try_count
        from record
        where playerid = %s;
    """

    try:
        cursor.execute(query, a)
        all_data = cursor.fetchall()
        
        print('\nlower_lound || upper_bound || try_count\n')
        for i in all_data:
            for j in i:
                print(j, end=" \t\t")
            print()
        
    except pymysql.Error as e:
        print(f'Error: {e}')
    
    
    
##################################################################################################################################
### ------------------------------------------------------- python ------------------------------------------------------------###
##################################################################################################################################

while True:
    print('\nWelcome to Number guessing game 🧠 \n1. Registration \n2. Login \n3. Exist\n')
    
    op = int(input('Enter your choice : '))
    
    # Registration
    if op == 1:
        print('\nWelcome for Registration\n')
        pname = input('Enter your name : ')
        pasrd = input('Enter your passward: ')
        
        addplayer(pname, pasrd)
    
    # Login
    elif op == 2:
        print('\nWelcome to Number Guessing game\n')
        pname = input('Enter your name : ')
        pasrd = input('Enter your passward: ')
        
        login = isregister(pname, pasrd)
        
        # if player are not registed. At first you need Registration
        if login == None:
            print('\nYou need first Registration\n')

        # If player already registed . Then login and start play
        else:
            print('\nSuccessfully login your number_gussing account\n')
           
           
            while True:
                print("Welcome to Number guessing game 🧠 \n1. Start game\n2. Max Score\n3. All game record\n4. Exist\n")
                op = int(input('Enter your choice: '))
                
                # start game
                if op == 1:
                    print('\nEnter the range of your guessing numeber for play game\n')
                    lower = int(input('Enter lower bound: '))
                    upper = int(int(input('Enter upper boud: ')))

                    # Generating random number between the lower bound and upper bound
                    # randint generate integer random number
                    number = random.randint(lower, upper)

                    count = 0

                    print('\n--------------------> Start game <--------------------\n')
                    while True:
                        count+=1
                        
                        guess = int(input('Enter your guessing number : '))
                        
                        if guess == number:
                            print(f"\n🏆Congratulations you win the game in {count} try🏆\n")
                            
                            # Save record in database
                            playerid = login[0]
                            addrecord(playerid, lower, upper, count)
                            
                            count = 0
                            break
                        
                        elif guess < number:
                            print('\nYou guessed too small number🤏 Try again\n')
                        
                        elif guess > number:
                            print('\nYou guessed to high number👆 Try again\n')
                
                
                # Show Maximum Score
                elif op == 2:
                    print('\nMy Maximum score is_______________\n')
                    a = login[0]
                    find_max_score(a)
                
                
                # Show all playing statistics in game
                elif op == 3:
                    print('\nMy All playing statistics is_______________\n')
                    a = login[0]
                    playing_statistics(a)
                
                
                # Quit game
                elif op == 4:
                    print('\nThanks for playing game 🔲\n')
                    break
                
                # oops Press Wrong choice
                else:
                    print('\nInvalid number ❌\n')
    
    
    # Exist app           
    elif op == 3:
        print('\nThanks for Visiting game 🔲\n')
        break
    
    # OOPS press wrong choice
    else:
        print("\nInvalid number ❌\n")



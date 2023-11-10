##################################################################################################################################
### --------------------------------------------------- mysql connection ------------------------------------------------------###
##################################################################################################################################


import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='***********',
    database='BankTrainsaction'
)


cursor = connection.cursor()



##################################################################################################################################
### -------------------------------------------- mysql query use by python ----------------------------------------------------###
##################################################################################################################################

# Create Bank account    
def createaccount(account_number, passward, name, phone_number, age):
    query = """
        insert into Users(Account_number, Passward, Name, Phone_number, Age, Balance)
        values
        (%s, %s, %s, %s, %s, 00);
    
    """
    
    cursor.execute(query, (account_number, passward, name, phone_number, age))
    connection.commit()
    
    print('\nSuccessfully create your bank account ✅\n')



# check account registed or not
def checkregisted(account_number, passward):
    query = """
        SELECT User_id
        FROM Users
        WHERE Account_number = %s AND Passward = %s;
    """
    
    cursor.execute(query, (account_number, passward))
    
    print('\nSuccessfully login your account ✅\n')
    data = cursor.fetchone()
    return data


# Check balance
def checkbalance(account_number, user_id):
    query = """
        SELECT Balance
        FROM Users
        WHERE Account_number = %s AND User_id = %s;
    """
    
    cursor.execute(query, (account_number, user_id))
    
    data = cursor.fetchone()
    print(f'\nYour current balance is : {data[0]}\n')

# ADD Transaction
def addtransaction(user_id, account_number, amount):
    query = """
        INSERT INTO trainsaction(User_id, Account_number, Amount, Transfer_Date)
        VALUES
        (%s, %s, %s, CURRENT_DATE());
    """

    cursor.execute(query, (user_id, account_number, amount))
    connection.commit()
    



                
# Transaction History
def transactionhistory(user_id, account_number):
    query = """
        SELECT *
        FROM trainsaction
        WHERE User_id = %s AND Account_number  = %s;
    """
    cursor.execute(query, (user_id, account_number))
    alldata = cursor.fetchall()
    
    print('\nTransction_id || User_id ||  Account_number ||  Transfer_Date  ||  Amount\n')
    for i in alldata:
        for j in i:
            print(j, end='\t\t')
        print()
    print()


                
# Deposit / Withdraw
def transfermoney(amount, user_id, account_number):
    query = """
        UPDATE Users
        SET Balance = Balance + %s
        WHERE User_id = %s AND Account_number = %s;
    """

    cursor.execute(query, (amount, user_id, account_number))
    connection.commit()
    
    print('\nSuccessfully Transfer your balance ✅\n')
    

# FInd user ID
def finduserid(reciver_number):
    query = """
        SELECT User_id
        FROM Users
        WHERE Account_number = %s;
    
    """
    cursor.execute(query, (reciver_number))
    
    data = cursor.fetchone()
    
    return data[0]
    
    

##################################################################################################################################
### ------------------------------------------------------- python ------------------------------------------------------------###
##################################################################################################################################



while True:
    print('\nWelcome to ABC Bank 🏦\n')
    
    print('\n1. Create Account\n2. Login\n3. Exist\n')
    
    op = int(input('Enter your choice : '))
    
    if op == 1:
        account_number = int(input('Enter your account number : '))
        passward = int(input('Enter your passward : '))
        name = input('Enter your full name : ')
        phone_number = input('Enter your phone number : ')
        age = int(input('Enter your age : '))
        
        if age < 18:
            print('\nYou are under 18. Try again later\n')
        
        # Create Bank account    
        else:
            createaccount(account_number, passward, name, phone_number, age)
    
    elif op == 2:
        account_number = int(input('Enter your account number : '))
        passward = int(input('Enter your account passward : '))
        
        # check account registed or not
        value = checkregisted(account_number, passward)
        
        if value == None:
            print('\nYou need first create a bank account ⭕\n')
        
        else:
            while True:
                print('\n1. Check balance\n2. Send money\n3. Transaction History\n4. Deposit\n5. Withdraw\n6. Exist\n')
                
                user_id = value[0]
                op1 = int(input('Enter your choice : '))
                
                
                # Check balance
                if op1 == 1:
                    checkbalance(account_number, user_id)
                
                # Send money
                elif op1 == 2:
                    reciver_number = int(input('Enter reciver account number : '))
                    
                    uid = finduserid(reciver_number)
                    
                    amount = int(input('Enert your amount how much you want to send : '))
                    
                    # recive money
                    transfermoney(amount, uid, reciver_number)
                    addtransaction(uid, reciver_number, amount)
                    
                    # send money
                    amount = amount * (-1)
                    transfermoney(amount, user_id, account_number)
                    addtransaction(user_id, account_number, amount)
                
                # Transaction History
                elif op1 == 3:
                    transactionhistory(user_id, account_number)
                
                # Deposit
                elif op1 == 4:
                    amount = int(input('Enter your amount how much you want to deposit : '))
                    
                    if amount <= 0:
                        print('\nPlease deposit a valid amount of money 💵\n')
                    else:
                        transfermoney(amount, user_id, account_number)
                        addtransaction(user_id, account_number, amount)
                
                # Withdraw
                elif op1 == 5:
                    amount = int(input('Enter your amount how much you want to deposit : '))
                    
                    if amount <= 0:
                        print('\nPlease deposit a valid amount of money 💵\n')
                    else:
                        amount = amount * (-1)
                        transfermoney(amount, user_id, account_number)
                        addtransaction(user_id, account_number, amount)
                
                elif op1 == 6:
                    print('\nThanks for visiting your account\n')
                    break
                
                else:
                    print('\nYou press invalid choice option ❌ Please try again \n')
    
    elif op == 3:
        print('\nThanks for visiting ABC Bank 🏦\n')
        break
    
    else:
        print('\nYou press invalid choice option ❌ Please try again \n')
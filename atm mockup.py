from datetime import datetime as dt
from random import randint


print('Welcome to Oluwarotimi bank!')

pass
total = 0


print('\nPlease enter Numerical Digits')
print('\nThese are the available options: ')
print('1. Withdraw')
print('2. Cash Deposit')
print('3. Complaint')
print('4. Open account')
print('5. Monthly commision after deposit')


#Login function for login
def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start , range_end)

#account number generation


   
def account_details():
    account_name = input('What is your name?')
    account_info = input('What is your DOB?')
    account_info_location = input('What is your Nationality and state of origin?')
    account_number = random_digits(10)
    print(account_number)
    
def login_details():
    username = input("What is your name? \n")
    allowedUsers = ["Samuel", "Bukunmi", "Esther"]
    allowedPassword = ['passwordSam', 'passwordIbk', 'passwordEst']
    total = 0

    if(username in allowedUsers):
        password = input("Your password? \n")
        userId = allowedUsers.index(username)

        if(password == allowedPassword[userId]):
            print('\nWelcome %s \n' % (username))

        else:
            print('password incorrect')
    



            print(dt.strftime(dt.now(), '''Date: %DTime: %T'''))

    
       

selectedOption = int(input('Please select an option:\n'))

if (selectedOption == 1):
    login_details()
    value = input('How much would you like to withdraw\n')
    print('take your cash')

elif (selectedOption == 2):
    login_details()
    value = float(input('How much would you like to deposit?\n'))
    print('Balance is ', (total + value))

elif (selectedOption == 3):
    login_details()
    value = input('What issue will you like to report?\n')
    print('Thank you for contacting us')
    
elif (selectedOption == 4):
    account_details()
elif(selectedOption == 5):
    monthly_interest = total*8.20
    print(monthly_interest)
    
else:
    print('Invalid Option selected, please try again')






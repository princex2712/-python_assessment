"""

Q - Write a program to demonstrate the bank management Console based application
    Prepare demonstration of Python bank management under software
    development principles and follow coding protocols
    To implement application using of control statements as well as
    collection concept
    In this application 2 modules involved (Banker , Customer)
    Execution of the code following menu must be displayed.
    Make sure each business logic is denoted with appropriate comments and
    make your code interactive and represent clean and clear output on your
    console screen.

"""
#importing module 
from Bank_management_console import banker,customer

#Taking input from user and printing instruction 
print('\n\n'+'WELCOME TO PYTHON BANK MANAGEMENT SYSTEM'.center(60)+'\n\n'+'Select Your Role: ')
print('\n'+'1)Banker'.center(60))
print('2)Customer'.center(61)+'\n')
print('3)Exit'.center(58))
user_role = int(input('\n'+'Choose Your Role(1,2 or 3): '))

#calling function based on input
match user_role :
    case 1:
        banker.welcome()
    case 2:
        customer.welcome()
    case 3:
        exit()
    case  _:
        print('Invalid Choice')
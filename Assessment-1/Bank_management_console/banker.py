from datetime import datetime # importing datetime funtion to get date and time for opening date log

# creating dictionary to store data of customer
customer_data = {101:{'name':'Prince Patel','balance':1000000,'opening_date':''}}


# creating funtion for menu and taking input for choice
def welcome():
    print('\n'+'WELCOME TO BANKER\'S  APP'.center(60)+'\n')
    print('Operation Menu As Follows:\n')
    print('1)Add Customer'.center(50)+'\n'+'2)Search Customer'.center(54)+'\n'+'3)View All Customer'.center(56)+'\n'+'4)Total Amount in bank'.center(58))
    banker_choice = int(input('Choose Operation: '))
    operation(banker_choice)

# funtion to check account number is unique or not
def is_account_number_unq(num):
    return num not in customer_data

# function to search user and retrieve desired customer data
def search_customer():
    acc_no = int(input('Enter Customer Account Number:'))
    for i in customer_data:
        if i == acc_no:
            print('\nAccount Number:{}\nCustomer Name:{}\nBalance:{}\nOpening-Date:{}'.format(i,customer_data.get(i).get('name'),customer_data.get(i).get('balance'),customer_data.get(i).get('opening_date')))

# funtion to create new user account
def add_account():
    account_num = int(input('Enter Account Number: '))
    if is_account_number_unq(account_num):
        customer_name = input('Enter Customer Name: ')
        opening_balance = int(input('Enter Opening Balance: '))
        customer_data[account_num] = {'name':customer_name.title(),'balance':opening_balance,'opening_date':datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    else:
        print('*ACCOUNT NUMBER ALREADY EXIST RESTARTING OPERATION!*')
        operation(1)

# funtion to view all customer and their detail
def view_all_customer():
    for i in customer_data:
        print('\nAccount Number:{}\nCustomer Name:{}\nBalance:{}\nOpening-Date:{}\n'.format(i,customer_data.get(i).get('name'),customer_data.get(i).get('balance'),customer_data.get(i).get('opening_date')))

# funtion to get total amount in bank
def total_amount():
    return sum([val.get('balance') for i,val in customer_data.items()])

# calling function based on bankers input
def operation(choice):
    match choice:
        case 1:
            add_account()
        case 2:
            search_customer()
        case 3:
            view_all_customer()
        case 4:
            print(total_amount())
        case _:
            print('Invalid Operation')
    
    # taking input about want to continue or want to exit
    other_operation = input('Do You want to perform another operation \'y\' for Yes and \'n\' for No: ')
    if other_operation.lower() == 'y':
        welcome()
    else:
        None
    
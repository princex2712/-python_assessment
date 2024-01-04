from . import banker

def welcome():
    print('\n'+'WELCOME TO CUSTOMERS\'S  APP'.center(60)+'\n')
    print('Operation Menu As Follows:\n')
    print('1)Withdraw Amount'.center(50)+'\n'+'2)Deposite Amount'.center(50)+'\n'+'3)View Balance'.center(46)+'\n')
    customer_choice = int(input('Choose Operation: '))
    operation(customer_choice)

def withdraw(acc_no):
    if acc_no in banker.customer_data.keys():
        withdraw_amount = int(input('Enter Withdraw Amount:'))
        if withdraw_amount > banker.customer_data[acc_no].get('balance'):
            print('Withdraw Amount is larger than Account Balance, Re-Enter Withdraw Amount!')
            withdraw(acc_no)
        else:
            banker.customer_data[acc_no]['balance'] -= withdraw_amount
            print('Updated Balance: ',end='')
            print(banker.customer_data[acc_no].get('balance'))
    else:
        print('ACCOUNT NUMBER NOT FOUND RE-ENTER ACCOUNT NUMBER:')
        operation(1)

def deposite(acc_no):
    if acc_no in banker.customer_data.keys():
        deposite_amount = int(input('Enter Deposite Amount:'))
        if deposite_amount <= 0:
            print('Deposite Amount is should be above 0, Re-Enter Deposite Amount!')
            deposite(acc_no)
        else:
            banker.customer_data[acc_no]['balance'] += deposite_amount
            print('Updated Balance: ',end='')
            print(banker.customer_data[acc_no].get('balance'))
    else:
        print('ACCOUNT NUMBER NOT FOUND RE-ENTER ACCOUNT NUMBER:')
        operation(2)

def view_balance(acc_no):
    return banker.customer_data[acc_no]['balance']

def operation(customer_choice):
    acc_no = int(input('Enter Your Account No:'))
    match customer_choice:
        case 1:
            withdraw(acc_no)
        case 2:
            deposite(acc_no)
        case 3:
            print(view_balance(acc_no))
        case _:
            print('Invalid Operation')
    other_operation = input('Do You want to perform another operation \'y\' for Yes and \'n\' for No: ')
    if other_operation.lower() == 'y':
        welcome()
    else:
        None

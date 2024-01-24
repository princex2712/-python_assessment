from .connect_db import cursor

# Create Table to store the data in Database
def create_table():
    table_name = input("Enter Your Table Name: ")
    fields_config = ''
    first_flag = True 
    final_flag = True

    while final_flag:
        yn = input("Want to field: ")
        if yn.lower() == 'y':
            if first_flag:
                field = input("Enter First Field Configuration: ")
                first_flag = False
            else:
                field = input("Enter New Field Configuration: ")
            fields_config += field
        else:
            final_flag = False
    
    create_table_query = f"CREATE TABLE {table_name} ({fields_config})"
    cursor.execute(create_table_query)


# from .models import AppUser
import json
import mysql.connector 
import datetime

# connect to db
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="nicolas",
    password="password",
    database="chat_app_db"
    )


# Create your tests here.
def createUserMockData(cursor):
    
    with open("mock_data_user.json", "r") as f:
        data = json.load(f)
        
    # print(data[0])
    # return data
    
    # sql = "insert into auth_user (username, first_name, last_name, email, password, phone_number, bio, is_superuser, is_staff, is_active, date_joined) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql = "insert into user_appuser (username, first_name, last_name, email, password, phone_number, bio, is_superuser, is_staff, is_active, date_joined) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    for row in data:
        values_dict = row
        
        # add the values to the user table
        values_tuple = (values_dict["username"], values_dict["first_name"], values_dict["last_name"], values_dict["email"], values_dict["password"], values_dict["phone_number"], values_dict["bio"], False, False, True, datetime.datetime.now())
        my_cursor.execute(sql, values_tuple)
        for x in my_cursor:
            print(x)
    
    
    
    
# db cursor
my_cursor = mydb.cursor()
# my_cursor.execute("show tables")


# open mock data
createUserMockData(my_cursor)

# my_cursor.execute("show tables")
# make sure that the changes were applied
for x in my_cursor:
    print(x)
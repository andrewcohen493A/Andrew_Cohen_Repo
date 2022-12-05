"""
SQL Injection Example

"""
from In_Class_Practices import DBConnector as DBC

# Connect to DB
my_db = DBC.MyDB()


def CreateTablesAndFillData():
    """
    This creates one table (users) and inserts three rows, each represents a username and a password.
    """

    # Your code goes here.
    # my_db.query('CREATE TABLE AndrewCohen_users(Username VARCHAR, Password VARCHAR, Admin Boolean)', '')

    users = ["User1", "User2", "User3"]
    password = ["Pass1", "Pass2", "Pass3"]
    admin = ["true", "false", "false"]

    counter = 0
    while counter < len(users):
        command = 'INSERT INTO AndrewCohen_users VALUES(%s,%s,%s)'
        my_db.query(command, (users[counter], password[counter], admin[counter],))
        counter = counter + 1

    # 3. Test whether table has been created and has data using SQL: SELECT * FROM [Table_Name].

    data = my_db.query('SELECT * FROM AndrewCohen_users', '')
    print(data)


    # my_db.query('DROP TABLE AndrewCohen_users;', '');


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    # Create the table and add data
    CreateTablesAndFillData()


if __name__ == "__main__":
    main()
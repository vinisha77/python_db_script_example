import pyodbc

# Database connection details
server = 'vaishaliserver.database.windows.net'
database = 'vaishalidb'
username = 'vaishaliadmin'
password = '*******'  # Ideally, use a secure way to handle passwords
driver = '{ODBC Driver 17 for SQL Server}'

# Establish connection
connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful")

    # Create a table and insert some data
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE Persons (
        PersonID int,
        LastName varchar(255),
        FirstName varchar(255),
        Address varchar(255),
        City varchar(255)
    )
    ''')

    cursor.execute('''
    INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
    VALUES
    (1, 'Smith', 'John', '123 Main St', 'New York'),
    (2, 'Doe', 'Jane', '456 Maple Ave', 'Los Angeles')
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print("Table created and data inserted successfully")

except Exception as e:
    print("Error connecting to database:", e)

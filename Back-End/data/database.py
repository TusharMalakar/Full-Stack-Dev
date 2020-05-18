import pyodbc

connection = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-Q87HICN\SQLEXPRESS;'
    'DATABASE=tweeter-db;'
    'Trusted_Connection=Yes'
)

cursor = connection.cursor()
accounts = cursor.execute('select * from [dbo].[Account]').fetchall()

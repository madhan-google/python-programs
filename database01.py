import pyodbc
con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=C:\Users\ELCOT\Documents\Database1.accdb')
cursor = con.cursor
cursor.execute('select *from Database1')
for row in cursor.fetchall():
      print(row)

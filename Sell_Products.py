import sqlite3


conn = sqlite3.connect("Products.db")
c = conn.cursor()
fetch = c.execute("SELECT * FROM Retail_Products WHERE Product_Name='PARA'")
result = fetch.fetchall()

print(result[0][0])
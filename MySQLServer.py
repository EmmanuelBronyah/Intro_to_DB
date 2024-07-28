import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

try:
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=os.getenv("password"),
  )

  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
  print(f"Database 'alx_book_store' created successfully!")

  mycursor.close()
  mydb.close()

except Exception as e:
  print(e)
  
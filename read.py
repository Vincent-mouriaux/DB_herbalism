import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Selene Mouriaux",
  passwd="santoryu",
  database="herbalism"
)
pointer = mydb.cursor()
pointer.execute("")


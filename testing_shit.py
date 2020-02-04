"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Selene Mouriaux",
    passwd="santoryu",
    database="herbalism"
)

pointer = mydb.cursor()

pointer.execute("SELECT nom, indication FROM plante WHERE nom LIKE '%ai%'")
myresult = pointer.fetchall()

#for x in myresult:
print(myresult)


mylist = ['spam', 'ham', 'eggs']

print(', '.join(mylist))
"""

x = list(input("Enter a multiple value: ").split())
print("List of students: ", x)

# Select indication, round(AVG(price), 2) from plant group by indication
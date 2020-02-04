import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='Selene Mouriaux',
    passwd='santoryu',
    database='herbalism'
)

mycursor = mydb.cursor()

def menu():
    choix = input("\nVeuillez sélectionner une option : \n(L)ister les plantes de la DB \n" \
                  + "(A)jouter une plante à la liste \n(S)upprimer une plante (par son Id) \n" \
                  + "(C)hercher une plante \n(Q)uitter \n(I)ndiquer la sous classe de la plante ")
    return choix

def list_plants():
    mylist = []
    mycursor.execute("SELECT id, nom FROM plante")
    myresult = mycursor.fetchall()
    for x in myresult:
        x = ''.join(str(x))
        mylist.append(x)
    print("La liste de mes plantes est composée de :\n {}.".format(', '.join(mylist)))

def add_plant():
    nom = input("Quel est le nom de la nouvelle plante ? ")
    indication = input("Donnez une indication sur la plante : ")
    partie_utilisee = input("Quelle est la partie utilisée de la plante ? ")
    prix = float(input("Enfin, quel est son prix ? "))
    sql = "INSERT INTO plante (nom, indication, partie_utilisee, prix) VALUES (%s, %s, %s, %s);"
    val = [nom, indication, partie_utilisee, prix]
    mycursor.execute(sql, val)
    mydb.commit()

def delete_plant():
    sql = "DELETE FROM plante WHERE id = %s"
    val = (int(input("Veuillez saisir l'ID de la plante que vous voulez supprimer de la liste : ")), )
    mycursor.execute(sql, val)
    mydb.commit()

def lookfor_plant():
    val = (input("Tapez votre recherche : "), )
    sql = "SELECT id, nom from plante where nom like CONCAT('%', %s, '%') order by nom, prix limit 3;"
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(myresult)

def sub_class():
    plant_id = input("Tapez l'id de votre recherche : ")
    sql = "SELECT plant.name, underclass.name_fr from plant JOIN family on plant.family_id = family.id" \
          " JOIN underclass on family.underclass_id = underclass.id WHERE plant.id = %s"
    mycursor.execute(sql, (plant_id, ))
    result = mycursor.fetchall()[0]
    print("La plante d'Id {} est {} de la sous classe {}.".format(plant_id, result[0], result[1]))

while True:
    choix = menu()
    if choix.upper() == "L":
        list_plants()
    elif choix.upper() == "A":
        add_plant()
    elif choix.upper() == "S":
        delete_plant()
    elif choix.upper() == "C":
        lookfor_plant()
    elif choix.upper() == "I":
        sub_class()
    elif choix.upper() == "Q":
        exit()

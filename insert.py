import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Selene Mouriaux",
  passwd="santoryu",
  database="herbalism"
)
pointer = mydb.cursor()
"""
#pointer.execute("ALTER TABLE plante AUTO_INCREMENT = 1;")
pointer.execute('INSERT INTO plante(nom, indication, partie_utilisee, prix) VALUES' 
                '("Menthe poivrée", "Anesthésiant", "feuiles", 3), '
                '("Absinthe", "Antiseptique", "feuiles", 4), '
                '("Ail", "Antiseptique", "feuiles", 1), '
                '("Basilic", "Antiseptique", "feuiles", 5), '
                '("Carotte", "Digestion", "feuiles", 2.2), '
                '("Aigremoine", "Digestion", "feuiles", 5.4), '
                '("Ronce", "Digestion", "feuiles", 3.21), '
                '("Linaire commune", "Diurétique", "feuiles", 1.12), '
                '("Mélilot officinal", "Diurétique", "feuiles", 13.22);')
"""
pointer.execute("UPDATE plante SET partie_utilisee = 'feuilles' WHERE partie_utilisee = 'feuiles';")


mydb.commit()
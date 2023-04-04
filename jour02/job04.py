import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789",
  database="laplateforme"
)

# Récupération des données de la table "salles"
mycursor = mydb.cursor()
mycursor.execute("SELECT nom, capacite FROM salles")
result = mycursor.fetchall()

# Affichage des résultats
for row in result:
  print(row[0], "-", row[1])

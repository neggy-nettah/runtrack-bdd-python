import mysql.connector 

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Malika1959!',
    database = "LaPlateforme"
)

cursor = db.cursor()
requete = 'SELECT * FROM etudiants' 
cursor.execute(requete)
datas = cursor.fetchall()

print(datas)
cursor.close()
 

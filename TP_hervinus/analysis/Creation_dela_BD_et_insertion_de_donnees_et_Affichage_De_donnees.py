import mysql.connector
from mysql.connector import errorcode
import pandas as pd

# Configuration de la connexion MySQL
config = {
    'user': 'root',
    'password': '', 
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

try:
    # Connexion au serveur MySQL
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("Connexion réussie au serveur MySQL!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nom d'utilisateur ou mot de passe incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
    else:
        print(err)

# Création de la base de données
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS Bd_Dataliner")
    cursor.execute("USE Bd_Dataliner")
    print("Base de données 'Bd_Dataliner' sélectionnée!")
except mysql.connector.Error as err:
    print(f"Erreur lors de la création de la base de données: {err}")

# Création de la table
table_creation_query = """
CREATE TABLE IF NOT EXISTS data (
    ID_Employe INT PRIMARY KEY,
    Age INT,
    Experience INT,
    Salaire FLOAT,
    Satisfaction FLOAT,
    Departement VARCHAR(255),
    Taux_Absentéisme FLOAT,
    Performance VARCHAR(255),
    Taux_Turnover FLOAT
)
"""

try:
    cursor.execute(table_creation_query)
    print("Table 'data' créée avec succès!")
except mysql.connector.Error as err:
    print(f"Erreur lors de la création de la table: {err}")

# Lecture des données JSON
data = pd.read_json('/mnt/data/data.json')

# Insertion des données dans la table
for _, row in data.iterrows():
    try:
        cursor.execute("""
            INSERT INTO data (ID_Employe, Age, Experience, Salaire, Satisfaction, Departement, Taux_Absentéisme, Performance, Taux_Turnover)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['ID_Employe'], row['Age'], row['Experience'], row['Salaire'], row['Satisfaction'],
            row['Departement'], row['Taux_Absentéisme'], row['Performance'], row['Taux_Turnover']
        ))
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'insertion des données: {err}")

# Commit des transactions et fermeture de la connexion
cnx.commit()
cursor.close()
cnx.close()
print("Données insérées avec succès et connexion fermée!")

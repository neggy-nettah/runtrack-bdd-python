mysql> SELECT * FROM etudiants WHERE nom = (SELECT nom FROM etudiants WHERE nom = 'Dupuis' AND prenom = 'Gertrude');

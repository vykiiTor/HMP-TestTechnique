# HMP-TestTechnique
Repository du test technique pour HeadMind Patners

## Installation du projet en local :

1. Cloner le projet

```bash
git clone https://github.com/vykiiTor/HMP-TestTechnique.git
```

2. Rester dans le directory root du projet

```bash
cd  HMP-TestTechnique
```

3. Installer FastAPI et Sqlite

```bash
 pip install "fastapi[standard]"   
```

4. Lancer la base de données depuis root

```bash
 python -m backend.db_init    
```
5. Lancer le backend depuis root

```bash
 fastapi run backend/main.py
```
6. Lancer le frontend

```bash
cd frontend
npm install
npm run
```

6. Aller sur `http://localhost:3000`

### Routes :

Pour le swagger : http://0.0.0.0:8000/docs 

### Features faites :
Backend fait avec persistance des données.   
3 endpoints pour GET, POST, PUT   
Validation des champs pour les formulaires (typage seulement)  
Front basic et responsive avec MUI

### Features à faire
Améliorer le front avec des % plus précis pour le fait responsive   
Vérification des champs pour les formulaires avec des objets en plus des types   
Bonus...

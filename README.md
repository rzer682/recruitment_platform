Description du projet:

Ce projet demander par le CTO à Ari-Mayi vise à développer une API REST avec Django et Python pour une plateforme de recrutement. 
L'API permet de gérer les informations des candidats et des recruteurs, tout en offrant une documentation accessible via Swagger.

  Fonctionnalités principales:

    1) Modélisation des données avec Django et stockage dans une base PostgreSQL.

    2) Endpoints API pour :
      -Les candidats : création, consultation, et mise à jour de leurs informations personnelles.
      -Les recruteurs : consultation des informations des candidats.
      -Les offres d'emploies: créatoin, consultation et mis à jour (si permission) et filtrage.
      -Les entreprises: création, consultation mis à jour.
      -Les candidatures:  créatoin, consultation et mis à jour (si permission)

    3) Documentation API interactive via Swagger/OpenAPI.


  Comment cloner le projet ? 

    1) Ouvrir le terminal et introduire => git clone https://github.com/votre-repo/recruitment-platform.git et se rendre sur le bon directory avec => cd recruitment-platform
    2) Créer et activer un environnement virtuel => python -m venv env (création) ; env\Scripts\activate (activation Windows)
    3) Installer les dépendances => pip install -r requirements.txt
    4) Configurer la base de données =>

         DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'recruitment_db',
                'USER': 'votre_utilisateur',
                'PASSWORD': 'votre_mot_de_passe',
                'HOST': 'localhost',
                'PORT': '5432',
              }
            }

    5)  Appliquer les migrations => python manage.py makemigrations et ensuite, python manage.py migrate
    6)  Lancer le serveur => python manage.py runserver

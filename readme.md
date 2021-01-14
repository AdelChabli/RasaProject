# Projet chat bot sous Rasa et interaction avec Nao

## Utilisation
L'utilisation de python 3.7 est obligatoire pour Rasa.

Pour pouvoir utliser le projet il est necessaire de lancer un serveur Rasa et ses actions:
    
    rasa run --enable-api --cors "*" --debug
    cd actions/
    rasa run actions

Ainsi que l'ASR necessaire à la transcription des fichiers audio:
    
    cd ServerAux
    python googleSR_server.py

Le script permettant de lancer la routine pour l'utilisation du Nao avec le serveur Rasa se trouve dans le dossier Choregraphe.
Pense à mettre l'ip de la machine qui héberge les serveurs.

## Fonctionnalité du chatbot

Projet universitaire permettant de mettre un place un chatbot relié à l'API de l'université
du CERI d'Avignon permettant l'exécution d'action comme :

    * Donner l'emploi du temps à une date donnée
    * Donner le nom des salles disponibles 
    * Donner le chemin de l'entré du CERI jusqu'à une salle
    
## Groupe

Adel CHABLI - M2 ILSEN-CLA

Léo SALADIN - M2 ILSEN-CLA

## Github

    https://github.com/AdelChabli/RasaProject
#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

def obtenir_progression_todo_employee(id_employe):
    # Point de terminaison de l'API
    base_url = 'https://jsonplaceholder.typicode.com'
    url_todo = f'{base_url}/todos?userId={id_employe}'

    # Obtenir la liste de tâches de l'employé
    reponse = requests.get(url_todo)

    if reponse.status_code == 200:
        todos = reponse.json()
        reponse_utilisateur = requests.get(f"{base_url}/users/{id_employe}")
        info_utilisateur = reponse_utilisateur.json()

        # Filtrer les tâches terminées
        taches_terminees = [tache for tache in todos if tache['completed']]
        nombre_taches_terminees = len(taches_terminees)
        nombre_total_taches = len(todos)

        # Afficher l'avancement de l'employé
        print(f"L'employé {info_utilisateur['name']} a terminé {nombre_taches_terminees}/{nombre_total_taches} tâches :")
        print(f"Nom de l'employé : {info_utilisateur['name']}")
        print(f"Nombre de tâches terminées : {nombre_taches_terminees}")
        print(f"Nombre total de tâches : {nombre_total_taches}")
        
        if nombre_taches_terminees > 0:
            print("Tâches terminées :")
            for tache in taches_terminees:
                print(f"\t{tache['title']}")
    else:
        print("Impossible de récupérer les données. Veuillez réessayer plus tard.")

# Vérifier si l'argument (ID de l'employé) est passé en ligne de commande
if len(sys.argv) != 2:
    print("Veuillez fournir l'ID de l'employé en argument.")
else:
    employee_id = int(sys.argv[1])
    obtenir

import requests

def salleLibre(duree, heureDebut, date):
    url = "https://edt-api.univ-avignon.fr/app.php/api/salles/disponibilite?site=CERI&duree=" + duree + "&debut=" + heureDebut + "&date=" + date
    sallelibre = requests.get(url).json()
    response = ""

    if sallelibre["results"] == "":
        response = "Le " + date + " à " + heureDebut + "h pour une durée de " + duree + "h aucune salle n'est disponible"
    else:
        response += "Voici les salles disponible pour le " + date + " à " + heureDebut + "h pour une durée de " + duree + "h :"
        for salle in sallelibre["results"]:
            response += "\nSalle " + salle['libelle']

    return response
# print(salleLibre("3","10.30","2020-11-17"))

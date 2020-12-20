import requests as rq
from datetime import datetime
import actions.utilFunction as uti

url = "https://edt-api.univ-avignon.fr/app.php/api/"


def free_room(duration, start, date):
    new_dt = date.strftime("%Y-%m-%d")

    tz = int(date.strftime("%z")[1:3])  # format ==>   +0100  convert to int("01")

    dur = uti.rm_hour(duration)
    h_start = uti.rm_hour(start)

    h_start = str(int(h_start[:h_start.find('.')]) - tz) + h_start[h_start.find('.'):]

    new_url = url + "salles/disponibilite?site=CERI&duree=" + dur + "&debut=" + h_start + "&date=" + new_dt
    room_free = rq.get(new_url).json()
    response = ""

    new_dt = new_dt.replace("-", " ")
    h_start = uti.add_hour(h_start)
    dur = uti.add_hour(dur)

    # TODO format date to more verbal

    if room_free["results"] == "":
        response = "Le " + new_dt + " à " + h_start + " pour une durée de " + dur + " aucune salle n'est disponible"
    else:
        response += "Voici les salles disponible pour le " + new_dt + " à " + h_start + " pour une durée de " + dur + " :"
        for room in room_free["results"]:
            room_name = room['libelle'][:room['libelle'].find('=') - 1]

            if "cisco" in room_name or "elec" in room_name:
                response += ", salle " + room_name
            else:
                response += ", " + room_name

    return response


duration = " 3 heure"
hour_start = "14 heure 30"
date = datetime.now().astimezone()

print(free_room("3 heure", "8h30", date))

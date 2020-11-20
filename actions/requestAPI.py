import requests as rq
from datetime import datetime

url = "https://edt-api.univ-avignon.fr/app.php/api/"


def getCodeBySection(section, spec):
    newUrl = url + "elements"
    request = rq.get(newUrl).json()
    response = ""

    for row in request['results']:
        if row['letter'] == "INFORMATIQUE":
            for e in row['names']:
                if section in e['name'] and spec in e['name']:
                    #print(e['name']+" "+e['code'])
                    response = e['code']
    return response


def get_group_by_section(section, spec):
    newUrl = url + "tdoptions/" + getCodeBySection(section, spec)
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)

    return response


def getCurrentLesson(section, spec, current_dt):
    newUrl = url + "events_promotion/" + getCodeBySection(section,spec)
    request = rq.get(newUrl).json()
    response = ""

    for row in request['results']:

        dt_start = datetime.strptime(row['start'][0:19], "%Y-%m-%dT%H:%M:%S%z")
        dt_end = datetime.strptime(row['end'][0:19], "%Y-%m-%dT%H:%M:%S%z")

        if dt_start <= current_dt < dt_end:
            # print("INFO ==> "+dt_start.strftime("%Y-%m-%dT%H:%M:%S")+" / "+current_dt.strftime("%Y-%m-%dT%H:%M:%S")+"/"+dt_end.strftime("%Y-%m-%dT%H:%M:%S"))
            # print(row['title'])
            response = row['title']

        lastRow = row
    return response


def getScheduleByPromo(section, spec, current_dt):
    newUrl = url + "events_promotion/" + getCodeBySection(section, spec)
    request = rq.get(newUrl).json()
    response = []

    tz = int(current_dt.strftime("%z")[1:3])  # format ==>   +0100  convert to int("01")
    for row in request['results']:
        dt_start = datetime.strptime(row['start'], "%Y-%m-%dT%H:%M:%S%z")
        dt_end = current_dt.replace(hour=23)

        current_dt = current_dt.replace(hour=6)  # TEST

        if current_dt < dt_start < dt_end:
            # print("INFO ==> "+dt_start.strftime("%Y-%m-%dT%H:%M:%S")+" / "+current_dt.strftime("%Y-%m-%dT%H:%M:%S")+"/"+dt_end.strftime("%Y-%m-%dT%H:%M:%S"))
            # print(row['title'])
            hour = str(int(row['start'][11:13]) + tz) + "h" + row['start'][14:16]  # format with timeZone

            response.append(row['title'] + "\n Heure :" + hour)

    return response


def getScheduleByOptions(code):
    newUrl = url + "events_tdoption/" + code
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)
    return response


def isMultipleLesson(section, spec):
    new_url = url + "events_promotion/" + getCodeBySection(section, spec)
    request = rq.get(new_url).json()
    last_row = None

    for row in request['results']:
        if last_row is not None:
            if row['start'] == last_row['start']:
                return True
        last_row = row
    return False

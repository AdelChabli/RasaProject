import requests as rq
from  datetime import datetime

url = "https://edt-api.univ-avignon.fr/app.php/api/"

def getCodeBySection(section):
    newUrl = url + "elements"
    request = rq.get(newUrl).json()
    response = ""

    for row in request['results']:
        if row['letter'] == "INFORMATIQUE":
            for e in row['names']:
                if section in e['name']:
                    response = e['code']
    return response

def get_group_by_code(code):
    newUrl = url + "tdoptions/"+code
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)

    return response

def getScheduleByPromo(section, current_dt):
    newUrl = url + "events_promotion/" + getCodeBySection(section)
    request = rq.get(newUrl).json()
    response = ""

    for row in request['results']:
        dt_start = datetime.strptime(row['start'][0:19], "%Y-%m-%dT%H:%M:%S")
        dt_end = datetime.strptime(row['end'][0:19], "%Y-%m-%dT%H:%M:%S")

        if dt_start <= current_dt < dt_end:
            # print("INFO ==> "+dt_start.strftime("%Y-%m-%dT%H:%M:%S")+" / "+current_dt.strftime("%Y-%m-%dT%H:%M:%S")+"/"+dt_end.strftime("%Y-%m-%dT%H:%M:%S"))
            # print(row['title'])
            response = row['title']
    return response

def getScheduleByOptions(code):
    newUrl = url + "events_tdoption/" + code
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)
    return response

# print(get_group_by_code("2-m2en"))
# print(get_schedule_by_code("4133-4130-4126"))

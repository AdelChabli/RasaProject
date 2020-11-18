import requests as rq

url = "https://edt-api.univ-avignon.fr/app.php/api/"

def getallgroup():
    newUrl = url + "elements"
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        if row['letter'] == "INFORMATIQUE":
            for e in row['names']:
                if not "hdr" in e['name']:
                    response.append(e['code'])
    return response

def get_group_by_code(code):
    newUrl = url + "tdoptions/"+code
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)

    return response

def get_schedule_by_code(code):
    newUrl = url + "events_tdoption/" + code
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)
    return response

def get_schedule_by_code(code):
    newUrl = url + "events_tdoption/" + code
    request = rq.get(newUrl).json()
    response = []

    for row in request['results']:
        response.append(row)
    return response

# print(get_group_by_code("2-m2en"))
print(get_schedule_by_code("4133-4130-4126"))

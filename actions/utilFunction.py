def respForAllLesson(response):
    resp = "Vous allez avoir " + str(len(response)) + " cours, "
    for ele in response:
        resp += convertToSentence(ele)

    return resp


def convertToSentence(response):
    lesson, teacher, location, typeL, hour = "", "", "", "", ""

    slitMessage = response.split("\n")
    # print(slitMessage)
    for line in slitMessage:
        if line == "":
            continue
        if "Matière :" in line:
            lesson = line[line.find(':') + 1:]

        if "Enseignant :" in line:
            teacher = line[line.find(':') + 1:]

        if "Salle :" in line:
            location = line[line.find(':') + 1:]

        if "Type :" in line:
            typeL = line[line.find(':') + 1:]

        if "Heure :" in line:
            hour = line[line.find(':') + 1:]

    sentence = "le " + typeL + " " + lesson + " enseigné par " + teacher + " commencera à " + hour + " et se déroulera dans la salle " + location + ", "

    return sentence


def rm_hour(string):
    resp = string
    if "heures" in string:
        resp = resp.replace("heures", '')
    if "heure" in string:
        resp = resp.replace("heure", '')
    if "h" in string:
        resp = resp.replace('h', '.')
    if ' ' in string:
        resp = resp.replace(' ', '')

    return resp


def add_hour(string):
    resp = string
    if '.' in string:
        resp = resp.replace('.', " heure ")
    else:
        resp += " heure"
    return resp

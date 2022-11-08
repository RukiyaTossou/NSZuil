
import json
import datetime

with open("bericht.json", "r") as json_file:
    json_data = json.load(json_file)
lst = []
while True:

    for item in json_data:
        print(item)
        naam = item["naam"]
        invoer = item["bericht"]
        datum = item["datum"]
        tijd = item["tijd"]
        stationsnaam = item["station"]
        beoordelingstijd = item["beoordelingstijd"]
        beoordelingsdatum = item["beoordelingsdatum"]
        goedkeuring = item["goedkeuring"]
        lst.append(item)

    with open("bericht.json", "w") as json_file:
        json.dump(lst, json_file, indent=4)
    break


#info van moderator
naam_mod = input("Beste moderator voer aub uw voor en achternaam in: ")
email_mod = input("Voer hier uw geldig email adres: ")
#while loop, het email adres moet goed zijn anders kan je niet verder
while True :
    if "@" in email_mod:
        break
    else:
        print("beste moderator dit is geen geldig email adres, probeer op nieuw")
        email_mod = input("Voer hier uw geldig email adres: ")



goedkeuring = input("Beste moderator geef aan of dit bericht is goedgekeurd, voer in:  ja of nee")
#de moderator mag alleen ja of nee invoeren niks anders
while True:
    if goedkeuring == "ja" or "nee":
        print("bericht is beoordeeld")
        break
    else:
        print("Je kunt alleen ja of nee invoeren probeer opnieuw ")

d = datetime.datetime.now()
beoordelingstijd = d.strftime("%H:%M:%S")
beoordelingsdatum = d.strftime("%Y-%m-%d")

new_data ={"naam": naam, "bericht": invoer, "station": stationsnaam.strip(), "datum": datum, "tijd": tijd, "beoordelingstijd": beoordelingstijd, "beoordelingsdatum": beoordelingsdatum, "goedkeuring": goedkeuring, "naam_mod" : naam_mod, "email_mod":email_mod}


try:
    with open("new.json", "r") as json_file:
        data = json.load(json_file)
        data.append(new_data)
except:
    data = [new_data]

with open("new.json", "w") as json_file:
    json.dump(data, json_file, indent=4)







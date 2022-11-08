import datetime
import random
import json


naam = input("voer uw naam in:")
invoer = input("U kunt hier een opmerking invullen(Max 140 karakters)")


if naam == "":
    naam = "anoniem"
if len(invoer) > 140: #als het bericht te lang is moet het niet opgeslagen worden in het bestand.
    print("uw bericht is te lang ")


#random station kiezen uit de lijst met station namen
file = open("stations.txt", "r")

data = file.readlines()
stationsnaam = random.choice(data)
file.close()

#huidige datum en tijd gebruiken
x = datetime.datetime.now()
datum = x.strftime("%Y-%m-%d")
tijd = x.strftime("%H:%M:%S")



#alle info die in de file moet
new = {"naam": naam, "bericht": invoer, "station": stationsnaam.strip(), "datum": datum, "tijd": tijd,"beoordelingstijd":"nvt", "beoordelingsdatum": "nvt", "goedkeuring": "nvt"}

try:
    with open("bericht.json","r") as json_file:
        data = json.load(json_file)
        data.append(new)
except:
    data = [new]

with open("bericht.json", "w") as f:
    json.dump(data, f, indent=2)





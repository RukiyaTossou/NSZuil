import psycopg2
import json
# connectie maken met database
con = psycopg2.connect(
    host="localhost",
    database="module2",
    user="postgres",
    password="Nietleuk"
)
with open("new.json", "r") as json_file:
    json_data = json.load(json_file)

while True:

    for item in json_data:
        naam = item["naam"]
        invoer = item["bericht"]
        datum = item["datum"]
        tijd = item["tijd"]
        stationsnaam = item["station"]
        beoordelingstijd = item["beoordelingstijd"]
        beoordelingsdatum = item["beoordelingsdatum"]
        goedkeuring = item["goedkeuring"]
        naam_mod = item["naam_mod"]
        email_mod = item["email_mod"]

cursor = con.cursor()
query = "insert into berichten(bericht,datum,tijd,naam, stationsnaam,goedkeuring,beoordelingsdatum, beoordelingstijd ,naam_moderator, email_adres) values (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
insert = (
invoer, datum, tijd, naam, stationsnaam, goedkeuring, beoordelingsdatum, beoordelingstijd, naam_mod, email_mod)

if "module2" in insert:
    print("staat al in bestand ")
else:
    cursor.execute(query, insert)

con.commit()
# cursor sluiten
cursor.close()

# connectie sluiten
con.close()






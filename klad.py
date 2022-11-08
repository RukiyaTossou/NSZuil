import requests
import tkinter
import json


with open("bericht.json", "r")as json_file:
    json_data = json.load(json_file)

for item in json_data:
    naam = item.get("naam")
    invoer = item.get("bericht")
    datum = item.get("datum")
    tijd = item.get("tijd")
    station = item.get("station")

file = open("api.text", "r")
line = file.readline()
file.close()

api_key = line
def weer(api_key, station):
    url = f"https://api.openweathermap.org/data/2.5/weather?&appid={api_key}"


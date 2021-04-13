import requests
import json
import datetime
import mysql.connector
#import pyodbc

location_data_all = requests.get('https://pte2.duckdns.org/api/v1/locations/oil230')
locoation_database = requests.get("https://pte2.duckdns.org/api/v1/database/eersel")
file_name_pre = "response"
date = datetime.datetime.now()
date_format = str(date.strftime("%d")) + "-" + str(date.strftime("%m")) + "-" + str(date.strftime("%Y")) + "_" + str(date.strftime("%H")) + "-" + str(date.strftime("%M")) + "-" + str(date.strftime("%S"))

#aanmaken van het .json bestand met de API request:
def jprint(obj, file_name):

  datum = datetime.datetime.now()
  text = json.dumps(obj, sort_keys=True, indent=4)
  #datum in een str zetten
  date = str(datum.strftime("%d")) + "-" + str(datum.strftime("%m")) + "-" + str(datum.strftime("%Y")) + "_" + str(datum.strftime("%H")) + "-" + str(datum.strftime("%M")) + "-" + str(datum.strftime("%S"))

  f = open(file_name + "_" + date + ".json", "x")
  f.write(text)
#  print(text)


#aanvragen van de functie:
jprint(location_data_all.json(), file_name_pre)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:16:32 2021

@author: Gamer
"""
import requests
import json
import requests
import json
import csv
import re
import os
import time

#response = requests.get("https://crimescore.p.mashape.com/")


##FBI Database
api_key = "E3CSzOIS8dKUIhAnbmQ3JhWqbnvNdgFTPwqlV3SO"
#response = requests.get("https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/MO0830100/aggravated-assault/2017/2019?api_key=" + api_key)

#def jprint(obj):
  #  text = json.dumps(obj, sort_keys=True, indent=4)
 #   print(text)
#
#jprint(response.json())

#county_ORI = "AL0040000"

#aggravatedAssault_Response = requests.get("https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/" + county_ORI + "/aggravated-assault/2005/2007/?api_key=" + api_key)

#def jprint(obj):
    #text = json.dumps(obj, sort_keys=True, indent=4)
    #print(text)

#jprint(aggravatedAssault_Response.json())

#import re
#org_string = '        "count": 0,'
#pattern = r'[a-z, A-Z, '', ", :, ,]'
# Match all digits in the string and replace them by empty string
#mod_string = re.sub(pattern, '', org_string)
#print(mod_string)



#pattern = r'[a-z, A-Z, '', ", :, ,]'
#newFile = open('NewFile.txt', 'a')
#with open('Lesser-CrimeStats.txt', 'r+') as file_lesserCrimeStats:
#    for line in file_lesserCrimeStats:
#        mod_string = re.sub(pattern, '', line)
#        newFile.write(mod_string)
        
#newFile.close()
        
#with open("Lesser-CrimeStats.txt") as lessercount:
 #   start_CountLesser = 0
  #  for line in lessercount:
   #     start_CountLesser = start_CountLesser + int(line)

#print(start_CountLesser)

#def truncate(n, decimals=0):
#    multiplier = 10 ** decimals
#    return int(n * multiplier) / multiplier

#math = 2/3
#print(truncate(math, 4))


zipCode = input("Enter area Zip Code: ")

usZips = open('C:\\Users\\Gamer\\Desktop\\Work\\uszips_v1.csv')  # Keep in mind this MUST be in the same file pathway as the code, or the string itself needs the explicit pathway to the file
csv_usZips = csv.reader(usZips) # Just sets the a variable equal to the file so it can be more easily read inside of the program

for row in csv_usZips:          # This loop just goes through every row in the uszips_v1.csv file to find a match
    if row[0] == zipCode:
        county_Name = (row[4])
     #   print (row[4] + " County")          # Gives the County Name associated with the Zip Code number  
        stateABV = (row[2])     # Gives the state code, ex: MO --> Missouri
       # print("State: " + stateABV)

countyNumber = open('C:\\Users\\Gamer\\Desktop\\Work\\State_ORI\\NumberOfCounties.csv')
csv_countyNumber = csv.reader(countyNumber)

for row in csv_countyNumber:
    if row[0] == stateABV:
        print(row[1])


























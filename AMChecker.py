'''
Created on Aug 19, 2015

@author: djunghans
'''

import csv
import requests
import json

def main():

    blacklist = [
      "craigslist"
    ]

    def isInBlacklist(email):
      for keyword in blacklist:
        if keyword in email:
          return True
      return False

    contacts =[]
    with open('contacts.csv', 'rb') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      header = reader.next()
      for row in reader: 
        contacts.append(row)

    for row in contacts:
      name = row[header.index('Name')]
      email = row[header.index('E-mail 1 - Value')]

      if isInBlacklist(email):
        continue

      result = requests.post('https://ashley.cynic.al/check', data={'email':email})
      if result.status_code is 200:
        rawJson = result.text
        response = json.loads(rawJson)
        if response.has_key('found'):
          print email + " - " + response['found']
      else:
        print email + ' - server error: ' + str(result.status_code)

if __name__ == '__main__':
    main()
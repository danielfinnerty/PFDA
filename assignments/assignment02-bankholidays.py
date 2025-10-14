# Program to print out Northern Ireland bank holidays
# Author: Daniel Finnerty

import requests
import pandas as pd

 
url =" https://www.gov.uk/bank-holidays.json" # json file location
response = requests.get(url)
data = response.json()
nirl_data = (data['northern-ireland']) # seperate all the northern ireland dates from the rest

# print('Northern Ireland 2024 Bank Holidays:') # this pulls all holidays in the file, without separation for each year.

# To outline holidays for each year:
print('Northern Ireland 2024 Bank Holidays:')

# Create loop to pull all the events that occur on a date which starts with 2024.
for event in nirl_data['events']:
    if event['date'].startswith('2024'): # Startswith reference: https://www.w3schools.com/python/ref_string_startswith.asp
        print(f'{event["title"]} occurs on {event["date"]}')

print('\n''Northern Ireland 2025 Bank Holidays:')

# Repeat look for 2025 and so on.
for event in nirl_data['events']:
    if event['date'].startswith('2025'):
        print(f'{event["title"]} occurs on {event["date"]}')

print('\n''Northern Ireland 2026 Bank Holidays:')

for event in nirl_data['events']:
    if event['date'].startswith('2026'):
        print(f'{event["title"]} occurs on {event["date"]}')

print('\n''Northern Ireland 2027 Bank Holidays:')

for event in nirl_data['events']:
    if event['date'].startswith('2027'):
        print(f'{event["title"]} occurs on {event["date"]}')
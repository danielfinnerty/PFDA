# Program to print out Northern Ireland bank holidays
# Author: Daniel Finnerty

import requests
import pandas as pd

 
url =" https://www.gov.uk/bank-holidays.json" # json file location
response = requests.get(url)
data = response.json()
nirl_dates = (data['northern-ireland']) # seperate all the northern ireland dates from the rest


# print('Northern Ireland 2024 Bank Holidays:') # this code would pull all holidays in the file, without separation for each year.
# To outline holidays clearly for each for each year:

print('Northern Ireland 2024 Bank Holidays:')

# Create loop to pull all the events that occur on a date which starts with 2024.
for event in nirl_dates['events']:
    if event['date'].startswith('2024'): # Startswith reference: https://www.w3schools.com/python/ref_string_startswith.asp
        print(f'{event["title"]} occurs on {event["date"]}')

print('\n''Northern Ireland 2025 Bank Holidays:')

# Repeat loop for 2025 and so on.
for event in nirl_dates['events']:
    if event['date'].startswith('2025'):
        print(f'{event["title"]} occurs on {event["date"]}')

print('\n''Northern Ireland 2026 Bank Holidays:')

for event in nirl_dates['events']:
    if event['date'].startswith('2026'):
        print(f'{event["title"]} occurs on {event["date"]}')

print('\n''Northern Ireland 2027 Bank Holidays:')

for event in nirl_dates['events']:
    if event['date'].startswith('2027'):
        print(f'{event["title"]} occurs on {event["date"]}')


# For determining bank holidays that are unique to Northern Ireland 
# Separate all the holdiys associated to the 3 regions.

eng_hols = data['england-and-wales']['events']
scot_hols = data['scotland']['events']
nirl_hols = data['northern-ireland']['events']


# Use set comprehension to collect list of unique bank holidays (titles) for each region.
# Source: https://realpython.com/python-set-comprehension/

eng_titles = set(event['title'] for event in eng_hols)
scot_titles = set(event['title'] for event in scot_hols)
nirl_titles = set(event['title'] for event in nirl_hols)


# Compare the difference in the Northern Ireland list to the other 2.
# source = https://www.askpython.com/python/list/difference-between-two-lists-unique-entries

difference = list(nirl_titles - scot_titles - eng_titles)
# Print the result

print (f'\n''The unique Northern Ireland bank holidays are:''\n',difference)
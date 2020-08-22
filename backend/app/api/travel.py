import requests
import os
import json


url = "https://api.edamam.com/search?q=chicken&app_id=1a1b22a4&app_key=a2c22e4e48e83a0e569c38bf86c67d60&from=0&to=3&calories=591-1000"

response = requests.get(url)
print(response.text)


#
# with open("example.json", "r") as file:
#     data = json.load(file)
#
# for key, val in data.items():
#     print(key, val)
#
#
# def travel_data():
#     pass





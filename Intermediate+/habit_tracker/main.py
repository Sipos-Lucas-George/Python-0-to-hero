"""
    Track Habits With Pixela
"""
import requests
import os
import dotenv
from datetime import date, timedelta

dotenv.load_dotenv()

USERNAME = "imalilpie"
GRAPH_ID = "graph1"
PIXELA_CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_CREATE_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs"
PIXELA_POST_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
PIXELA_PUT_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/"
PIXELA_ADD_TO_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/add"
TOKEN = os.getenv("TOKEN")


# Add to today's pixel
quantity = input("Add hours(.): ")
pixel_parameters = {
    "quantity": quantity
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.put(PIXELA_ADD_TO_PIXEL_ENDPOINT, json=pixel_parameters, headers=headers)
print(response.text)

# Creating account
# user_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(PIXELA_CREATE_USER_ENDPOINT, json=user_parameters)
# print(response.text)

# Creating graph
# graph_parameters = {
#     "id": GRAPH_ID,
#     "name": "Programming Graph",
#     "unit": "h",
#     "type": "float",
#     "color": "kuro"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(PIXELA_CREATE_GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(response.text)

# Update graph
# graph_parameters = {
#     # "timezone": "Europe/Bucharest",
#     # "color": "kuro",
#     # "unit": "Hours"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.put(PIXELA_PUT_GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(response.text)

# POST a pixel
# today = date.today()
# pixel_parameters = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "6.9"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(PIXELA_POST_GRAPH_ENDPOINT, json=pixel_parameters, headers=headers)
# print(response.text)

# Update a pixel
# today = (date.today() - timedelta(days=1)).strftime("%Y%m%d")
# PIXELA_PUT_GRAPH_ENDPOINT += today
# pixel_parameters = {
#     "quantity": "3.5"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.put(PIXELA_PUT_GRAPH_ENDPOINT, json=pixel_parameters, headers=headers)
# print(response.text)

# Delete a pixel
# today = date.today().strftime("%Y%m%d")
# PIXELA_PUT_GRAPH_ENDPOINT += today
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.delete(PIXELA_PUT_GRAPH_ENDPOINT, headers=headers)
# print(response.text)

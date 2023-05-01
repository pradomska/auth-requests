import requests
from datetime import datetime

# <PIXELA_ENDPOINT>/<username>/graphs/<graphID>.html
USER = "paulina"
TOKEN = "************"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs"
GRAPH_ID_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_params = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()

graph_id_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}
# response = requests.post(url=GRAPH_ID_ENDPOINT, json=graph_id_params, headers=headers)
# print(response.text)

update_endpoint = f"{GRAPH_ID_ENDPOINT}/{today.strftime('%Y%m%d')}"
update_graph = {
    "quantity": "9",
}
# response = requests.put(url=update_endpoint, json=update_graph, headers=headers)
# print(response.text)

delete_endpoint = f"{GRAPH_ID_ENDPOINT}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

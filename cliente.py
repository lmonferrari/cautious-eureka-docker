import requests

url = "http://127.0.0.1:8000"
endpoint = "/api/v1/"

header = {"accept": "application/json"}

file = [("image", open("./images/imagem3.jpg", "rb"))]
payload = {"text": (None, "What is the dog doing in the image?")}

response = requests.request(
    "POST",
    url=url + endpoint,
    headers=header,
    data=payload,
    files=file,
)

print(response.text)

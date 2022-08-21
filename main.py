import base64
import requests
import datetime


from secrets import client_id, client_secret

def convert_key(): 
    creds = f"{client_id}:{client_secret}"
    creds = base64.b64encode(creds.encode())
    return creds.decode()

#Use our key to get the access token to do stuff 
def get_token(): 
    response = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "client_credentials"}, headers={"Authorization": f"Basic {convert_key()}"}) 
    return response.json()['access_token']

def search(query):
    pass

print(get_token())


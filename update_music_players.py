import csv
import requests

def update_music_players(file_path, client_id, token):
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        mac_addresses = [row[0] for row in reader]
    
    
    endadress = "https:///profiles/clientId:port"
    
    
    headers = {
        "Content-Type": "application/json",
        "x-client-id": client_id,
        "x-authentication-token": token
    }
    
    
    body = {
        "profile": {
            "applications": [
                {
                    "applicationId": "music_app",
                    "version": "v1.4.10"
                },
                {
                    "applicationId": "diagnostic_app",
                    "version": "v1.2.6"
                },
                {
                    "applicationId": "settings_app",
                    "version": "v1.1.5"
                }
            ]
        }
    }
    
    
    for mac_address in mac_addresses:
        
        url = endadress.format(mac_address)
        
        
        response = requests.put(url, headers=headers, json=body)
        
        
        if response.status_code == 200:
            print("Success:", response.json())
        elif response.status_code == 401:
            print("Error 401: Unauthorized")
        elif response.status_code == 404:
            print("Error 404: Not Found")
        elif response.status_code == 409:
            print("Error 409: Conflict")
        elif response.status_code == 500:
            print("Error 500: Internal Server Error")

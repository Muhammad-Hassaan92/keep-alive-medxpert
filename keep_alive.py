import requests

url = "https://huggingface.co/spaces/Muhammad-Hassaan/MedXpert"

def keep_alive():
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully pinged the app!")
    else:
        print("Failed to ping the app.")

if __name__ == "__main__":
    keep_alive()

import requests

urls = [
    "https://huggingface.co/spaces/Muhammad-Hassaan/MedXpert",
    "https://huggingface.co/spaces/Muhammad-Hassaan/LinguaFix",
    "https://huggingface.co/spaces/Muhammad-Hassaan/chatbot",
    "https://huggingface.co/spaces/Muhammad-Hassaan/Text-Summarizer",
    "https://huggingface.co/spaces/Muhammad-Hassaan/SnapShoe-Picture-Perfect-Predictions",
    "https://huggingface.co/spaces/Muhammad-Hassaan/Diabetes-Prediction",
    "https://huggingface.co/spaces/Muhammad-Hassaan/Chatbot_Voice_Assistant"
]

def keep_alive():
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"✅ Successfully pinged: {url}")
            else:
                print(f"⚠️ Failed to ping: {url} (Status: {response.status_code})")
        except Exception as e:
            print(f"❌ Error pinging {url}: {e}")

if __name__ == "__main__":
    keep_alive()

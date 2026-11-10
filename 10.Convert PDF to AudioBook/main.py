import requests
from requests import RequestException
from pdf_reader import extract_text
import os
from dotenv import load_dotenv
load_dotenv()

pdf_path = "simple_pdf_audiobook_test.pdf"

all_text = extract_text(pdf_path=pdf_path)
print(all_text)

url = "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb"
headers = {
    "xi-api-key":os.environ.get("API_KEY"),
    "Content-Type":"application/json"
}
data = {
    "text": all_text,
    "model_id": "eleven_multilingual_v2"
}
try:
    response = requests.post(url=url,json=data,headers=headers)
    print(response.raise_for_status())

    with open("audiobook.mp3","wb") as file:
        file.write(response.content)
except requests.exceptions.RequestException as e:
    print(e)



import requests
import pandas as pd
import os

# Load metadata CSV
df = pd.read_csv("cv-valid-dev.csv")

def transcribe_file(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post("http://localhost:8001/asr", files={"file": f})
    if response.status_code == 200:
        return response.json().get("transcription")
    return ""

# Transcribe each file and store the result
df["generated_text"] = df["filename"].apply(lambda x: transcribe_file(f"{x}"))
df.to_csv("cv-valid-dev.csv", index=False)

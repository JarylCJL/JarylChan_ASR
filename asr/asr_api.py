from flask import Flask, request, jsonify
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from pydub import AudioSegment
import torch
import os

# AudioSegment.converter = os.path.join(os.path.dirname(__file__), "ffmpeg/bin/ffmpeg.exe")

app = Flask(__name__)

# Load the model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@app.route('/asr', methods=['POST'])
def asr():
    file = request.files['file']
    # Convert the uploaded file to the correct format
    audio = AudioSegment.from_file(file).set_frame_rate(16000).set_channels(1)
    audio_samples = torch.tensor(audio.get_array_of_samples()).float()

    # Process the audio and get predictions
    inputs = processor(audio_samples, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(inputs.input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    # Calculate duration
    duration = len(audio) / 1000.0  # in seconds

    # Return the response
    return jsonify({
        "transcription": transcription,
        "duration": str(duration)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)

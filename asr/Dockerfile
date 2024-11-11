# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements_docker.txt .

# Install the dependencies
RUN pip install -r requirements_docker.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port Flask will run on
EXPOSE 8001

# Install ffmpeg for audio processing
RUN apt-get update && apt-get install -y ffmpeg

# Command to run the Flask app
CMD ["python", "asr_api.py"]

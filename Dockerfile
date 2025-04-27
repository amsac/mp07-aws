# Use an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your requirements.txt first (for better cache)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app files (Python script, model file, etc.)
COPY . .

# Expose the port Gradio runs on
EXPOSE 7860

# Command to run your app
CMD ["python", "app.py"]



# # Build the docker image
# docker build -t gradio-app .

# # Run the docker container
# docker run -p 7860:7860 gradio-app
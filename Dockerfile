# Use a Python base image (adjust version if needed, e.g., python:3.8-slim based on notebook)
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and the model
COPY . .

# Expose the port Gradio will run on (defined in app.py's launch command)
EXPOSE 8001

# Expose the port Prometheus metrics will be served on (defined in start_http_server)
EXPOSE 8000

# Command to run the application when the container starts
CMD ["python", "app.py"]
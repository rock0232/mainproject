# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code to the container
COPY . .

# Set any necessary environment variables
ENV DISPLAY=host.docker.internal:99

# Define the command to run your Python script
CMD ["python", "TestCases/rough.py"]

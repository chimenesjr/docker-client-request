# Use an official Python runtime as a parent image
FROM frolvlad/alpine-python3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apk --no-cache add curl

# Make port 80 available to the world outside this container
EXPOSE 8888

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "request.py"]

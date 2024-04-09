FROM ubuntu:latest

# Install OpenJDK 
RUN \
  apt-get update && \
  apt-get install -y openjdk-17-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python3 python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python3 /usr/bin/python

# Install PySpark and Numpy
RUN \
    pip install --upgrade pip && \
    pip install numpy && \
    pip install pyspark

# Set the working directory in the container
WORKDIR /mlops

# Copy the Flask server code into the container
COPY . /mlops

# Install any dependencies needed for your Flask server
RUN pip install -r requirements.txt

# Expose port 8001 for Flask server
EXPOSE 8001

# Define environment variables
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["python", "app.py"]
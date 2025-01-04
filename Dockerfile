# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set environment variables
ENV FLASK_APP=server.py
ENV FLASK_ENV=production

# Expose port 5000 to allow access to the Flask app
EXPOSE 5000

# Set the default command to run your Flask app
# CMD ["flask", "run", "--host", "0.0.0.0"]

ENTRYPOINT ["/app/entrypoint.sh"]
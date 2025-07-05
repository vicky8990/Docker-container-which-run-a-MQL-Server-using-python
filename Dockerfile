# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy your Flask app code
COPY app.py .

# Install dependencies
RUN pip install flask mysql-connector-python

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the app
CMD ["flask", "run"]

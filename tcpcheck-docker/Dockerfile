# Stage 1: Build stage
FROM python:3.9-slim AS build

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Stage 2: Final stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application code
COPY --from=build /app /app

# Expose the port
EXPOSE 8080

# Set environment variable
ENV FLASK_APP=wsgi.py

# Run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "wsgi:app"]


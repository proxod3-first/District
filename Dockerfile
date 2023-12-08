# Base image
FROM python:3.9-slim-buster

RUN mkdir /app
# Set working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app

# Install project dependencies
RUN pip install -r requirements.txt

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
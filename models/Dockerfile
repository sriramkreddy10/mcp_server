FROM python:3.13.7-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

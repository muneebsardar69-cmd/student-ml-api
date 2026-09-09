# Use specific Python version (not latest)
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first (for better layer caching)
COPY requirements.txt .

# Install Python dependencies without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create VERSION file in container
COPY VERSION .

# Expose port 5000
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=app.py

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:5000/health')" || exit 1

# Run the Flask application
CMD ["python", "app.py"]

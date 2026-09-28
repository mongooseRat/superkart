# -----------------------------
# Base image
# -----------------------------
FROM python:3.12-slim

# -----------------------------
# Working directory inside container
# -----------------------------
WORKDIR /app

# -----------------------------
# Copy requirements and install
# -----------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy API code and model file
# -----------------------------
COPY . .

# -----------------------------
# Expose FastAPI port
# -----------------------------
EXPOSE 7860

# -----------------------------
# Run the FastAPI app with uvicorn
# -----------------------------
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
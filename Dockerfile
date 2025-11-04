# Gunakan image Python dasar
FROM python:3.8-slim

# Set working directory di dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . /app

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Perintah untuk menjalankan aplikasi
CMD ["python", "app/calculator.py"]

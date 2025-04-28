# Python resmi imajı
FROM python:3.13-slim

# Çalışma dizini
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Portu aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]

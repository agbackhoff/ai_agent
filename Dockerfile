FROM python:3.9-slim

# Instalar ping y herramientas de red para diagnóstico
RUN apt-get update && apt-get install -y iputils-ping curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Variables de entorno para timeouts
ENV GRPC_TIMEOUT=30
ENV PYTHONUNBUFFERED=1

# Verificar conectividad antes de ejecutar
CMD ping -c 1 generativelanguage.googleapis.com && python src/main.py 
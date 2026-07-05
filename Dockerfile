FROM python:3.11-slim

WORKDIR /app

# Dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code de l'application (server.py, index.html, images/, reservations.db, swagger.yaml)
COPY . .

EXPOSE 5000

CMD ["python", "server.py"]
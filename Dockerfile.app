FROM python:3.9

WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]

# docker build -t my-app-image -f Dockerfile.app . && docker run -d -p 8080:8080 --name my-app-container my-app-image
# docker exec -it my-app-container bash
# docker stop my-app-container && docker rm my-app-container && docker rmi my-app-image



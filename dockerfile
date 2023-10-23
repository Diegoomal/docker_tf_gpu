FROM tensorflow/tensorflow:latest-gpu

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY app/ .
CMD [ "python", "main.py" ]
FROM tensorflow/tensorflow:latest-gpu

ENV TF_CPP_MIN_LOG_LEVEL 2

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY app/ .
CMD [ "python", "main.py" ]
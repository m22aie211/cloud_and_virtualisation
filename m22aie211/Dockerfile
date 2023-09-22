FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y python3 python3-pip

WORKDIR /app

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt


RUN pip3 install -r requirements.txt

EXPOSE 5050

CMD ["python3", "app.py"]

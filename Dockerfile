FROM python:3.10.0

RUN apt-get update -y && \
    apt-get install python3-opencv gedit -y\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py .

CMD ["python", "app.py","gedit"]
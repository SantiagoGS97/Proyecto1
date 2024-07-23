FROM python:3.10.0

RUN apt-get update -y && \
    apt-get install python3-opencv gedit -y\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone https://github.com/SantiagoGS97/Proyecto1.git

WORKDIR /home/src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py .
COPY ./neumonia_detec.py .

CMD ["python", "app.py","gedit","neumonia_detec.py"]
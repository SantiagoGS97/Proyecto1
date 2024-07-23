FROM python:3.10.0

RUN apt-get update -y && \
    apt-get install python3-opencv gedit -y\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/src

COPY requirements.txt .
COPY imagenes/ .

# En la carpeta donde se vaya a crear el Docker file, debe estar
# la carpeta de models con el archivo .h5 para que al 
# ejecutarse en Docker funciones
COPY models /home/src/models

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py .
COPY ./neumonia_detec.py .

CMD ["python", "app.py","gedit","neumonia_detec.py"]
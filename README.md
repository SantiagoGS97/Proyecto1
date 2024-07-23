
## 🩺 Hola! Bienvenido a la herramienta para la detección rápida de neumonía 🩺

Deep Learning aplicado en el procesamiento de imágenes radiográficas de tórax en formato DICOM, jpg o png con el fin de clasificarlas en 3 categorías diferentes:

1. Neumonía Bacteriana 🦠

2. Neumonía Viral ⚕️

3. Sin Neumonía ❤️‍🩹

Aplicación de una técnica de explicación llamada Grad-CAM para resaltar con un mapa de calor las regiones relevantes de la imagen de entrada.

---

## Uso de la herramienta 🛠️

Para usar la herramienta es necesario crear un Dockerfile, el cual creara un contenedor donde puede correr la aplicación, para ello basta con copiar el siguiente código y pegarlo en el Dockerfile 

    FROM  python:3.10.0
    RUN  apt-get  update  -y  && 
	     apt-get  install  python3-opencv  gedit  -y\
	     &&  apt-get  clean  \
	     &&  rm  -rf  /var/lib/apt/lists/*  /tmp/*  /var/tmp/*
	RUN  git  clone  https://github.com/SantiagoGS97/Proyecto1.git
    WORKDIR  /home/src
    COPY  requirements.txt  .
    RUN  pip  install  --no-cache-dir  -r  requirements.txt
    COPY  ./app.py  .
    CMD  ["python",  "app.py","gedit"]

Cuando el contenedor este creado este puede ser ejecutado desde la aplicación de Docker Desktop o bien desde consola ejecutando `Docker run contenedor`

⚠️ Si el contenedor se corre en Windows se debe intalar [Xming](https://sourceforge.net/projects/xming/)  Para que el contendor no tenga problemas a la hora de mostrar las interfaces graficas.

⚠️ Si se corre el Docker en Ubuntu o cualquier disto de Linux importante tenerl la Shell de GNOME para que pueda funcionar a la hora de crear los archivos de PDF.

---

## Arquitectura de archivos propuesta 🏗️

## app.py 🐍

Contiene el diseño de la interfaz gráfica utilizando Tkinter, la interacción de los botones y los espacios de texto para agregar informacion sobre el paciente
 
![Reporte0](https://github.com/user-attachments/assets/018be707-b3bb-4a74-877e-1f84b132d043)

## modelo.py 🧩

En este modulo se crea una función que llama a un modelo pre-entrenado para detectar anomalías en imágenes de radiografías.

## read_img.py 🖼️

Dentro de este modulo esta una sola clase la cual es capaz de leer formatos de imagenes usados para las radiograficas como puede ser *.dcm*, *.jpg*, *.jpeg*, y *.png*.

## preprocess.py 🏭

Script que recibe el arreglo proveniente de read_img.py, realiza las siguientes modificaciones:

- resize a 512x512
- conversión a escala de grises
- ecualización del histograma con CLAHE
- normalización de la imagen entre 0 y 1
- conversión del arreglo de imagen a formato de batch (tensor)

## pdf.py ✉️

En este modulo esta una función que se encarga de tomar un screenshot a la GUI con la predicción para posteriormente guardarla en un archivo de PDF.

## predict.py 🔮

En este modulo se carga el modelo, se procesa la imagen y se hace la predicción con  la capa convolucional de interés para obtener las características relevantes de la imagen.

---

## Acerca del Modelo ❓

La red neuronal convolucional implementada (CNN) es basada en el modelo implementado por F. Pasa, V.Golkov, F. Pfeifer, D. Cremers & D. Pfeifer
en su artículo Efcient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization.

Está compuesta por 5 bloques convolucionales, cada uno contiene 3 convoluciones; dos secuenciales y una conexión 'skip' que evita el desvanecimiento del gradiente a medida que se avanza en profundidad.
Con 16, 32, 48, 64 y 80 filtros de 3x3 para cada bloque respectivamente.

Después de cada bloque convolucional se encuentra una capa de max pooling y después de la última una capa de Average Pooling seguida por tres capas fully-connected (Dense) de 1024, 1024 y 3 neuronas respectivamente.

Para regularizar el modelo utilizamos 3 capas de Dropout al 20%; dos en los bloques 4 y 5 conv y otra después de la 1ra capa Dense.

## Acerca de Grad-CAM ❓

Es una técnica utilizada para resaltar las regiones de una imagen que son importantes para la clasificación. Un mapeo de activaciones de clase para una categoría en particular indica las regiones de imagen relevantes utilizadas por la CNN para identificar esa categoría.

Grad-CAM realiza el cálculo del gradiente de la salida correspondiente a la clase a visualizar con respecto a las neuronas de una cierta capa de la CNN. Esto permite tener información de la importancia de cada neurona en el proceso de decisión de esa clase en particular. Una vez obtenidos estos pesos, se realiza una combinación lineal entre el mapa de activaciones de la capa y los pesos, de esta manera, se captura la importancia del mapa de activaciones para la clase en particular y se ve reflejado en la imagen de entrada como un mapa de calor con intensidades más altas en aquellas regiones relevantes para la red con las que clasificó la imagen en cierta categoría.

## Proyecto original realizado por 👩🏻‍💻👨🏻‍💻

Isabella Torres Revelo - https://github.com/isa-tr
Nicolas Diaz Salazar - https://github.com/nicolasdiazsalazar

# Yolo11

## Códigos:

**webpub.py:**
Publicador de imágenes. Captura imágenes desde la WebCam(0) por el topic especifico en formato comprimido.
* Topic: /webcam/image/compressed
* CompressedImage: Comprimido en formato "jpeg"

**cv2_msg_test.py:**
Código para test con todas las funciones de conversión de imágenes ROS <=> openCV.

**websupprocess.py:**
Visualizador de imágenes. Muestra imágenes publicadas en el topic específico. Espera las imágenes comprimidas.
* topic: /yolo/image/compressed
* CompressedImage: Comprimido en formato "jpeg"

**yolo_process.py:**
Procesa con yolov11n.pt las imágenes, devolviendo un json con el resultado del procesamiento de inferencia, y una imagen con el etiquetado. Espera todas las imágenes en formato comprimido.
* topicIn: /webcam/image/compressed
* topicOut: /yolo/image/compressed
* topicOut: /yolo/inference

**yolo_test.py**
Código para test con funciones de pruebas de yolo.

## Uso:
### entry_points:
* webpub = yolo11.webpub:main
* yolo_test = yolo11.yolo_test:main
* view_imgprocess = yolo11.websupprocess:main

# Ejecución:
Para ejecutar cada uno de los nodos de este paquete, se necesitan 3 terminales, en las que tenemos que ejecutar estas tres órdenes:

    ros2 run yolo11 webpub
    ros2 run yolo11 yolo_process
    ros2 run yolo11 view_imgprocess

# Lanzado:
Para lazar la demo de funcionamiento de este paquete, con los tres paquetes a la vez, se puede usar el comando:

    ros2 launch yolo11 yolo11_launch.py

# Problemas
Si tenéis problemas con la instalación de Yolo, porque se interrumpe la instalación, una de las maneras de arreglar el error es con el comando **--no-cache-dir**

    pip install ultralytics --no-cache-dir

Durante la instalación de Yolo, se puede producir una actualización de **numpy** a la versión 2.xx, como se puede ver en siguiente código de salida en la instalación:

    Collecting numpy>=1.23.0
       Downloading numpy-2.1.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)

Yolo11 necesita la versión numpy v1.xx para que funcione correctamente, por lo que es necesario hacer un donwgrade de versión:

    pip install --upgrade numpy==1.26.4


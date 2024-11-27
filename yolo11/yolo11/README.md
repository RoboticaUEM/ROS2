# Yolo11

## Codigos:

**webpub.py:**
Publicador de imagenes. Captura imagenes desde la WebCam(0) por el topic especifico en formato comprimido.
* Topic: /webcam/image/compressed
* CompressedImage: Comprimido en formato "jpeg"

**cv2_msg_test.py:**
Codigo con todas las funciones de conversion de imagenes ROS <=> openCV.
 

**websupprocess.py:**
Visualizador de imagenes. Muestra imagenes imagenes publicadas en el topic especifico. Espera las imagenes comprimidas.
* topic: /webcam/image/yoloProcess
* CompressedImage: Comprimido en formato "jpeg"

**yolo_process.py:**
Procesa con yolov11n.pt las imagenes, devolviendo un json con el resultado del prcesamiento de inferencia, y una imagen cin el etiquetado.
* topicIn: /webcam/image/compressed
* topicOut: /yolo/image/compressed
* topicOut: /yolo/inference

**yolo_test.py**
Test de yolo.

## Uso:
### entry_points:
* webpub = yolo11.webpub:main
* yolo_test = yolo11.yolo_test:main
* view_imgprocess = yolo11.websupprocess:main

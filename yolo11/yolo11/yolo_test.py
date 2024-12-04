#!/home/mixi/yolo11/bin python3

from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("/home/mixi/yolo11/yolo11n.pt", verbose=True)
print(model.names)
print(model.info(detailed = False, verbose = True))

# from ndarray
im2 = cv2.imread("/home/mixi/yolo11/bus.jpg")
results = model.predict(source=im2, save=True, save_txt=True, verbose=False)  # save predictions as labels
# results would be a generator which is more friendly to memory by setting stream=True
# 2. return as a generator
#results = model.predict(source=0, stream=True)

for result in results:
    print("1.-=======================================================================")
    print(result)
    print("2.-=======================================================================")
    print(result.boxes)  # Print detection boxes
    print(result.masks)  # Masks object for segmentation masks outputs
    print(result.keypoints)  # Keypoints object for pose outputs
    print(result.probs)  # Probs object for classification outputs
    print(result.obb)  # Oriented boxes object for OBB outputs
    result.show()  # Display the annotated image
    #result.save(filename="result.jpg")  # Save annotated image
    print(result.to_json(normalize=True, decimals=5))
    print("3.-=======================================================================")
    print(result.summary())
    print("4.-=======================================================================")
    import json
    print(json.dumps(result.summary(normalize=True, decimals=6), indent=3))
    print("5.-=======================================================================")
    print(result.to_csv())
    print("6.-=======================================================================")

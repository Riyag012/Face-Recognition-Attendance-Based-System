import cv2
import numpy as np
import face_recognition
imgSam = face_recognition.load_image_file('Images Basic/samAltman_train.jpeg')
imgSam = cv2.cvtColor(imgSam, cv2.COLOR_BGR2RGB)
# OpenCV loads images in BGR (Blue, Green, Red) format by default.However, the face_recognition library expects 
# images to be in RGB (Red, Green, Blue) format to properly process them for face detection and encoding.
imgTest = face_recognition.load_image_file('Images Basic/samAltman_test.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)


faceLoc = face_recognition.face_locations(imgSam)[0] #used to define the cordinates of the face (x1,x2,y1,y2)
# The function face_recognition.face_locations() returns a list of all face locations detected in the image.
# Each face location is represented as a tuple: (top, right, bottom, left), which gives the coordinates of the face's 
# bounding box.
encodeSam = face_recognition.face_encodings(imgSam)[0]


'''
When to Use [0]:
1. This works if there is only one face in the image. If there are multiple faces, and you only use [0], you’re selecting
 just the first face detected.
2. If your image contains multiple faces, you might need to iterate over the list instead of selecting just the first one.
'''
'''
Face Encoding:
1. Represents the features of the detected face.
2. It’s a numerical representation (usually a 128-dimensional vector) that describes unique facial features.
These encodings are used to compare and match faces.
'''

# cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(imgSam, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)

faceLoc = face_recognition.face_locations(imgTest)[0] #used to define the cordinates of the face (x1,x2,y1,y2)
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)

result = face_recognition.compare_faces([encodeSam], encodeTest)
faceDist = face_recognition.face_distance([encodeSam], encodeTest)
print(result, faceDist)
cv2.putText(imgTest, f'{result}, {round(faceDist[0], 2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)


cv2.imshow('samAltman_train', imgSam)
cv2.imshow('samAltman_test', imgTest)
cv2.waitKey(0)
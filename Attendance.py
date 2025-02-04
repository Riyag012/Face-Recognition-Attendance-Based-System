import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'AttendanceImg'
imgs = []
names = []
myList = os.listdir(path)
# print(myList) #prints ['Adi.jpg', 'Lokesh.jpg', 'Reena.jpg', 'Riya.jpg']
for i in myList:
    curImg = cv2.imread(f'{path}/{i}')
    # This line reads an image file from the directory and stores it in the variable curImg.
    imgs.append(curImg)
    names.append(os.path.splitext(i)[0])
print(names)

def findEncodings(imgs):
    encodingsList = []
    for i in imgs:
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        # facLoc = face_recognition.face_locations(i)[0]
        current = face_recognition.face_encodings(i)[0]
        encodingsList.append(current)
    return encodingsList

alreadyMarked = set()

def markAttendance(names):
    if name not in alreadyMarked:
        with open('Attendance1.csv', 'r+') as f:
        # Using with ensures the file is properly closed after the operations.

            myDataList = f.readlines()
            # The readlines() method reads all lines from the file and stores them as a list of strings in myDataList.
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])

            '''
            Each line from myDataList is split into parts using split(',').
            Example: "John,12:30:45" → ["John", "12:30:45"].
            The first part of the split result (entry[0]) is the name, which is added to nameList.
            '''

            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\{name},{dtString}')
        alreadyMarked.add(name)



encodeListKnown = findEncodings(imgs)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    # The cap.read() function reads frames from the video source (webcam in this case).
    '''
    success:
    ->A boolean indicating if the frame was successfully captured.
    ->True if successful; False if not (e.g., if the webcam is not working or disconnected).
    img:
    ->The actual frame (image) captured by the webcam as a NumPy array.
    '''
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    # This reduces the image dimensions to 25% of the original size, improving processing speed (useful for face detection/encoding).
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

    for encodeFace, faceLoc in zip(encodeCurrFrame, facesCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDist = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDist)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            name = names[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = 4*y1,4*x2,4*y2,4*x1
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            # This rectangle is drawn around the detected face.
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            # This rectangle creates a filled box below the face where the detected person's name will be displayed.
            # It ensures the text is easily readable by providing a contrasting background.
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)


        cv2.imshow('Webcam', img)
        cv2.waitKey(1)
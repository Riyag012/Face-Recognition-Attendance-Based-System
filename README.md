# Face-Recognition-Based-Attendance-System

### Content
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)

### Project Overview

This project is a Face Recognition system using Python, OpenCV, and the face_recognition library. The project has two main functionalities:

1. Basic Face Recognition (basic.py):
- Objective: Perform basic face detection and comparison using two images (training and testing).
  
- Process:

    1. Loads and processes two images (one for training, one for testing).

    2. Detects faces and generates encodings (128-dimensional feature vectors) for the faces.

    3. Compares the test image's face with the training image's face using the generated encodings.

    4. Displays bounding boxes around the detected faces and calculates the similarity distance between the faces.

- Output: Prints whether the faces match and shows the similarity score.

2.  Attendance System (Attendance.py):
   
- Objective: Implement a face recognition-based attendance system using a webcam.

- Process:

    1. Loads images of known individuals from the AttendanceImg folder and generates face encodings for them.

    2. Continuously captures video from the webcam, detects faces in the frame, and compares them to the known faces.

    3. If a match is found, marks the attendance by saving the person's name and the current time in a CSV file.

    4. Draws bounding boxes around detected faces and displays the name of the recognized person.

- Output: Captures real-time attendance and stores the data in a CSV file with timestamps.

### Technologies Used

- Python: Core programming language.

- OpenCV: For video capture and image processing.

- Face Recognition Library: For face detection and encoding.

- NumPy: For mathematical operations on image arrays.

- CSV File Handling: To store attendance records.

### Features

- Face Detection and Encoding: The system uses facial recognition to identify individuals. It generates 128-dimensional face encodings for each face in the database using the face_recognition library.

- Attendance Registration: Once a face is recognized, the system registers the person's attendance in a CSV file along with the time of identification. The attendance is logged with the person’s name and timestamp.

- Redundancy Avoidance: To avoid redundant attendance logging, the system ensures that the same individual is not logged repeatedly within a 24-hour period. This prevents multiple entries for the same person on the same day.

- Unknown Faces Handling: If a face does not match any known encodings in the database, it is labeled as "UNKNOWN" and not entered into the attendance log.

- Name Confirmation: To improve accuracy and reduce false positives, the system requires the recognized name to remain constant for at least 3 seconds before the attendance is registered. This ensures that transient misidentifications (e.g., due to camera movement or partial face detection) are filtered out.



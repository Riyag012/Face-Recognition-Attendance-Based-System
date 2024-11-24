# Face-Recognition-Based-Attendance-System
This project implements a real-time face recognition-based attendance system using Python, OpenCV, and the Face Recognition library. The system captures video from a webcam, identifies faces from a pre-trained dataset, and marks attendance by storing the person's name and timestamp in a CSV file.

### Content
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)

### Features
-> Face Recognition: Uses face encodings to identify individuals from the webcam feed.

-> Attendance Marking: Ensures each individual is logged only once per session, avoiding duplicates.

-> Scalable: Easily extendable to add more faces to the dataset.

-> Efficient Processing: Reduces the frame size for faster face recognition.

### Technologies Used

-> Python: Core programming language.

-> OpenCV: For video capture and image processing.

-> Face Recognition Library: For face detection and encoding.

-> NumPy: For mathematical operations on image arrays.

-> CSV File Handling: To store attendance records.

### How It Works

-> Load images from a folder (AttendanceImg) and encode faces for recognition.

-> Capture video from the webcam and process frames to detect and match faces.

-> Mark the attendance by saving the person's name and timestamp to Attendance1.csv.


# Number-Of-People-In-A-Room

 1)Overview:

The "Number of People in a Room" project is a web application implemented using Flask and OpenCV's YOLO object detection. The purpose of the project is to estimate the count of people in a room using a video feed. 

The code sets up a Flask application with multiple routes. The home route ("/") renders an HTML template for the main page. The "/classroom" route handles user input for the video feed IP address, validates it, and displays the video feed if valid.

The core functionality lies in the "generate_frames" function, which processes each frame from the video feed. It resizes the frame, performs object detection using the YOLO model, and extracts information such as bounding box coordinates, confidence scores, and centroids. It filters the detected objects to focus on people and draws bounding boxes and centroids on the frame.

The count of people is determined by the number of centroids, and it is displayed on the screen. The "/count" route allows users to retrieve the current count.

Overall, the project provides a user-friendly interface to estimate the number of people in a room using real-time object detection on a video feed.

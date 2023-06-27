# Number-Of-People-In-A-Room

 1)Overview:

The "Number of People in a Room" project is a web application implemented using Flask and OpenCV's YOLO object detection. The purpose of the project is to estimate the count of people in a room using a video feed. 

The code sets up a Flask application with multiple routes. The home route ("/") renders an HTML template for the main page. The "/classroom" route handles user input for the video feed IP address, validates it, and displays the video feed if valid.

The core functionality lies in the "generate_frames" function, which processes each frame from the video feed. It resizes the frame, performs object detection using the YOLO model, and extracts information such as bounding box coordinates, confidence scores, and centroids. It filters the detected objects to focus on people and draws bounding boxes and centroids on the frame.

The count of people is determined by the number of centroids, and it is displayed on the screen. The "/count" route allows users to retrieve the current count.

Overall, the project provides a user-friendly interface to estimate the number of people in a room using real-time object detection on a video feed.

2)Program Details:
1. The code imports necessary libraries such as Flask, OpenCV, and Ultralytics' YOLO for object detection.
   - This ensures the availability of required functionalities for the project.
2. The Flask application instance is created, which will handle incoming HTTP requests.
   - This sets up the foundation for the web application.
3. The code defines a route ("/") that renders the index.html template for the home page.
   - This provides a user interface to interact with the application.
4. The "generate_frames" function processes frames from the video feed.
   - It performs tasks such as resizing frames, object detection, and counting people.
5. Within the loop of "generate_frames":
   - The code captures frames from the video feed.
   - It resizes the frames for efficient processing.
   - It performs object detection using the YOLO model.
6. The code extracts information from the detection results.
   - It retrieves classes, confidence scores, and bounding box coordinates of detected objects.
7. The code filters the detected objects to focus on people only.
   - It selects the bounding boxes and centroids corresponding to people.
8. The detected people are visualized on the frames.
   - Bounding boxes are drawn around people.
   - Centroids are marked with circles.
9. The code counts the number of people detected and updates the global variable "count_var".
   - This variable holds the count of people detected in the video feed.
10. The frames, with visualizations and count, are converted to JPEG format and yielded as a response.
    - This allows the frames to be displayed on the web page.
11. Additional routes are defined:
    - "/video_feed" to handle the video feed, providing frames and visualizations.
    - "/stop_feed" to stop the video feed.
    - "/count" to retrieve the current count of people.
12. The script runs the Flask application on port 8000 in debug mode.
    - This ensures the application is accessible and facilitates debugging if needed.
   
3) Where can this be used?
1. Crowd management: Monitor crowd density in shopping malls, stadiums, etc., to ensure safety and manage flow.
2. Occupancy monitoring: Track room occupancy in buildings for resource optimization and scheduling.
3. Social distancing: Enforce distancing measures by alerting when the number of people exceeds limits.
4. Retail analytics: Analyze customer traffic, queue lengths, and behavior to optimize store layouts and operations.
5. Security and surveillance: Detect unauthorized individuals, count people in restricted areas, and enhance security measures.

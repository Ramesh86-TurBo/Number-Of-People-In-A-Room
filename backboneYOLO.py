# importing libraries
from flask import Flask, render_template, Response, request
import cv2
import os
import signal
from ultralytics import YOLO
import numpy as np

# global variable stores the people count
count_var = 0

# creating flask app
app = Flask(__name__)

# home route
@app.route("/")
def index():
    return render_template('index.html')


def generate_frames(ip_address):

    # access the global variable
    global count_var
    model = YOLO("yolov8m.pt")
    cap = cv2.VideoCapture(ip_address)

    while True:

        # ---------- capturing frames-----------#
        ret , frame = cap.read()
        if not ret :
            break

        # ---------- resizing the frames---------#
        frame = cv2.resize(frame , (1400,800))

        # --------- list that stores the centroids of the current frame---------#
        centr_pt_cur_fr = []

        results = model(frame)
        result = results[0]
        # print("this is results :")
        # print(results)
        print("this is shape of frame,",frame.shape)
        print("this is result :")
        print(result)

        # classes = np.array(result.boxes.names.cpu())
        # print("this is classes:",classes)

        # ------- to get the classes of the yolo model to filter out the people---------------#
        classes = np.array(result.boxes.cls.cpu(),dtype="int")
        print("this is classes:",classes)

        # ---------confidence level of detections-----------#
        confidence = np.array(result.boxes.conf.cpu())
        print("this is confidence:",confidence)

        # --------- anarray of bounding boxes---------------#
        bboxes = np.array(result.boxes.xyxy.cpu(),dtype="int")
        print("this is boxes",bboxes)

        # -------- getting indexes of the detections containing persons--------#
        idx = []
        for i in range(0,len(classes)):
            if classes[i] == 0:
                idx.append(i)

        print("these are indexes:",idx)

        # ----------- bounding boxes for person detections---------------#
        bbox = [] 
        for i in idx:
            temp = bboxes[i]
            print ("this is temp",temp)
            bbox.append(temp)
        
        # Convert to bbox to multidimensional list
        box_multi_list = [arr.tolist() for arr in bbox]
        print("this are final human detected boxes")
        print(box_multi_list)    

        # ------------ drawing of bounding boxes-------------#
        for box in box_multi_list :
            (x,y,x2,y2) = box
            
            cv2.rectangle(frame,(x,y),(x2,y2),(0,0,255),2)
            cx = int((x+x2)/2)
            cy = int((y+y2)/2)
            centr_pt_cur_fr.append((cx,cy))
            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

    

        print("this are the centroids in the current frame")
        print(centr_pt_cur_fr)

        # ------------- counting of total people in the footage ------------# 
        head_count =len(centr_pt_cur_fr)

        # counting the number of faces with count_var variable
        count_var = head_count

        # displaying the face count on the screen for experiment purpose
        cv2.putText(frame, f'{head_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # if the q is pressed the the loop is broken
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        # Convert the frame to JPEG and yeild it
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()

# video feed route
@app.route("/video_feed")
def video_feed():
    ip_address = request.args.get('ip')
    if ip_address == "0":
        ip_address = 0
    return Response(generate_frames(ip_address), mimetype='multipart/x-mixed-replace; boundary=frame')

# video stop feed route
@app.route("/stop_feed")
def stop_feed():
    os.kill(os.getpid(), signal.SIGINT)
    return "feed stopped!"

# face count route
@app.route("/count")
def count():
    return str(count_var)

# classroom route
@app.route("/classroom", methods = ['GET', 'POST'])
def classroom():

    # logic for input field validation
    if request.method == 'POST':
        
        if (request.form['ip'] == ''):
            inv_feed ="No Video-Feed!"
            return render_template('classroom.html',var2 = inv_feed)
        
        else:
            ip_address = request.form['ip']
            ip_vd_feed = "Video-Feed"
            return render_template('classroom.html', ip_address = ip_address, var2 = ip_vd_feed)
    
    if request.method == 'GET':
        return render_template('classroom.html')


# about page route
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
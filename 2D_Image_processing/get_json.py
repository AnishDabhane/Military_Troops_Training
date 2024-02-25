import cv2
import mediapipe as mp 
import numpy as np
import json

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose_name = 'img2'
image_path = "/home/anishdabhane/Projects/2nd_year/Troops/src/Mediapipe/images/img2.jpeg"
img = cv2.imread(image_path)

def calculate_angle(joint):
    global all_nodes
    #print(joint)
    a = all_nodes[joint[0]]
    b = all_nodes[joint[1]]
    c = all_nodes[joint[2]]

    start = np.array(a) # First
    middle = np.array(b) # Mid
    end = np.array(c) # End

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

if img is None:
    print("Could not open or find the image.")
else:

    with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:       
        results = pose.process(img)

        try:
            landmarks = results.pose_landmarks.landmark
        except:
            pass
         
        #print(results.pose_landmarks)

        # Render detections
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                            mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                            mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
        )               

        # gathering all coordinates
        all_nodes = []
        for i, landmark in enumerate(results.pose_landmarks.landmark):
            x = landmark.x
            y = landmark.y
            z = landmark.z
            all_nodes.append((x, y, z)) 

        # Joints
        joints = {
            "left_elbow": [15, 13, 11],
            "right_elbow": [16, 14, 12],
            "left_shoulder": [13, 11, 23],
            "right_shoulder": [14, 12, 24],
            "left_hip": [25, 23, 24],
            "right_hip": [26, 24, 23],
            "left_knee": [23, 25, 27],
            "right_knee": [24, 26, 28],
        }

        THRESHOLD = 10

        # Converting to json
        full_dict = {}
        for key, val in joints.items():
            angle = calculate_angle(val)

            angle_ranges = {
                "low": angle - THRESHOLD,
                "perfect": angle,
                "high": angle + THRESHOLD,
            }
            full_dict[key] = {
                "start_node": val[0],
                "middle_node": val[1],
                "end_node": val[2],
                "angle": angle_ranges
            }

        y = json.dumps(full_dict, indent=4)


        with open(f'poses/{pose_name}.json', 'w') as f:
            f.write(y)
            print(f'JSON file created')

        cv2.imshow('Mediapipe Feed', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



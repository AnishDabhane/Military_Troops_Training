import cv2
import mediapipe as mp 
import numpy as np
from pprint import pprint

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

image_path = "images/staff.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Could not open or find the image.")
    exit()

def calculate_angle(joint):
    global all_nodes

    a = all_nodes[joint[0]]
    b = all_nodes[joint[1]]
    c = all_nodes[joint[2]]

    start = np.array(a) # First
    middle = np.array(b) # Mid
    end = np.array(c) # End

    # similar to vectors
    SM = middle - start
    ME = end - middle

    # Calculate the dot product
    dot_product = np.dot(SM, ME)

    # Calculate the magnitudes of vectors
    magnitude_SM = np.linalg.norm(SM)
    magnitude_ME = np.linalg.norm(ME)

    # Calculate the angle in radians
    theta_radians = np.arccos(dot_product / (magnitude_SM * magnitude_ME))

    # Convert the angle to degrees
    angle = np.degrees(theta_radians)

    return angle

with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:       
    results = pose.process(img)

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

for key,value in joints.items():
    print(f"{key} : {calculate_angle(value)}")

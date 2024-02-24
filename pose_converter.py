import cv2
import mediapipe as mp 
import numpy as np
import json

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose_name = 'staff'
image_path = f"Images/kshit/{pose_name}.jpg"
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
    "elbow_left": [15, 13, 11],
    "elbow_right": [16, 14, 12],
    "shoulder_left": [13, 11, 23],
    "shoulder_right": [14, 12, 24],
    "hip_left": [25, 23, 24],
    "hip_right": [26, 24, 23],
    "knee_left": [23, 25, 27],
    "knee_right": [24, 26, 28],
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
    print(f'Poses')

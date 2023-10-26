import cv2
import mediapipe as mp
import pickle
from collections import defaultdict

userid = input(str('Enter the ID number:'))
userid = userid.lower()
print('Hello, ' + userid)

# Initialize the default dictionary to store pose landmarks
pose_landmarks_data = defaultdict(list)
mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities
landmarknum = [11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25, 26, 27, 28, 29, 30]

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Draw pose connections

def draw_styled_landmarks(image, results):

    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             )
#For live camera
#cap = cv2.VideoCapture(0)

#For uploading a video
video_path = 'C:/Users/jagad/Downloads/Walking - Side view.mp4'
cap = cv2.VideoCapture(video_path)

# Set mediapipe model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    landmark_data = []
    while cap.isOpened():
        ret, frame = cap.read()

        # Check if the video has ended
        if not ret:
            break

        # Make detections
        image, results = mediapipe_detection(frame, holistic)

        if results.pose_landmarks:

            # Iterate through pose landmarks from index 11 to 33
            for index in landmarknum:  # 11 to 33 (inclusive)
                pose_landmark = results.pose_landmarks.landmark[index]
                # Save x, y, z values in the default dictionary
                indexX = str(index) + "x"
                indexy = str(index) + "y"
                indexz = str(index) + "z"
                pose_landmarks_data[indexX].append(pose_landmark.x)
                pose_landmarks_data[indexy].append(pose_landmark.y)
                pose_landmarks_data[indexz].append(pose_landmark.z)

        # Draw landmarks
        draw_styled_landmarks(image, results)
        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        # Exit the loop when 'q' is pressed or at the end of the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

for key in pose_landmarks_data.keys():
    values = pose_landmarks_data[key]
    for value in values:
        print(f"Key: {key}, Value: {value}")

# Save the defaultdict to a file
with open(userid+'.pkl', 'wb') as file:
    pickle.dump(pose_landmarks_data, file)
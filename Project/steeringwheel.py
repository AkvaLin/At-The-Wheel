import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


def steering_wheel():
    while cap.isOpened():
        success, img = cap.read()
        cv2.waitKey(1)
        img = cv2.flip(img, 1)
        img.flags.writeable = False
        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        landmarks = results.multi_hand_landmarks
        if landmarks:

            if len(landmarks) == 2:
                left_hand_landmarks = landmarks[1].landmark
                right_hand_landmarks = landmarks[0].landmark

                shape = img.shape
                width = shape[1]
                height = shape[0]

                left_m_finger_x = (left_hand_landmarks[11].x * width)
                left_m_finger_y = (left_hand_landmarks[11].y * height)
                right_m_finger_x = (right_hand_landmarks[11].x * width)
                right_m_finger_y = (right_hand_landmarks[11].y * height)

                slope = ((right_m_finger_y - left_m_finger_y)/(right_m_finger_x-left_m_finger_x))

                sensitivity = 0.3
                if abs(slope) > sensitivity:
                    if slope < 0:
                        print("Turn left.")

                    if slope > 0:
                        print("Turn right.")

                if abs(slope) < sensitivity:
                    print("Keeping straight.")
    cap.release()

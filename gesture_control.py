import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
p_time = 0

mp_hand = mp.solutions.hands
hand = mp_hand.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hand.process(img_rgb)
    print(result.multi_hand_landmarks)

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(
        img, f'FPS: {int(fps)}', (10, 60),
        cv2.FONT_HERSHEY_PLAIN, 2,
        (0, 255, 255), 2
    )

    cv2.imshow("Web-cam", img)
    cv2.waitKey(1)

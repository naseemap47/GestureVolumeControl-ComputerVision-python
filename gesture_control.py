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
    # print(result.multi_hand_landmarks)
    lm_list = []
    if result.multi_hand_landmarks:
        for hand_lm in result.multi_hand_landmarks:
            for id, lm in enumerate(hand_lm.landmark):
                height, width, channel = img.shape
                x, y = int(lm.x * width), int(lm.y * height)
                lm_list.append([id, x, y])
                # print(lm_list)
                if len(lm_list) > 8:
                    # print(lm_list[4], lm_list[8])
                    x1, y1 = lm_list[4][1], lm_list[4][2]
                    x2, y2 = lm_list[8][1], lm_list[8][2]
                    cx, cy = (x1 + x2) // 2, (y1 + y2) //2
                    cv2.circle(img, (x1, y1), 8, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (255, 0, 255), cv2.FILLED)
                    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED)


            mp_draw.draw_landmarks(img, hand_lm, mp_hand.HAND_CONNECTIONS)

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

import cv2
import numpy as np
import mediapipe as mp

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Canvas
canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255

# Webcam
cap = cv2.VideoCapture(0)
prev_x, prev_y = 0, 0
draw_color = (0, 0, 255)  # Default: RED

# Define color buttons as hollow rectangles
color_buttons = {
    "Red":    ((10, 10, 80, 50), (0, 0, 255)),
    "Green":  ((100, 10, 80, 50), (0, 255, 0)),
    "Blue":   ((190, 10, 80, 50), (255, 0, 0)),
    "Yellow": ((280, 10, 80, 50), (0, 255, 255)),
}
clear_button = (370, 10, 100, 50)  # "Clear" button box

def is_inside(x, y, box):
    bx, by, bw, bh = box
    return bx < x < bx + bw and by < y < by + bh

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    h, w, _ = frame.shape
    fingertip = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)
            fingertip = (x, y)

            # Check if inside any color box
            for label, (box, color) in color_buttons.items():
                if is_inside(x, y, box):
                    draw_color = color
                    print(f"Color selected: {label}")

            # Check if inside clear button
            if is_inside(x, y, clear_button):
                canvas[:] = 255
                print("Canvas cleared!")

            # Draw line on canvas and camera
            else:
                if prev_x != 0 and prev_y != 0:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, 5)
                    cv2.line(frame, (prev_x, prev_y), (x, y), draw_color, 5)
                prev_x, prev_y = x, y

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        prev_x, prev_y = 0, 0

    # Draw color selection boxes (hollow)
    for label, (box, color) in color_buttons.items():
        x, y, w_, h_ = box
        cv2.rectangle(frame, (x, y), (x + w_, y + h_), color, 2)  # hollow
        cv2.putText(frame, label, (x + 10, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Draw "Clear" button (hollow)
    x, y, w_, h_ = clear_button
    cv2.rectangle(frame, (x, y), (x + w_, y + h_), (0, 0, 0), 2)
    cv2.putText(frame, "Clear", (x + 10, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # Combine camera + canvas side by side
    combined = np.hstack((frame, canvas))
    cv2.imshow("Air Drawing | Camera + Canvas", combined)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite("drawing.png", canvas)
        print("Drawing saved.")
        break
    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

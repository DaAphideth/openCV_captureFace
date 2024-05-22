import cv2
import time
cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('asas.xml')

screenshot_delay = 5  # Set the delay in seconds
last_screenshot_time = time.time()
screenshot_count = 0  # Initialize the screenshot count

cv2.namedWindow('Screenshots', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray)  # Fixed typo in the method name
    for (x, y, w, h) in faces:

        current_time = time.time()
        if current_time - last_screenshot_time >= screenshot_delay:
            # Increment the screenshot count
            screenshot_count += 1
            # Save the screenshot with the count in the filename
            # screenshot_filename = f'./screenshots/screenshot_{screenshot_count}.png'
            # cv2.imwrite(screenshot_filename, frame)
            last_screenshot_time = current_time

            # Show the screenshot in the 'Screenshots' window
            cv2.imshow('Screenshots', frame)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)  # Show the original frame with rectangles around faces
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import os

import cv2

DATA_DIR = './data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}', format(j))

    image_count = 0

    done = False
    while not done:
        ret, frame = cap.read()
        
        # Display the frame
        cv2.imshow('Collecting Images', frame)

        # Wait for the user to press a key
        key = cv2.waitKey(1) & 0xFF

        # If 'q' is pressed, exit the loop
        if key == ord('q'):
            done = True
            break

        # If 'c' is pressed, save the image
        if key == ord('c'):
            image_count += 1
            image_path = os.path.join(DATA_DIR, str(j), f'image_{image_count}.jpg')
            cv2.imwrite(image_path, frame)
            print(f"Image {image_count} saved for class {j}")

        # Break the loop if the desired number of images for this class is reached
        if image_count >= dataset_size:
            done = True
            break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
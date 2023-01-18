import face_recognition
import cv2
import datetime
import os
from os import listdir
folder_dir="/home/jadidi/PycharmProjects/BachlorProject/7th/IMG"
for images in os.listdir(folder_dir):
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg")):
        # display
        print(images)


# Open the input movie file
input_movie = cv2.VideoCapture(0)
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]
    rgb_frame = rgb_frame.copy()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(rgb_frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(rgb_frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(rgb_frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    # print("Writing frame {} / {}".format(frame_number, length))
    # output_movie.write(frame)
    cv2.imshow("img", rgb_frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

# All done!
input_movie.release()
cv2.destroyAllWindows()
'''
read from directory but without label

'''
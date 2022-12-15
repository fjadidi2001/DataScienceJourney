import face_recognition
import cv2


# Open the input movie file
input_movie = cv2.VideoCapture(0)
#length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))

# Load some sample pictures and learn how to recognize them.
fj_image = face_recognition.load_image_file("/home/jadidi/PycharmProjects/BachlorProject/7th/fateme-jadidi.jpg")
fj_face_encoding = face_recognition.face_encodings(fj_image)[0]

NR_image = face_recognition.load_image_file("NR_1.jpg")
NR_face_encoding = face_recognition.face_encodings(NR_image)[0]

AA_image = face_recognition.load_image_file("AA_2.jpg")
AA_face_encoding = face_recognition.face_encodings(AA_image)[0]

AM_image = face_recognition.load_image_file("AM_2.jpg")
AM_face_encoding = face_recognition.face_encodings(AM_image)[0]

XX_image = face_recognition.load_image_file("XX_2.jpg")
XX_face_encoding = face_recognition.face_encodings(XX_image)[0]




known_faces = [
    fj_face_encoding,
    NR_face_encoding
]

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
    rgb_frame=rgb_frame.copy()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.40)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "fatemeh jadidi"
        elif match[1]:
            name = "Mr amir"

        face_names.append(name)

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
    #print("Writing frame {} / {}".format(frame_number, length))
    #output_movie.write(frame)
    cv2.imshow("img",rgb_frame)
    cv2.waitKey(0)



# All done!
input_movie.release()
cv2.destroyAllWindows()
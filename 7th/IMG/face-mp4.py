import face_recognition
import cv2
import datetime

# Open the input movie file
input_movie = cv2.VideoCapture(0)
# length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))

# Load some sample pictures and learn how to recognize them.


FJ_image = face_recognition.load_image_file("FJ_1.jpg")
FJ_face_encoding = face_recognition.face_encodings(FJ_image)[0]

NA_image = face_recognition.load_image_file("NA_1.jpg")
NA_face_encoding = face_recognition.face_encodings(NA_image)[0]

NR_image = face_recognition.load_image_file("NR_1.jpg")
NR_face_encoding = face_recognition.face_encodings(NR_image)[0]

SK_image = face_recognition.load_image_file("SK_2.jpg")
SK_face_encoding = face_recognition.face_encodings(SK_image)[0]

AM_image = face_recognition.load_image_file("AM_2.jpg")
AM_face_encoding = face_recognition.face_encodings(AM_image)[0]

AA_image = face_recognition.load_image_file("AA_2.jpg")
AA_face_encoding = face_recognition.face_encodings(AA_image)[0]

PC_image = face_recognition.load_image_file("PC_2.jpg")
PC_face_encoding = face_recognition.face_encodings(PC_image)[0]

known_faces = [
    FJ_face_encoding,
    NA_face_encoding,
    NR_face_encoding,
    SK_face_encoding,
    AM_face_encoding,
    AA_face_encoding,
    PC_face_encoding
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
    rgb_frame = rgb_frame.copy()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.40)

        # If you had more than 2 faces, you could make this logic a lot prettier,
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "Fatemeh Jadidi"
        elif match[1]:
            name = "Dr Naeimi"
        elif match[2]:
            name = "Mr Nader Rezazade"
        elif match[3]:
            name = "ms. Shima Khosravani"
        elif match[4]:
            name = "Mr Ali Mehdizade"
        elif match[5]:
            name = "Mr Ali Ramezani"
        elif match[6]:
            name = "ms. Parto charkhkar"

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

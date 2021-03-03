import cv2
from time import sleep
import face_recognition as fr
import face_recognition as fr
import cv2
import numpy as np
import os
from openpyxl import Workbook
import datetime
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
import media
class test_code:
    #def __init__(self):
        #camera = cv2.VideoCapture(0)
        #for i in range(2):
            #return_value, image = camera.read()
            #cv2.imwrite('opencv' + str(i) + '.png', image)
            #cv2.imshow('opencv' + str(i) + '.png', image)
        #del (camera)
        """key = cv2.waitKey(1)
        webcam = cv2.VideoCapture(0)
        sleep(2)
        while True:

            try:
                check, frame = webcam.read()
                print(check)  # prints true as long as the webcam is running
                print(frame)  # prints matrix values of each framecd
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite(filename='./static/saved_img.jpg', img=frame)
                    webcam.release()
                    print("Processing image...")
                    img_ = cv2.imread('./static/saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                    print("Converting RGB image to grayscale...")
                    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    print("Converted RGB image to grayscale...")
                    print("Resizing image to 28x28 scale...")
                    img_ = cv2.resize(gray, (28, 28))
                    print("Resized...")
                    #img_resized = cv2.imwrite(filename='./static/saved_img-final.jpg', img=img_)
                    print("Image saved!")
                    webcam.release()
                    cv2.destroyAllWindows()
                    break

                elif key == ord('q'):
                    webcam.release()
                    cv2.destroyAllWindows()
                    break

            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break"""
        # Face recognition project using concept of ML

        def __init__(self):
            folder="./media/images"
            images = []
            for filename in os.listdir(folder):
                images.append(filename)
            video_capture = cv2.VideoCapture(0)
            book=Workbook()
            sheet=book.active
            # print(images)
            images_name = []
            for img in images:
                        images_name.append(fr.load_image_file(os.path.join("./media/images", img)))
            encodings = []
            for img in images_name:
                        encodings.append(fr.face_encodings(img)[0])
                    # Create array of known face encodings and their names
            known_face_encodings = []
            for encode in encodings:
                        known_face_encodings.append(encode)
            known_face_names = []
            for name in images:
                        known_face_names.append(os.path.splitext(name)[0])
                    # Initialize some variables
            face_locations = []
            face_encodings = []
            face_names = []
            process_this_frame = True
            now=datetime.datetime.now()
            today=now.day
            month=now.month
            while True:
                        # Grab a single frame of video
                        ret, frame = video_capture.read()
                        # Resize the frame of video to 1/4 size for fast process
                        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                        # Convert the image from BGR color(opencv) to RGB color(face_recognition)
                        rgb_small_frame = small_frame[:, :, ::-1]
                        # Only process every other frame of video to save time
                        if process_this_frame:
                            # Find all the faces and face encodings in the current frame of video
                            face_locations = fr.face_locations(rgb_small_frame)
                            face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
                            face_names = []
                            for face_encoding in face_encodings:
                                # See if the face is a match for known face(s)
                                matches = fr.compare_faces(known_face_encodings, face_encoding)
                                name = "10"
                                face_distances = fr.face_distance(known_face_encodings, face_encoding)
                                best_match_index = np.argmin(face_distances)
                                if matches[best_match_index]:
                                    name = known_face_names[best_match_index]
                                if int(name) in range(1,61):
                                    sheet.cell(row=int(name),column=int(today)+1).value="Present"
                                else:
                                    pass
                                face_names.append(name)
                        process_this_frame = not process_this_frame
                        # display the result
                        for (top, right, bottom, left), name in zip(face_locations, face_names):
                            top *= 4
                            right *= 4
                            bottom *= 4
                            left *= 4
                            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 225), 2)
                            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 225), cv2.FILLED)
                            font = cv2.FONT_HERSHEY_DUPLEX
                            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (225, 225, 225), 1)
                        cv2.imshow('Video', frame)
                        book.save(str(month)+'.xlsx')
                        if cv2.waitKey(1) & 0XFF == ord('q'):
                            break
            video_capture.release()
            cv2.destroyAllWindows()








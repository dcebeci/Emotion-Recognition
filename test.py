from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

def start_capturing():
    face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    classifier =load_model('./Emotion_Detection.h5')

    class_labels = ['Sinirli', 'Mutlu', 'Dogal', 'Uzgun', 'Saskin']

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                preds = classifier.predict(roi)[0]
                print("\nprediction = ", preds)
                label = class_labels[preds.argmax()]
                print("\nprediction max = ", preds.argmax())
                print("\nlabel = ", label)
                label_position = (x, y)
                cv2.putText(frame,label,label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            else:
                cv2.putText(frame,'Yuz Bulunamadi', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            print("\n\n")
        frame= cv2.resize(frame, (860, 490))
        cv2.imshow("Emotion Detector", frame)
        if cv2.waitKey(1) and (0xFF == ord("q")): # çıkma tuşu
            break
    cap.release()
    cv2.destroyAllWindows()



























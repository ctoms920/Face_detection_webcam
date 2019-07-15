import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\Cyril Tom Mathew\Desktop\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\Cyril Tom Mathew\Desktop\haarcascade_eye.xml")
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        crop_face = gray_img[y:y+h, x:x+w]
        crop = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(crop_face, 1.03, 5, 0, (40,40))
        for (p, q, r, s) in eyes:
            cv2.rectangle(crop, (p,q), (p+r,q+s), (255,0,0), 2)

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
         break

camera.release()
cv2.destroyAllWindows()

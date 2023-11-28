import cv2
import easyocr
harcascade = "Model\Harcascade_Number. xml"

cap = cv2.VideoCapture(0)

cap.set(3,640) #width
cap.set(4,480) #Height

min_area = 500
count =0
while True:
    success, img = cap.read()

    # plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "Harcascade_Number. xml")
    plate_cascade = cv2.CascadeClassifier("C:\\Users\\sahur\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_russian_plate_number.xml")

    image_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(image_grey,1.1,4)

    for (x,y,w,h)in plates:
        area = w*h
        
        if area > min_area:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)

            img_roi = img[y: y+h, x:x+w] #Cropping
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result",img)

    if cv2.waitKey(1) & 0xff == ord('s'):
        cv2.imwrite("plates/Plate_img"+str(count)+".jpg", img_roi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0), cv2.FILLED)
        cv2.putText(img,"Plate Saved",(150,265), cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
cv2.destroyAllWindows()



import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
cv2.imwrite(f"plates/Plate_img_{timestamp}.jpg", img_roi)

fps = cap.get(cv2.CAP_PROP_FPS)
cv2.putText(img, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

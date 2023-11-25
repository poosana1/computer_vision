import numpy as np
import cv2

cap = cv2.VideoCapture(0)

TARGET_SIZE = (640,360)

while(True):
    ret,im = cap.read()
    im_resized = cv2.resize(im, TARGET_SIZE)
    im_flipped = cv2.flip(im_resized, 1)    

    mask = cv2.inRange(im_flipped,(0,0,120),(50,50,255)) #inrage ทำ color threshold B ในช่วง 0-50 G ในช่วง 0-50 R ในช่วง 90-255

    cv2.imshow('mask', mask)
    cv2.moveWindow('mask',TARGET_SIZE[0],0)

    print(np.sum(mask/255)) #จะกลายเป็น 0,1  ถ้าเป็น 0 คือ สีดำ ถ้าเป็น 1 คือ สีขาว

    #อยากให้ set ให้มัน relative กับขนาดภาพ
    if(np.sum(mask/255) > 10000):   #ถ้า pixel ขาว มากกว่า 10000 จะเขียนคำว่า Coke
        cv2.putText(im_flipped,'Coke',(50,100),cv2.FONT_HERSHEY_PLAIN,10,(0,0,255))
    # pepsi
    mask_blue = cv2.inRange(im_flipped, (90, 0, 0), (255, 50, 50))
    if (np.sum(mask_blue/255) > 10000):
        cv2.putText(im_flipped, 'Pepsi', (50, 200), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0))

    # sprite
    mask_green = cv2.inRange(im_flipped, (0, 100, 0), (100, 255, 50))
    if (np.sum(mask_green/255) > 10000): 
        cv2.putText(im_flipped, 'Sprite', (50, 300), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0))

    cv2.imshow('camera', im_flipped)
    cv2.moveWindow('camera',0,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

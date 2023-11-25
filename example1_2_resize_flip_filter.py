import cv2
import numpy as np


import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret,im = cap.read()

    ############ Resizing ############################
    TARGET_SIZE = (360,240)     #ตั้งขนาดภาพ ต้องเป็น int 
    im_resized = cv2.resize(im,TARGET_SIZE)    #method resize ใช้ปรับขนาดภาพ รับ input เป็น uint8 หรือ float32 รับขนาดที่ต้องการ resize
    print(im_resized.shape)     #output ออกมาเป็น H W [B,G,R]
    ##################################################

    ############ Flipping ############################
    im_flipped = cv2.flip(im_resized,1)     #1 คือ flip ขวาซ้าย 0 คือ flip บนล่าง
    ##################################################

    ############ Blurred ############################   Linear filter เบลอขอบด้วย
    L = 30  # เลขน้อยลง blur น้อยลง
    kernel = np.ones((L, L), np.float32) / L / L
    im_blurred = cv2.filter2D(im_flipped, -1, kernel)
    ##################################################
    
    ############ Median Filter ####################### ไม่เบลอขอบ
    L = 25  
    im_median = cv2.medianBlur(im_flipped, L)
    ##################################################

    cv2.imshow('original', im)
    cv2.imshow('modified', im_blurred) # Change variable name for displaying another images 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

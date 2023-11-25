import cv2

cap = cv2.VideoCapture(0)

TARGET_SIZE = (640,360)

while(True):
    ret,im = cap.read()
    im_resized = cv2.resize(im, TARGET_SIZE)
    im_flipped = cv2.flip(im_resized, 1)

    im_gray = cv2.cvtColor(im_flipped,cv2.COLOR_BGR2GRAY)   #convert color จาก BGR to Gray
    im_hsv = cv2.cvtColor(im_flipped, cv2.COLOR_BGR2HSV)    #convert color จาก BGR to HSV
    hue = im_hsv[:,:,0]
    hue = cv2.applyColorMap((hue*(255/179)).astype('uint8'),cv2.COLORMAP_HSV)
    sat = im_hsv[:,:,1]
    val = im_hsv[:,:,2]

    cv2.imshow('Gray', im_gray)
    cv2.moveWindow('Gray',0,0)
    cv2.imshow('Hue', hue)
    cv2.moveWindow('Hue',TARGET_SIZE[0],0)
    cv2.imshow('Sat', sat)
    cv2.moveWindow('Sat',0,TARGET_SIZE[1])
    cv2.imshow('Val', val)
    cv2.moveWindow('Val',TARGET_SIZE[0],TARGET_SIZE[1])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

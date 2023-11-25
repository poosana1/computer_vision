import cv2
print(cv2.__version__)

cap = cv2.VideoCapture(0)   #VideoCapture ใช้ติดต่อกับกล้อง 0 คือกล้องตัวแรก

#CAP_SIZE = (1280,720)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_SIZE[0])
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_SIZE[1])

ret,im = cap.read()     #method read จะคืนค่า 2 ค่า คือ ret กับ im ถ้า ret คือ true แสดงว่าอ่านภาพได้ถูกต้อง im คือภาพที่อ่านได้

print(im.shape)     #return แถว หลัก และ ช่องสี [B,G,R]
print(type(im))     #type เป็น numpy.ndarray
print(im[0,0])      #สี pixel แรก
print(im[0,0,0])    #สี blue ของ pixel แรก
print(type(im[0,0,0]))      #type เป็น numpy.uint8 เก็บค่าได้ 0-255

cv2.imshow('camera',im)     #method imshow ใช้แสดงภาพ รับ input เป็น uint8 หรือ float32
cv2.imshow('blue channel',im[:,:,0])        #เอาทุกแถว ทุกหลัก และเอาแค่ช่องสี blue
cv2.imshow('green channel',im[:,:,1])       #เอาทุกแถว ทุกหลัก และเอาแค่ช่องสี green
cv2.imshow('red channel',im[:,:,2])        #เอาทุกแถว ทุกหลัก และเอาแค่ช่องสี red
cv2.waitKey()       #method waitKey ให้ค้างหน้าจอไว้ จนกว่าจะมีการกดปุ่มใดๆ
cap.release()       #หยุดการเชื่อมต่อกับกล้อง

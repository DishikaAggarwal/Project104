import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,"Mercury",(105,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(285,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(385,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(550,370),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(780,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(965,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1110,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("solar",img)
cv2.imwrite("solar-system-with-names.jpg",img)

cv2.waitKey(0)

print(img)




import numpy as np
import cv2
from pyzbar.pyzbar import decode

#img = cv2.imread("./images/mix.jpg")
cap = cv2.VideoCapture(0)

with open("data.txt") as t:
    passwords=t.read().splitlines()

print(passwords)
while True:
    ret, img = cap.read()
    codes = decode(img)
    for code in codes:
        data = code.data.decode("utf-8")
        print(data)
        x, y, z, w = code.rect
        if data in passwords:
            col=(0,255,0)
        else:
            col=(0,0,255)

        cv2.rectangle(img, (x, y), (x + z, y + w), col, 2)
        typ = code.type
        txt = f"{data} : {typ}"
        cv2.putText(img, txt, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0), 2)

    cv2.imshow("Image",img)
    k=cv2.waitKey(10)
    if k==27:
        break;

cap.release()
cv2.destroyAllWindows()

'''
cv2.imshow("qr",img)
cv2.waitKey(0)
'''
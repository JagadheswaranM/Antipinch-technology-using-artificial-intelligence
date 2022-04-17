import cv2
import numpy as np

# SENDER

import socket

ip = "localhost"
port = 8089
msg = b"You are a Champion"

print(f'Sending {msg} to {ip}:{port}')

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('palm.xml')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.1, 5)
    for(x,y,w,h) in hands:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('Frame', frame)
    if (hands==( )):
        msg = b'1'
        print (msg)
    else:
        msg = b'0'
        print (msg)
    sock.sendto(msg, (ip, port))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

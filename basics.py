import os

import cv2
import face_recognition
import numpy as np

path = 'images'


ronaldoimg = face_recognition.load_image_file('ronaldo.jpg')
ronaldoimg = cv2.cvtColor(ronaldoimg, cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('ronaldo_test.jpg')
imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(ronaldoimg)[0]
encodeRonaldo = face_recognition.face_encodings(ronaldoimg)[0]
cv2.rectangle(ronaldoimg, (faceloc[3], faceloc[0]),
              (faceloc[1], faceloc[2]), (255, 0, 255), 2)

faceloc = face_recognition.face_locations(imgtest)[0]
encodeRonaldo = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest, (faceloc[3], faceloc[0]),
              (faceloc[1], faceloc[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeRonaldo], encodeRonaldo)
facedis = face_recognition.face_distance([encodeRonaldo], encodeRonaldo)
print(results, facedis)


cv2.imshow('Ronaldo', ronaldoimg)
cv2.imshow('Ronaldo Test', imgtest)
cv2.waitKey(0)

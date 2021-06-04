
#from PyQt5.QtGui import QImage, QPixmap
#from PyQt5.uic import loadUi
#from PyQt5.QtCore import pyqtSlot, QTimer
#from PyQt5.QtWidgets import QDialog
import cv2
import face_recognition
import numpy as np
import datetime
import os




path ='C:/Users\SHUBHAM_2018\Desktop\intership attendance system\code\ImagesAttendance'
if not os.path.exists(path):
    os.mkdir(path)
        # known face encoding and known face name list
images = []
class_names = []
encode_list = []
attendance_list = os.listdir(path)
        # print(attendance_list)
for cl in attendance_list:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    class_names.append(os.path.splitext(cl)[0])
for img in images:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
           # boxes = face_recognition.face_locations(img)
            #encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
    encode = face_recognition.face_encodings(img)[0]
    encode_list.append(encode)

 
  
path = 'C://Users\SHUBHAM_2018\Desktop\intership attendance system\code\sentimage'
if not os.path.exists(path):
    os.mkdir(path)
            
            
images1 = []
class_names1 = []
encode_list1 = []
attendance_list1 = os.listdir(path)
print(attendance_list)
for cl in attendance_list1:
    cur_img1 = cv2.imread(f'{path}/{cl}')
    images1.append(cur_img1)
    class_names1.append(os.path.splitext(cl)[0])
for img in images1:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
           
    encode = face_recognition.face_encodings(img)[0]
    encode_list1.append(encode)


for encodeFace in encode_list:

    match = face_recognition.compare_faces(encode_list1, encodeFace, tolerance=0.50)
    face_dis = face_recognition.face_distance(encode_list1, encodeFace)
    #print(face_dis)
    best_match_index = np.argmin(face_dis)
    #print(class_names1)
    #print(best_match_index)
    if match[best_match_index]:
            name = class_names1[best_match_index].upper()
            print(name)   
    

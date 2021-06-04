from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QDialog
import cv2
import face_recognition
import numpy as np
import datetime
import os




path ='C://Users\SHUBHAM_2018\Desktop\intership attendance system\code\ImagesAttendance'
#if not os.path.exists(path):
    #os.mkdir(path)
        # known face encoding and known face name list

images = []
class_names = []
encode_list = []
attendance_list = os.listdir(path)
print(attendance_list)

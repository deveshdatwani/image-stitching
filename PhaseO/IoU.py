box1 = [[200,400],[600,800]]
box2 = [[600,700],[500,400]]

xLeft = max(box1[0][0], box2[0][0])
yLeft = max(box1[0][1], box2[0][1])

xRight = min(box1[1][0], box2[1][0])
yRight = min(box1[1][1], box2[1][1])

width = max(0, xRight-xLeft)
height = max(0, yRight-yLeft)

print(f'left X = {xLeft}')
print(f'width = {width}')
print(f'heoght = {height}')

area = width * height

print(f'The area of IoU is {area}')

import cv2 
import numpy as np
from matplotlib import pyplot as plt

image = np.ones((1000,1000,3))
image = cv2.rectangle(image, box1[1], box1[0], [0,0,0])
image = cv2.rectangle(image, box2[1], box2[0], [0,0,0])

from FastIoI import IoU_calculator

BOX1 = []
BOX2 = []

for i in box1:
    BOX1.append(i[0])
    BOX1.append(i[1])

for i in box2:
    BOX2.append(i[0])
    BOX2.append(i[1])

areaIOU = IoU_calculator(BOX1, BOX2)
print(f'FAST IOU IS {areaIOU}')

print(BOX1)
print(BOX2)
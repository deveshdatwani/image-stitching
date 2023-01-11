import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from PIL import Image
import json

global labels 
labels = dict()

class CreateHomographyData():
    def __init__(self):
        self.basePath = "/home/deveshdatwani/Stitching/PhaseO/Train/val2017/"
        self.labelPath = "/home/deveshdatwani/Stitching/PhaseO/Train/trainlabel.json"

    def createImageSet(self, imagePath):
        global labels
        image = cv2.imread(imagePath)
        #image = cv2.resize(image, (1000,1000))
        topLeft = np.array([100,50])
        bottomLeft = np.array([200,50])
        topRight = np.array([topLeft[0], topLeft[1]+100])
        bottomRight = np.array([bottomLeft[0], bottomLeft[1]+100])
        
        R1 = np.random.randint(-20,20)
        R2 = np.random.randint(-20,20)
        R3 = np.random.randint(-20,20) 
        R4 = np.random.randint(-20,20)

        Image1 = image[topLeft[0]:bottomLeft[0], topLeft[1]:topRight[1], :]
        newtopLeft = topLeft + R1
        newbottomLeft = bottomLeft + R2
        newtopRight = topRight + R3
        newbottomRight = bottomRight + R4
        transformation = cv2.getPerspectiveTransform(np.float32([topLeft, topRight, bottomLeft, bottomRight]), np.float32([newtopLeft, newtopRight, newbottomLeft, newbottomRight]))
        transformedImage = cv2.warpPerspective(image, transformation, dsize=(image.shape[1], image.shape[0]))
        Image2 = transformedImage[topLeft[0]:bottomLeft[0], topLeft[1]:topRight[1], :]
        
        dataPathOne = "/home/deveshdatwani/Stitching/PhaseO/Train/Images/viewOne/" + imagePath.split("/")[7] 
        dataPathTwo = "/home/deveshdatwani/Stitching/PhaseO/Train/Images/viewTwo/" + imagePath.split("/")[7]

        try:
            cv2.imwrite(dataPathOne, Image1)
            cv2.imwrite(dataPathTwo, Image2)
            print(imagePath)
        except Exception as e:
            pass

        labels[imagePath] = tuple(map(tuple, transformation))

        return None

    def create(self):
        for i in os.listdir(self.basePath):
            imagePath = self.basePath + i
            self.createImageSet(imagePath)
        with open(self.labelPath, 'w') as fp:
            json.dump(labels, fp)
    
     
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

def createImageSet(imagePath):
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (1000,1000))
    topLeft = np.array([400,400])
    bottomLeft = np.array([800,400])
    topRight = np.array([topLeft[0], topLeft[1]+400])
    bottomRight = np.array([bottomLeft[0], bottomLeft[1]+400])
    
    R1 = np.random.randint(-100,100)
    R2 = np.random.randint(-100,100)
    R3 = np.random.randint(-100,100) 
    R4 = np.random.randint(-100,100)

    Image1 = image[topLeft[1]:topRight[1], bottomLeft[1]:bottomRight[1], :]
    newtopLeft = topLeft + R1
    newbottomLeft = bottomLeft + R2
    newtopRight = topRight + R3
    newbottomRight = bottomRight + R4
    transformation = cv2.getPerspectiveTransform(np.float32([topLeft, topRight, bottomLeft, bottomRight]), np.float32([newtopLeft, newtopRight, newbottomLeft, newbottomRight]))
    transformedImage = cv2.warpPerspective(image, transformation, dsize=(image.shape[1], image.shape[0]))
    Image2 = transformedImage[topLeft[1]:topRight[1], bottomLeft[1]:bottomRight[1], :]
    dataInstance = np.dstack(Image1, Image2)
    cv2.imwrite(dataInstance, "something")
    #Write lagel

    return None

if __name__ == "__main__":
    for i in os.listdir():
        imagePath = i
        createImageSet(imagePath) 

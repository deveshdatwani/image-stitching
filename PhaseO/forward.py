from network import HomographyNet
import cv2
import numpy as np

if __name__ == "__main__":
    model = HomographyNet()
    filename = "000000000139.jpg"
    path1 = "/home/deveshdatwani/Stitching/PhaseO/Train/Images/viewOne/"
    path2 = "/home/deveshdatwani/Stitching/PhaseO/Train/Images/viewTwo/"
    image1 = cv2.imread(path1 + filename)
    image2 = cv2.imread(path2 + filename)
    IMAGE = np.dstack((image1, image2))
    output = model(IMAGE) 
    
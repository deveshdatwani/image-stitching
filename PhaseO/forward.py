from network import HomographyNet
import cv2
import numpy as np
import torch
from torchvision.io import read_image

if __name__ == "__main__":
    model = HomographyNet()
    filename = "000000000139.jpg"
    path1 = "/home/deveshdatwani/Stitching/PhaseO/Train/Images/viewOne/"
    path2 = "/home/deveshdatwani/Stitching/PhaseO/Train/Images/viewTwo/"
    image1 = read_image(path1 + filename)
    image2 = read_image(path2 + filename)
    IMAGE = torch.stack((image1, image2))
    print(IMAGE.shape)
    output = model(image1.float()) 
    print(output)
    
    
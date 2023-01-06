import os
import torch
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import json

class HomographySet(Dataset):

    def __init__(self, root_dir="/home/deveshdatwani/Stitching/PhaseO/Train/Images", transform=None):
        self.root_dir = root_dir
        with open("/home/deveshdatwani/Stitching/PhaseO/Train/Labels/groun.json", "r") as file:
            data = json.load(file)
        self.labels = data

    def __len__(self):
        
        return len(self.landmarks_frame)

    def __getitem__(self, idx):
        rootOne = self.root_dir + "/viewOne/"
        rootTwo = self.root_dir + "/viewTwo/"
        imgOne_name = os.path.join(rootOne, list(self.labels.keys())[idx])
        imgTwo_name = os.path.join(rootOne, list(self.labels.keys())[idx])
        image1 = io.imread(imgOne_name)
        image2 = io.imread(imgTwo_name)
        image = np.dstack((image1, image2))
        transformation = list(self.labels.items())[idx]
        transformation = [j for sub in transformation for j in sub]
        sample = {'image': image, 'ground_truth': transformation}

        return sample


if __name__ == "__main__":
    face_dataset = HomographySet()
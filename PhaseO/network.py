from torch import nn
import torch.nn.functional as F

class HomographyNet(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 3, 1, padding="same")
        self.conv2 = nn.Conv2d(64, 64, 3, 1, padding="same")
        self.max = nn.MaxPool2d(4, 1)
        self.conv3 = nn.Conv2d(64, 64, 3, 1, padding="same")
        self.conv4 = nn.Conv2d(64, 64, 3, 1, padding="same")
        self.conv5 = nn.Conv2d(64, 128, 3, 1, padding="same")
        self.conv6 = nn.Conv2d(128, 128, 3, 1, padding="same")
        self.conv7 = nn.Conv2d(128, 64, 3, 1, padding="same")
        self.conv8 = nn.Conv2d(64, 32, 3, 1, padding="same")
        self.fullyConnected1 = nn.Linear(264992, 1024, bias=True)
        self.fullyConnected2 = nn.Linear(1024, 8)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.max(x)
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = self.max(x)
        x = F.relu(self.conv5(x))
        x = F.relu(self.conv6(x))
        x = self.max(x)
        x = F.relu(self.conv7(x))
        x = F.relu(self.conv8(x))
        x = x.reshape(-1, 264992)
        x = F.relu(self.fullyConnected1(x))
        x = self.fullyConnected2(x)
        
        return x

    def lossFunction(self, x):
        return None

    def trainStep(self, x, trainLoader, epochs=10, batchSize=8):
        optimizer = self.optimizer
        trainSize = len(trainLoader)
        for epoch in range(epochs):
            for batchIdx, (data,target) in enumerate(trainLoader):
                optimizer.zero_grad()
                out = self.model(data)
                loss = nn.MSELoss(target, out)
                loss.backward()
                optimizer.step()
                if batchIdx & 20 == 0:
                    print(f'Train epoch {epoch} iteration {batchIdx} / {trainSize}')                    

        return None

    def validateStep(self):
        return None

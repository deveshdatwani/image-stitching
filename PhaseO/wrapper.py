from network import HomographyNet
from torch.nn import optim

if __name__ == "__main__":
    model = HomographyNet()
    model.optimizer = optim.Adam(model.parameters(), lr=0.01)
    model.trainStep()
import torch
import torchvision
import torchvision.transforms as T
from torch import nn, optim


def main():
    transform = T.Compose([T.ToTensor()])
    train = torchvision.datasets.FakeData(transform=transform)
    loader = torch.utils.data.DataLoader(train, batch_size=32, shuffle=True)

    model = nn.Sequential(nn.Flatten(), nn.Linear(3*224*224, 10))
    opt = optim.Adam(model.parameters(), lr=1e-3)
    lossf = nn.CrossEntropyLoss()

    for i, (x,y) in enumerate(loader):
        opt.zero_grad()
        out = model(x)
        loss = lossf(out, y)
        loss.backward()
        opt.step()
        if i % 10 == 0:
            print("step", i, "loss", float(loss))
        if i == 30:
            break


if __name__ == "__main__":
    main()

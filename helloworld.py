import torch
from torch import nn


def init_weight(m):
    if type(m) == nn.Linear:
        print(m.weight)


net = nn.Sequential(nn.Flatten(), nn.Linear(10, 4))
net.apply(init_weight)
torch.arange()
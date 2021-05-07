#%% md

# 5.4 池化层

#%%

import torch
from torch import nn

print(torch.__version__)

#%% md

## 5.4.1 二维最大池化层和平均池化层

#%%

def pool2d(X, pool_size, mode='max'):
    X = X.float()
    p_h, p_w = pool_size
    Y = torch.zeros(X.shape[0] - p_h + 1, X.shape[1] - p_w + 1)
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode == 'max':
                Y[i, j] = X[i: i + p_h, j: j + p_w].max()
            elif mode == 'avg':
                Y[i, j] = X[i: i + p_h, j: j + p_w].mean()
    return Y

#%%

X = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
pool2d(X, (2, 2))

#%%

pool2d(X, (2, 2), 'avg')

#%% md

## 5.4.2 填充和步幅

#%%

X = torch.arange(16, dtype=torch.float).view((1, 1, 4, 4))
X

#%%

pool2d = nn.MaxPool2d(3)
pool2d(X)

#%%

pool2d = nn.MaxPool2d(3, padding=1, stride=2)
pool2d(X)

#%%

pool2d = nn.MaxPool2d((2, 4), padding=(1, 2), stride=(2, 3))
pool2d(X)

#%% md

## 5.4.3 多通道

#%%

X = torch.cat((X, X + 1), dim=1)
X

#%%

pool2d = nn.MaxPool2d(3, padding=1, stride=2)
pool2d(X)

#%%



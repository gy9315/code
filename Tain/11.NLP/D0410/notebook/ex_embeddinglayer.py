import torch.nn as nn
import torch
# an Embedding module containing 10 tensors of size 3
embedding = nn.Embedding(12, 3)
# a batch of 2 samples of 4 indices each
input = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 11]])
a=embedding(input)
print(a[0])


# # example with padding_idx
# embedding = nn.Embedding(10, 3, padding_idx=0)
# input = torch.LongTensor([[0, 2, 0, 5]])
# embedding(input)

# # example of changing `pad` vector
# padding_idx = 0
# embedding = nn.Embedding(3, 3, padding_idx=padding_idx)
# embedding.weight
# with torch.no_grad():
#     embedding.weight[padding_idx] = torch.ones(3)
# embedding.weight
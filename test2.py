import torch
import model
log = torch.load('logs/2017-08-04_00.55.19.pth')
tokens = len(log['vocab']['question']) + 1

net = torch.nn.DataParallel(model.Net(tokens))
net = net.load_state_dict(log['weights'])
print(net)
print(type(net))
img = '/datasets/home/49/049/s2solomo/show_tell2/show-attend-and-tell-tensorflow/image/val2014/COCO_val2014_000000581929.jpg'


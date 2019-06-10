# ECE285_Jarvis_ProjectA
# Implementation of Visual Question Answering

This code is an implementation based on Vahid Kazemi and Ali Elqursh's paper Show, Ask, Attend, and Answer: A Strong Baseline For Visual Question Answering using PyTorch. This is part of the final project for the UCSD course Machine Learning for Image Processing in Spring 2019

Pre-trained model (50epoch.pth) available at https://github.com/snagiri/ECE285_Jarvis_ProjectA/releases/tag/v1.0

## To run a demo:
To demo the model, run the '''demo.ipynb''' jupyter notebook

## To train the model:
- Change the parameters in config.py
- run '''python train.py <path-to-save-model>'''

## File Structure:

```
Root
|
+----efforts
|    (contains other models we tried during our experiments)
|
+----resnet
|    - other folders

```

### Required Packages:

1. torch
2. h5py
3. tqdm
4. pillow
5. json

For installing these packages, you can use either pip to install packages. For example,

```
pip install torch
```

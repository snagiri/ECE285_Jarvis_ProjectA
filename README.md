# ECE285_Jarvis_ProjectA
# Implementation of Visual Question Answering

This code is an implementation based on Vahid Kazemi and Ali Elqursh's paper Show, Ask, Attend, and Answer: A Strong Baseline For Visual Question Answering using PyTorch. This is part of the final project for the UCSD course Machine Learning for Image Processing in Spring 2019

Pre-trained model (50epoch.pth) is available [here](https://github.com/snagiri/ECE285_Jarvis_ProjectA/releases/tag/v1.0)

## To run a demo:
To demo the model, run the `demo.ipynb` jupyter notebook

## To train the model:
- Change the parameters in config.py
- run `python train.py <path-to-save-model>`

## File Structure:
### A typical top-level directory layout
.
    ├── efforts                 # Other models we tried
        ├── 
        ├──
        ├──
        ├──
    ├── resnet                  # Documentation files (alternatively `doc`)
        ├── config.py           # Parameters for training the model
        ├── data.py             # 
        ├──
        ├──
        ├──
    ├── config.py               # Contains parameters for training the model
    ├── data.py                 # Data loaders for the dataset
    ├── demo.ipynb              # Notebook to run the demo
    ├── dogs.jpg                # Image used in demo
    ├── model.py                # File to build the neural net in
    ├── preprocess-images.py    # Extract features from images
    ├── preprocess-vocab.py     # Do word embedding
    ├── tennis.jpg              # Image used in demo
    ├── test_img.jpg            # Image used in demo
    ├── train.py                # To train the model
    ├── utils.py                # Contains some utility functions
    ├── vocab.json              # Vocabulary file created during training
    └── README.md

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

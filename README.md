# Implementation of Visual Question Answering
## ECE285_Jarvis_ProjectA

This code is an implementation based on Vahid Kazemi and Ali Elqursh's paper Show, Ask, Attend, and Answer: A Strong Baseline For Visual Question Answering using PyTorch. This is part of the final project for the UCSD course Machine Learning for Image Processing in Spring 2019

Pre-trained model (50epoch.pth) is available [here](https://github.com/snagiri/ECE285_Jarvis_ProjectA/releases/tag/v1.0)

## To run a demo:
To demo the model, run the `demo.ipynb` jupyter notebook

## To train the model:
- Change the parameters in config.py
- run `python train.py <path-to-save-model>`

## File Structure:

    .
    ├── efforts                             # Other models we tried
    |   ├── Bottom-up-attention-imp         # Implementation of https://arxiv.org/abs/1708.02711 paper
    |   ├── san-vqa-tensorflow              # Implementation of https://arxiv.org/pdf/1511.02274.pdf paper 
    |   ├── Show_Attend_and_Tell_beam       # Implementation of https://arxiv.org/pdf/1502.03044.pdf paper 
    |   ├── show_attend_and_tell            # Implementation of https://arxiv.org/pdf/1502.03044.pdf paper 
    ├── resnet                              
    |   ├── convert.py                      # Used to build resnet model
    |   ├── convert2.py                     # Used to build resnet model
    |   ├── resnet.py                       # Used to build resnet model
    |   ├── synset.py                       # Used to build resnet model
    ├── config.py                           # Contains parameters for training the model
    ├── data.py                             # Data loaders for the dataset
    ├── demo.ipynb                          # Notebook to run the demo
    ├── dogs.jpg                            # Image used in demo
    ├── model.py                            # File to build the neural net in
    ├── preprocess-images.py                # Extract features from images
    ├── preprocess-vocab.py                 # Do word embedding
    ├── tennis.jpg                          # Image used in demo
    ├── test_img.jpg                        # Image used in demo
    ├── train.py                            # To train the model
    ├── utils.py                            # Contains some utility functions
    ├── vocab.json                          # Vocabulary file created during training
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

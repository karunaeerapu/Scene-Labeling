# Scene Labeling with Recurrent Convolutional Neural Networks

## Overview
This project implements a "Recurrent Convolutional Neural Network" (rCNN) for scene labeling,
as seen in [Pinheiro et al, 2014](http://www.jmlr.org/proceedings/papers/v32/pinheiro14.pdf).

### Summary of files
    README.md           -- README file
    category_maps/      -- Text files containing category info for Stanford  & "Data from Games" datasets
    model.py            -- Code for rCNN model
    preprocessing.py    -- Code for processing input data
    requirements.txt    -- Lists python package requirements
    test/		-- Contains unit tests and sample data
    train.py            -- Script for training and evaluating model

## Installation
 1. Clone or download this repository to your computer:

    ```git clone https://github.com/rkargon/Scene-Labeling.git```

 2. Install the necessary Python requirements through `pip`:

    ```pip install -r requirements.txt```

    This project only requires Tensorflow version 11, and PIL for image manipulation.

 3. Download a dataset with which to use the model.
 We used the [Stanford Background Dataset](http://dags.stanford.edu/projects/scenedataset.html) which has 700+ 320x240 images and 8 classes.
 The code also works with the [Data from Games](https://download.visinf.tu-darmstadt.de/data/from_games/)
 dataset, which has 25,000 1914 × 1052 with 38 categories.

    To use another dataset, make sure it is organized similarly to one of the above two, and specify while training and testing which dataset it is "mimicking".
  Specifically, both datasets had the data in one folder, with subfolders "labels" and "images" for labels and images, respectively.
  The stanford dataset had labels in the format of space-separated digits in a text file, while the "Data from  Games" dataset had labels in the form of paletted images,
   where each color corresponds to a different label.

  4. Generate a text file that maps colors to category numbers nad labels. Each line of the file has five space-separated values:


      R  G  B category_num category_id

   R,G,B values should be in the range [0,1].
   Category files for the Stanford Background and Data From Games datasets are provided in the folder `category_maps`.

## Running

### Training
For training, use the `train.py` script with the `--training` flag. The following command trains the model on the Stanford dataset:

    python train.py --training --dataset stanford-bground --category_map category_maps/stanford_bground_categories.txt --data_dir <STANFORD DATA FOLDER> --model_save_path <SAVED_MODEL_FILE>


Running `train.py -h` will show additional parameters for the script, including different hyperparameters.

### Testing
For testing, use the `train.py` script without the `--training` flag.
This script will get per-class accuracies for each image, as well as output predicted labels as image files.
The following command loads a saved model and evaluates accuracy on the stanford data set:

    python train.py --model <SAVED_MODEL> --category_map category_maps/stanford_bground_categories.txt --dataset stanford-bground --data_dir <STANFORD DATA FOLDER> --output_dir <RESULT IMAGES FOLDER>


This outputs per-clas accuracies for each layer of the recurrent rCNN, and also saves predicted labels for each layer.

## Credits

This was originally submitted as a final project for Dr. Thomas Serre's <u>Computational Vision (CLPS1520)</u> course at Brown University.
The code for the original project may be found at: https://github.com/NP-coder/CLPS1520Project

 - Tyler Barnes-Diana
 - Zhenhao Hou (Andrew)
 - Jae Hwan Hwang (James)
 - Raphael Kargon

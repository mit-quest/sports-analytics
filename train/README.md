### Prepare a dataset for training and testing a player identification model

Prerequisite artifacts:
* A formatted dataset CSV (in a GCP bucket) we will use to create train and test sets

Infrastructure that will be used:
* A GCP bucket where the dataset CSV will be accessed from & model files are written to
* A GCP virtual machine to train on

### Workflow

1. If you do not already have a formatted dataset CSV, see the previous workflow [Prepare a dataset for training and testing a player identification model](../dataset_preparation/README.md).

1. If you have continued from the previous workflow, you should still be `ssh`ed into a GCP VM with all relevant files available at their respective mount points.

#### Training a new model

1. In the `ssh` session, enter `python train/train.py`.

#### Testing a trained model

1. In the `ssh` session, enter `python train/test.py`.
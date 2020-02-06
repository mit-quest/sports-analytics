# Sports Analytics
## Pose-based player identification from  video

![](img/barcelona_demo.gif)
<sub>*Skeletal key point estimation on soccer players using [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)*</sub>

The way that professional athletes play their sport is sufficiently unique that just a few moves on the field or court can be enough for a computer vision model to distinguish them from their teammates and competitors.

Using pose estimation models, such as [CMU’s OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), we extract key points representing athletes’ skeletal positions from video recordings of their competitions. These skeletal key points are then used to train a neural network to predict a particular athlete’s identity from unseen footage. To accomplish this, there are five workflows that this repository supports:

* [data ingestion](data_ingestion): copying prepared video data into the cloud for storage and usage
* [pose extraction](pose_extraction): extracting skeletal keypoints from videos with OpenPose
* [dataset preparation](dataset_preparation): preparing a dataset for training and testing a player identification model
* [training](train): training and testing a player identification model on a prepared dataset
* [inference](infer): using a pretrained player identification model with a prepared dataset

Before running any of these workflows, you'll need to [set up your local machine](docs/local_setup.md) and [have a GCP account ready](https://cloud.google.com/). 
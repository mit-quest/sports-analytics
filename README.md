# Sports Analytics
## Pose-based player identification from  video

![](img/barcelona_demo.gif)

The way that professional athletes play their sport is sufficiently unique that just a few moves on the field or court can be enough for a computer vision model to distinguish them from their teammates and competitors.

Using pose estimation models, such as [CMU’s OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), we extract key points representing athletes’ skeletal positions from video recordings of their competitions. These skeletal key points are then used to train a neural network to predict a particular athlete’s identity from unseen footage. To accomplish this, there are five workflows that this repository supports:

* [data ingestion](data_ingestion): copying prepared video data into the cloud for storage and usage
* [pose extraction](pose_extraction): extracting skeletal keypoints from videos with OpenPose
* [dataset preparation](dataset_preparation): preparing a dataset for training and testing of a player identification model
* [training](train): training a player identification model on a prepared dataset
* [testing](test): testing a pretrained player identification model on a prepared dataset

Before running any of these workflows, you'll need to [set up your local machine](docs/local_setup.md) and [have a GCP account ready](https://cloud.google.com/). You may also want to look through [assumed knowledge](). TO DO: add link

---
### Demo

We've provided a [Colab notebook]() that will automatically download a prepared dataset and run a pretrained player identification model.

The demo dataset was curated from videos of two matches at Wimbledon 2018 provided by the [Wimbledon YouTube Channel](https://www.youtube.com/wimbledon). The model was trained on clips from [Novak Djokovic vs Rafael Nadal](https://www.youtube.com/watch?v=V96sSCV03ng) and is tested on unseen clips from that match (88.6% accuracy: Nadal 83.5%, Del Potro 95.5%), as well as clips from [Juan Martin del Potro vs Rafael Nadal](https://www.youtube.com/watch?v=S5LVbZUgM48) (76.5% accuracy: Nadal 86.5%, ”not Nadal” 65.2%).

TODO: image

---


#### **3. Prepare a dataset for training and testing of a player identification model**

#### **4. Train a player identification model**

#### **5. Test a pretrained player identification model**
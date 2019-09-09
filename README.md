# Sports Analytics
## Pose-based player identification from  video

TODO: image

The way that professional athletes play their sport is sufficiently unique that just a few moves on the field or court can be enough for a computer vision model to distinguish them from their teammates and competitors.

Using pose estimation models, such as [CMU’s OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), we extract key points representing athletes’ skeletal positions from video recordings of their competitions. These skeletal key points are then used to train a neural network to predict a particular athlete’s identity from unseen footage. To accomplish this, there are four workflows that this repository supports:

* copying prepared video data into the cloud for storage and usage
* preparing a dataset for training and testing of a player identification model
* training a player identification model on a prepared dataset
* testing a pretrained player identification model on a prepared dataset

---
### Demo

We've provided a script that will automatically download a prepared dataset and run a pretrained player identification model.

The demo dataset was curated from videos of two matches at Wimbledon 2018 provided by the [Wimbledon YouTube Channel](https://www.youtube.com/wimbledon). The model was trained on clips from [Novak Djokovic vs Rafael Nadal](https://www.youtube.com/watch?v=V96sSCV03ng) and is tested on unseen clips from that match (88.6% accuracy: Nadal 83.5%, Del Potro 95.5%), as well as clips from [Juan Martin del Potro vs Rafael Nadal](https://www.youtube.com/watch?v=S5LVbZUgM48) (76.5% accuracy: Nadal 86.5%, ”not Nadal” 65.2%).

TODO: image

1. Open a terminal and clone this repository:
`git clone git@github.com:mit-quest/sports-analytics.git`

2. Enter main directory: `cd sports-analytics`

3.  Run demo script: `./run_demo`

---
### Train your own model

**Note**: Each of the following steps, from video pre-processing to running pose estimation and training player ID models, can be computationally expensive. We therefore strongly recommend proceeding with a GPU-provisioned system, and provide instructions for running pose extraction and model training on a VM.

**Suggested background**
* [Python 1]()
* [Cloud 1]()
* [Applied ML: Image 2]() 

#### **1. Prepare data**

For player identification, your data should consist of a single directory containing a subdirectory with clips for each player.* Each clip should ideally contain only that one individual, but multi-person clips where the individual is the primary focus in the foreground will work as well if you are using our provided configuration of OpenPose to extract skeletal key points.

Given the specificity of each use case, we leave it up to you to prepare your video data appropriately. However, if you are interested in learning more about the video pre-processing pipeline we used for the above demo, you can read about it in our [Notes](#video-preprocessing).

**If you'd like to adapt this code for other purposes, please adjust your data accordingly; for instance, to identify actions from pose, each subdirectory should contain clips of that action being performed.*

#### **2. Run pose estimation**

We provide a Terraform script to set up an arbitrary number of GCP VMs that come preconfigured with OpenPose. You can adjust this script to work with your preferred cloud provider (IBM, AWS, etc.).

(Link to OpenPose Terraform repo)

#### **3. ConvLSTM for player ID**



---

### Notes

#### Data Collection

Pose-based player identification works best when footage is consistently filmed across multiple competitions from the same stationary camera. You may still  have good results with a collection of clips from a variety of events and camera angles, but you will need a significantly larger dataset.

The training clips should be representative of the footage that will be used in the final application.

#### Video Preprocessing

Perhaps the largest obstacle to large-scale player identification is not actually identifying the players, but rather collecting a


#### Pose Estimation

We trialed various pose estimation libraries, including [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) and [PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet), and did not find that any one library had a significant impact (either positive or negative) on overall identification accuracy. However, we primarily worked with [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) due to its relatively straightforward setup and multiple OS/system support, options for multi-person identification, 2D and 3D detection, and other features that were relevant to our use cases.
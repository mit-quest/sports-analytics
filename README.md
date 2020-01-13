# Sports Analytics
## Pose-based player identification from  video

TODO: image

The way that professional athletes play their sport is sufficiently unique that just a few moves on the field or court can be enough for a computer vision model to distinguish them from their teammates and competitors.

Using pose estimation models, such as [CMU’s OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), we extract key points representing athletes’ skeletal positions from video recordings of their competitions. These skeletal key points are then used to train a neural network to predict a particular athlete’s identity from unseen footage. To accomplish this, there are five workflows that this repository supports:

* [data ingestion](data_ingestion): copying prepared video data into the cloud for storage and usage
* [pose extraction](pose_extraction): extracting skeletal keypoints from videos with OpenPose
* [dataset preparation](dataset_preparation): preparing a dataset for training and testing of a player identification model
* [training](train): training a player identification model on a prepared dataset
* [testing](test): testing a pretrained player identification model on a prepared dataset

---
### Demo

We've provided a [Colab notebook]() that will automatically download a prepared dataset and run a pretrained player identification model.

The demo dataset was curated from videos of two matches at Wimbledon 2018 provided by the [Wimbledon YouTube Channel](https://www.youtube.com/wimbledon). The model was trained on clips from [Novak Djokovic vs Rafael Nadal](https://www.youtube.com/watch?v=V96sSCV03ng) and is tested on unseen clips from that match (88.6% accuracy: Nadal 83.5%, Del Potro 95.5%), as well as clips from [Juan Martin del Potro vs Rafael Nadal](https://www.youtube.com/watch?v=S5LVbZUgM48) (76.5% accuracy: Nadal 86.5%, ”not Nadal” 65.2%).

TODO: image

---
### Prerequisites for all workflows
**Note**: Each of the following steps, from video pre-processing to running pose estimation and training player ID models, can be computationally expensive. We therefore strongly recommend proceeding with a GPU-provisioned system, and provide instructions for running pose extraction and model training on a VM.

#### Clone this repository
If you have not done so already, in a terminal window, enter `git clone git@github.com:mit-quest/sports-analytics.git`

Change into the main directory: `cd sports-analytics`

If you do not have `git` installed, see [here]() for installation instructions. TODO: add link/link content

#### Terraform

To programmatically set up and destroy cloud resources (virtual machines, buckets, etc.), we will use a tool called Terraform. For instructions on how to install Terraform, see [here](). TODO: add link/link content

#### GCP

All of the workflows use Google Cloud Platform (GCP) for storage (buckets) and compute (virtual machines). To allow the code to programmatically interact with GCP, we will set up a Software Development Kit (SDK) on your local machine. To install the GCP SDK follow the instructions [here](). TODO: add link/link content

To set up and destroy virtual machines, Terraform requires access to GCP. For instructions on how to download GCP credentials for Terraform, see [here](). TODO: add link/link content

#### Pipenv

For locally run python code we will use a tool called `pipenv` to set up and manage python virtual environments and packages. See the instructions [here]() for on how to install `pipenv`. TODO: add link/link content

Run the command `pipenv install` to set up the virtual environment and download the required python packages for the workflows.

### Workflows
#### **0. Prepare video data**

For player identification, your data should consist of a single directory containing *n* subdirectories with mp4 clips for each of *n* players.* 

```
.
+-- player1
|   +-- clip1.mp4
|   +-- ...
|   +-- clipj.mp4
+-- player2
|   +-- clip1.mp4
|   +-- ...
|   +-- clipk.mp4
+-- ...
+-- playern
```

Each clip in a directory should ideally display only the individual named by the directory, but multi-person clips where the individual is the primary focus in the foreground will work as well if you are using our provided configuration of OpenPose to extract skeletal key points.

Given the specificity of each use case, we leave it up to you to prepare your video data appropriately. However, if you are interested in learning more about the video pre-processing pipeline we used for the above demo, you can read about it in our [Notes](#video-preprocessing).

**If you'd like to adapt this code for other purposes, please adjust your data accordingly; for instance, to identify actions from pose, each subdirectory should contain clips of that action being performed.*

#### **1. Copy prepared video data into the cloud for storage and usage**

Prerequisite artifacts:
* A directory of prepared video clips (see [Workflow 0: Prepare video data](#0-prepare-video-data))

Infrastructure that will be used:
* A GCP bucket where the videos will be stored
* Your local machine to upload the videos to the GCP bucket

#### Workflow

1. In a terminal window, enter:

`gsutil mb gs://[BUCKET_NAME]/`

where [BUCKET_NAME]  is the name you'd like for your GCP storage bucket.

1. After your bucket has been created, copy all of the data in your local directory into the bucket:

`gsutil -m cp -r [PATH_TO_LOCAL_DIRECTORY] gs://[BUCKET_NAME]/`

1. When this completes, you should see all of your video data at `gs://[BUCKET_NAME]/`.


#### **2. Extract skeletal keypoints from videos with OpenPose**

Prerequisite artifacts:
* Prepared mp4 clips (in a GCP bucket) from which we will extract skeletal keypoints

Infrastructure that will be used:
* A GCP bucket where the videos will be accessed from
* A GCP bucket where the extracted keypoints will be stored
* A GCP virtual machine to run OpenPose on

#### Workflow

1. If the clips are not in a GCP bucket, see the previous workflow [Copy prepared video data into the cloud for storage and usage]().
 
1. In a terminal window, enter: 

#### **3. Prepare a dataset for training and testing of a player identification model**

#### **4. Train a player identification model**

#### **5. Test a pretrained player identification model**



---

### Notes

#### Data Collection

Pose-based player identification works best when footage is consistently filmed across multiple competitions from the same stationary camera. You may still  have good results with a collection of clips from a variety of events and camera angles, but you will need a significantly larger dataset.

The training clips should be representative of the footage that will be used in the final application.

#### Video Preprocessing

Perhaps the largest obstacle to large-scale player identification is not actually identifying the players, but rather collecting a sufficient amount of appropriate footage for each player.


#### Pose Estimation

We trialed various pose estimation libraries, including [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) and [PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet), and did not find that any one library had a significant impact (either positive or negative) on overall identification accuracy. However, we primarily worked with [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) due to its relatively straightforward setup and multiple OS/system support, options for multi-person identification, 2D and 3D detection, and other features that were relevant to our use cases.
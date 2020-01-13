### Prepare a dataset for training and testing a player identification model

Prerequisite artifacts:
* Skeletal keypoints (in a GCP bucket) we will use to create train and test sets

Infrastructure that will be used
* A GCP bucket where the extracted keypoints will be accessed from
* A GCP virtual machine to run OpenPose on

### Workflow

1. If the clips are not in a GCP bucket, see the previous workflow [Copy prepared video data into the cloud for storage and usage]().
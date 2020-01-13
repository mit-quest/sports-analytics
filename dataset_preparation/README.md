### Prepare a dataset for training and testing a player identification model

Prerequisite artifacts:
* Skeletal keypoints (in a GCP bucket) we will use to create dataset CSVs

Infrastructure that will be used:
* A GCP bucket where the extracted keypoints will be accessed from & prepared datasets are written to
* A GCP virtual machine to prepare the datasets on

### Workflow

1. If the skeletal keypoints are not in a GCP bucket, see the previous workflow [Extract skeletal keypoints from videos with OpenPose](../pose_extraction/README.md).

1. At this point, after completing the previous workflow, you should be `ssh`ed into a GCP VM on which two buckets are mounted: the bucket with the original mp4 clips, and the bucket with the extracted keypoints.

1. In the `ssh` session, enter `python dataset_preparation/prepare_keypoints.py`. This will create two CSVs: one with the raw data from OpenPose (Player:Keypoints for each clip), and a version that is formatted for purpose. 

1. You can confirm that the two CSVs have been created by checking the keypoints bucket for `<dataset_ID>_keypoints.csv` and `<dataset_ID>_formatted.csv`
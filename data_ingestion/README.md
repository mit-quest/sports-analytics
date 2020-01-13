## Copy prepared video data into the cloud for storage and usage

Prerequisite artifacts:
* A directory of prepared video clips (see [Workflow 0: Prepare video data](docs/prepare_videos.md))

Infrastructure that will be used:
* A GCP bucket where the videos will be stored
* Your local machine to upload the videos to the GCP bucket

#### Workflow

1. In a terminal window, enter
`gsutil mb gs://[BUCKET_NAME]/`
where [BUCKET_NAME]  is the name you'd like for your GCP storage bucket.

1. After your bucket has been created, copy all of the data in your local directory into the bucket:
`gsutil -m cp -r [PATH_TO_LOCAL_DIRECTORY] gs://[BUCKET_NAME]/`

1. When this completes, you should see all of your video data at `gs://[BUCKET_NAME]/`
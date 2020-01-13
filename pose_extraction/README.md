## Extract skeletal keypoints from videos with OpenPose

Prerequisite artifacts:
* Prepared mp4 clips (in a GCP bucket) from which we will extract skeletal keypoints

Infrastructure that will be used:
* A GCP bucket where the videos will be accessed from
* A GCP bucket where the extracted keypoints will be stored
* A GCP virtual machine to run OpenPose on

### Workflow

1. If the clips are not in a GCP bucket, see the previous workflow [Copy prepared video data into the cloud for storage and usage]().

1. If you have not already, follow the [local setup instructions](docs/local_setup.md) to install the GCP SDK and Terraform.

1. Edit the `configs/openpose.yaml` file as follows:
    1. `clips_path`: the URL of the top-level directory containing the mp4 clips on which pose extraction will be run (ie `"gs://bucketname/directory"`)
    1. `dataset_ID`: the ID of the dataset to be created
    1. `keypoints_bucket`: the name of the destination bucket for CSVs containing the extracted skeletal keypoints.

#### Connect Terraform to GCP
1. Create and download the GCP service key that Terraform will need:
    1. Make a `keys` folder: `mkdir keys`
    1. Create a service account for terraform: 
        1. `https://console.cloud.google.com/apis/credentials/serviceaccountkey`
        1. Select `Compute Engine default service account` and leave JSON selected
        1. Create the key and move it into the `/keys` folder
        
1. Edit the terraform variables file [`terraform.tfvars`](../terraform.tfvars) to include your information.

#### Use Terraform to create GCP VM(s)

1. Initialize terraform: `terraform init`

1. Use `terraform apply` to start the appropriate GCP virtual machine. This will copy the current code base from your local machine to the GCP machine so make sure any changes to the configuration file are saved before this step is run.

1. Once Terraform finishes, you can check the GCP virtual machine console to ensure a virtual machine has been created named `<project_name>-<user_name>` where `<project_name>` is the name of your GCP project and `<user_name>` is your GCP user name.
 
#### Use OpenPose to extract skeletal keypoints

1. After the VMs have been created, you can `ssh` into the VM `<project_name>-<user_name>`, either using the one-click SSH that GCP provides through their [console](console.cloud.google.com), the GCP SDK, or simply via `ssh username@externalIPaddress`

1. In the `ssh` window, enter: `python extract_keypoints.py`

1. Once skeletal extraction has finished, you should see the folder `<gcp_bucket>/datasets/<dataset_ID>` has been created and populated, where `<dataset_ID>` was defined in `configs/openpose.yaml`.

1. Continue to [dataset preparation](../dataset_preparation/README.md)
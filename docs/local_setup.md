### Prerequisites for all workflows
**Note**: Each of the following steps, from video pre-processing to running pose estimation and training player ID models, can be computationally expensive. We therefore strongly recommend proceeding with a GPU-provisioned system, and provide instructions for running pose extraction and model training on a VM.

#### Clone this repository
If you have not done so already, in a terminal window, enter `git clone git@github.com:mit-quest/sports-analytics.git`

All commands will assume to be run from the main sports-analytics directory, which you can cd into using: `cd sports-analytics`

If you do not have `git` installed, see [here]() for installation instructions. TODO: add link/link content

#### GCP

All of the workflows use Google Cloud Platform (GCP) for storage (buckets) and compute (virtual machines). To allow the code to programmatically interact with GCP, we will set up a Software Development Kit (SDK) on your local machine. To install the GCP SDK follow the instructions [here](https://cloud.google.com/sdk/install).

#### Terraform

To programmatically set up and destroy cloud resources (virtual machines, buckets, etc.), we will use a tool called Terraform. For instructions on how to install Terraform, see [here](https://learn.hashicorp.com/terraform/getting-started/install.html).

To set up and destroy virtual machines, Terraform requires access to GCP. For instructions on how to download GCP credentials for Terraform, see [here](../pose_extraction/README.md).
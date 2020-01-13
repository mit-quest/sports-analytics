# openpose-sandbox

## Overview

This repo walks through:
1. Building and destroying an arbitrary number of GCP machines with openpose installed
1. Connecting PyCharm to the GCP machine for remote code execution

## Setup

1. Install the GCP SDK: `https://cloud.google.com/sdk/install`
1. Install terraform: `https://learn.hashicorp.com/terraform/getting-started/install.html`
1. Create and download the GCP service key terraform will need:
    1. In this directory, make a `keys` folder
    1. Create a service account for terraform: 
        1. `https://console.cloud.google.com/apis/credentials/serviceaccountkey`
        1. Select `Compute Engine default service account` and leave JSON selected
        1. Create the key and move it into the `/keys` folder
1. Create a ssh public and private key pair (or use a pre-existing pair) to be used to connect pycharm to the remote GCP VM (instructions are [here](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)).
1. Edit to the terraform variables file (`terraform.tfvars`) to include your information
1. Initialize terraform: `terraform init`

### Usage

Building the machines:
1. `terraform apply`
1. Review the changes and enter `yes` if correct
1. It will take ~30 minutes to install all of the necessary packages and build openpose

Connecting PyCharm:
1. File > Settings > Project > Project Interpreter > Click the settings sprocket to the right and select "Add"
1. Select SSH interpreter
1. Enter the IP address of the machine (most easily found from the GCP VM instances console under `Exeternal IP`) as `host` and your GCP username as `username` and click next
1. In the next window change the interpreter to `/usr/bin/python3`, in Sync folders click on the folder icon and change the remote path to `/home/<username>/openpose-sandbox` and click finish
1. Give PyCharm a few minutes to do its thing and get everything sync'd
1. Test it's working by running `test_openpose.py` in PyCharm
1. You can view the video by either `scp`ing it, copying it to a bucket and viewing it there, or in one of the browser SSH console windows select "Download file"

Destroying the machines:
1. `terraform destroy`
1. Review the changes and enter `yes` if correct

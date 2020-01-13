from multiprocessing import pool
import os
from pathlib import Path
import subprocess
import yaml


def run_openpose(clip_path):

    subprocess.call(['./run_openpose.sh', clip_path, player, str(int(start_time)), dir])


def get_clip_paths(clips_mount):

    directory = os.fsencode(clips_mount)

    clip_paths = []

    for subdir in os.listdir(directory):
        for file in os.listdir(subdir):

            filename = os.fsdecode(file)
            clip_path = subdir + '/' + filename
            clip_paths.append(clip_path)

    return clip_paths


def mount_buckets(clips_bucket, keypoints_bucket):

    os.environ["clips_bucket"] = clips_bucket
    os.environ["clips_mount"] = clips_mount
    os.environ["keypoints_bucket"] = keypoints_bucket
    os.environ["keypoints_mount"] = keypoints_mount

    subprocess.call(['mkdir $clips_mount'])
    subprocess.call(['mkdir $keypoints_mount'])

    subprocess.call(['./gcsfuse_setup.sh'])
    subprocess.call(['gcsfuse $clips_bucket $clips_mount'])
    subprocess.call(['gcsfuse $keypoints_bucket $keypoints_mount'])


if __name__ == '__main__':

    with Path('../configs/openpose_config.yaml').open('r') as f:
        openpose_config = yaml.safe_load(f)['openpose_config']

    clips_bucket = openpose_config["clips_bucket"]
    clips_mount = '/mnt/clips_mount'
    keypoints_bucket = openpose_config["keypoints_bucket"]
    keypoints_mount = '/mnt/keypoints_mount'

    subprocess.call(['./install_openpose.sh'])

    mount_buckets(clips_bucket, clips_mount, keypoints_bucket, keypoints_mount)

    clip_paths = get_clip_paths(clips_mount)

    pool = Pool()  # Create a multiprocessing Pool
    pool.map(run_openpose, clip_paths)
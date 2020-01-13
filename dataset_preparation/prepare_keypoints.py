import pandas as pd
import json
import os

from format_keypoints import create_formatted_csv


# create CSV from keypoints
def create_csv_from_keypoints(keypoints_path, output_csv_path):

    df = pd.DataFrame(columns=['Player', 'Keypoints'])
    df = df.astype('object')

    directory = os.fsencode(keypoints_path)

    for subdir in os.listdir(directory):

        player = os.fsdecode(subdir)

        for file in os.listdir(subdir):

            filename = os.fsdecode(file)
            if filename.endswith(".json"):

                filepath = keypoints_path + '/' + filename

                with open(filepath) as json_file:
                    data = json.load(json_file)

                    if len(data['people']) > 0:
                        print(filename)
                        frame_kps = data['people'][0]['pose_keypoints_2d']

                        df = df.append({"Player": player, "Keypoints": frame_kps}, ignore_index = True)

    df.to_csv(output_csv_path, index=False)


if __name__ == '__main__':

    with Path('../configs/openpose_config.yaml').open('r') as f:
        openpose_config = yaml.safe_load(f)['openpose_config']

    keypoints_bucket = openpose_config["keypoints_bucket"]
    keypoints_mount = '/mnt/keypoints_mount'
    keypoints_path = keypoints_mount + '/' + openpose_config["dataset_id"]
    output_csv_path = openpose_config["dataset_id"] + "_keypoints.csv"
    formatted_csv_path = openpose_config["dataset_id"] + "_formatted.csv"

    create_csv_from_keypoints(keypoints_path, output_csv_path)
    create_formatted_csv(output_csv_path, formatted_csv_path)
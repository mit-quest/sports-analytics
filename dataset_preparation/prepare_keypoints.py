import pandas as pd
import json
import os


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
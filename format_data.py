import pandas as pd
import json
import os


# create CSV from keypoints
def create_csv_from_keypoints(KEYPOINTS_DIR, output_csv_path):

    df = pd.DataFrame(columns=['Player', 'Clip', 'Frame', 'Keypoints'])
    df = df.astype('object')

    for filename in os.listdir(KEYPOINTS_DIR):

        if filename.endswith(".json"):

            filepath = KEYPOINTS_DIR + '/' + filename

            kp_idx = filename.split('_')
            player = kp_idx[0][0]
            clip_num = kp_idx[0][1:]
            frame_num = kp_idx[1]

            with open(filepath) as json_file:
                data = json.load(json_file)

                if len(data['people']) > 0:
                    print(filename)
                    frame_kps = data['people'][0]['pose_keypoints_2d']

                    df = df.append({"Player": player, "Clip": clip_num, "Frame": frame_num, "Keypoints": frame_kps}, ignore_index = True)

    df.to_csv(output_csv_path, index=False)

# format dataframe
def format_csv()
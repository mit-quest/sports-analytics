import ast
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
import yaml

from prepare_keypoints import create_csv_from_keypoints
from format_keypoints import create_formatted_csv


def _create_player_dict(df):

    player_names = df.Player.unique()

    player_dict = dict()

    for i, name in enumerate(player_names):
        player_dict[name] = i

    return player_dict


def _create_clip_kps(df, clip):

    clip_kps = df[clip].dropna().tolist()

    float_kps = []

    for lst in clip_kps:

        lst = ast.literal_eval(lst)

        new_lst = []

        for i, s in enumerate(lst):
            s = float(s)
            new_lst.append(s)

        float_kps.append(new_lst)

    return float_kps


# create x, y for player identification
def _playerID_data(df):

    x = []
    y = []

    clips = list(df.columns.values.tolist())

    player_dict = _create_player_dict(df)

    for clip in clips:

        player = df['Player']

        onehot_player = player_dict[player]

        clip_kps = _create_clip_kps(df, clip)

        x.append(clip_kps)
        y.append(onehot_player)

    return x, y


def create_test_train(formatted_csv_path):

    df = pd.read_csv(formatted_csv_path)

    x, y = _playerID_data(df)


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

    create_test_train(formatted_csv_path)
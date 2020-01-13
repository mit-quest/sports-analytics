import ast
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


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

    x = np.array(x, dtype='float32')
    y = np.array(y, dtype='float32')

    x = np.expand_dims(x, axis=3)
    x = np.expand_dims(x, axis=4)

    y = np.expand_dims(y, axis=1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    return x_train, y_train, x_test, y_test
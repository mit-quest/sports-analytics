import pandas as pd


N_FRAMES = 80 # number of frames to cut clips into


# create dict of dicts to store num frames per clip per player:
# { player1: { clip1: [frames, splits], clip2: frames...}, ...}

def _get_frames_per_clip(kp_df, N_FRAMES):

    frames_for_all_players = {}

    players = kp_df['Player'].unique()

    for p in players:

        player_frames = {}

        player_col = kp_df.loc[kp_df['Player'] == p]
        clips = player_col['Clip'].unique()

        for c in clips:

            clip_col = player_col.loc[kp_df['Clip'] == c]
            num_frames = clip_col['Frame'].max()

            # calculate number of times to split each clip
            # a split value of 0 means the clip is kept intact up to N_FRAMES
            splits_per_clip = (num_frames/N_FRAMES)

            player_frames[c] = [num_frames, splits_per_clip]

        frames_for_all_players[p] = player_frames

    return frames_for_all_players


# split clip keypoints into clips of n frames each

def _split_clips(kp_df, frames_dict, N_FRAMES):

    clip_kps = {}

    for player, clip_dict in frames_dict.items():

        player_col = kp_df.loc[kp_df['Player'] == player]

        for clip, clip_info in clip_dict.items():

            num_splits = clip_info[1]

            clip_col = player_col.loc[kp_df['Clip'] == clip]

            # iterate over each frame in each clip (per player)
            k = 0
            while k < len(clip_col.index):

                row = clip_col.iloc[[k]]
                frame = int(row["Frame"].values[0])
                max_frames = N_FRAMES * (num_splits+ 1)

                if frame < max_frames:

                    frame_idx = frame / N_FRAMES

                    splitclip_name = player + str(clip) + '.' + str(frame_idx)
                    print(splitclip_name)
                    if splitclip_name not in clip_kps:
                        clip_kps.update({splitclip_name: []})

                    clip_kps[splitclip_name].insert(frame, row["Keypoints"].values[0])

                k += 1

    cleaned_clip_dict = {k: v for k, v in clip_kps.items() if len(v) == N_FRAMES}
    return pd.DataFrame(cleaned_clip_dict)


def create_formatted_csv(input_csv, output_csv):

    # load keypoints df
    kp_df = pd.read_csv(input_csv)

    frames_dict = _get_frames_per_clip(kp_df)

    df = _split_clips(kp_df, frames_dict)

    # save dataframe
    df.to_csv(output_csv, index=False)

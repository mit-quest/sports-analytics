import subprocess
import os


def extract_keypoints(CLIPS_DIR):

    directory = os.fsencode(CLIPS_DIR)

    # for each player
    for subdir in os.listdir(directory):

        # for each video clip
        for file in os.listdir(subdir):

            filename = os.fsdecode(file)
            start_time = float(filename[:-len('.mp4')])
            video_path = dir_path + '/' + filename

            subprocess.call(['./run_openpose.sh', video_path, player, str(int(start_time)), dir])
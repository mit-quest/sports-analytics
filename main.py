from pose_extraction import extract_keypoints
from dataset_preparation import format_data

CLIPS_DIR = '/path/to/clips/directory'
KEYPOINTS_DIR = '/path/to/save/keypoints'
DATA_DIR = 'path/to/save/CSVs'

# run pose detection on video clips
extract_keypoints(CLIPS_DIR, KEYPOINTS_DIR)

# create CSV from extracted keypoints
format_data.create_csv_from_keypoints(KEYPOINTS_DIR)

# create test/train sets from CSV
train, test = format_data.data_from_csv()

# train player ID model from CSV
convlstm.train(train)

# test trained model
test_results = convlstm.test(test)

# analyze output
print(test_results)

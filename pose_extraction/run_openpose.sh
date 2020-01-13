#!/usr/bin/env bash
VIDEO_PATH=$1

echo video: $VIDEO_PATH

#VIDEO_NAME="${VIDEO_PATH:0:4}"
#EXT="_OP.mp4"
#output_fp="$VIDEO_NAME$EXT"

rm -rf output.mp4
cd openpose
rm -rf openpose.avi

# cut the first n seconds
#ffmpeg -y -loglevel info -i $VIDEO_PATH -ss $CLIP_START -to $CLIP_END -async 1 -strict -2 video.mp4

# detect poses on the these n seconds
./build/examples/openpose/openpose.bin --net_resolution "1280x368" --scale_number 4 --scale_gap 0.25 --number_people_max 1 --video $VIDEO_PATH --write_json $keypoints_mount --display 0  --write_video openpose.avi

#3d
#./build/examples/openpose/openpose.bin --flir_camera --3d --number_people_max 1 --write_json ./output/ --write_video_3d ../video_3d.avi

# convert the result into MP4
#ffmpeg -y -loglevel info -i openpose.avi ./output_vids/$output_fp
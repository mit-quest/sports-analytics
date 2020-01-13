## Prepare video data

For player identification, your data should consist of a single directory containing *n* subdirectories with mp4 clips for each of *n* players: 

```
.
+-- player1
|   +-- clip1.mp4
|   +-- ...
|   +-- clipj.mp4
+-- player2
|   +-- clip1.mp4
|   +-- ...
|   +-- clipk.mp4
+-- ...
+-- playern
```

Each clip in a directory should ideally display only the individual named by the directory, but multi-person clips where the individual is the primary focus in the foreground will work as well if you are using our provided configuration of OpenPose to extract skeletal key points.

Given the specificity of each use case, we leave it up to you to prepare your video data appropriately. However, if you are interested in learning more about the video pre-processing pipeline we used for our [demo](), you can read the following [Notes](#notes) section.

---

### Notes

#### Data Collection

Pose-based player identification works best when footage is consistently filmed across multiple competitions from the same stationary camera. You may still  have good results with a collection of clips from a variety of events and camera angles, but you will need a significantly larger dataset.

The training clips should be representative of the footage that will be used in the final application.

#### Video Preprocessing

Perhaps the largest obstacle to large-scale player identification is not actually identifying the players, but rather collecting a sufficient amount of appropriate footage for each player.


#### Pose Estimation

We trialed various pose estimation libraries, including [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) and [PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet), and did not find that any one library had a significant impact (either positive or negative) on overall identification accuracy. However, we primarily worked with [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) due to its relatively straightforward setup and multiple OS/system support, options for multi-person identification, 2D and 3D detection, and other features that were relevant to our use cases.
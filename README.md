## Intro

The purpose of this little project is to add object tracking to yolov2 and achieve real-time multiple object tracking.
Currently support people tracking (as the provided weights for deep_sort were trained on people tracking)

## Dependencies

    python
    numpy
    opencv 3
    tensorflow 1.0
    Cython.
    sklean.

### Setup

1 - Clone this repository : `git clone https://github.com/bendidi/Tracking-with-darkflow.git`

2 - Initialize all submodules: `git submodule update --init --recursive`

## Getting started

Download the weights :

Read more about YOLO (in darknet) and download weight files [here](http://pjreddie.com/darknet/yolo/),In case the weight file cannot be found, [thtrieu](https://github.com/thtrieu) has uploaded some of his [here](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU), which include `yolo-full` and `yolo-tiny` of v1.0, `tiny-yolo-v1.1` of v1.1 and `yolo`, `tiny-yolo-voc` of v2.

The artchitecture I used/tested in this project is `cfg/yolo.cfg` with the weights `bin/yolo.weights`.

Next you need to download the deep_sort weights [here](https://owncloud.uni-koblenz.de/owncloud/s/f9JB0Jr7f3zzqs8?path=%2Fresources) (networks folder), provided by [nwojke](https://github.com/nwojke)

extract the folder and copy it to `deep_sort/resources`

Edit `run.py` following your desired configuration, and run it : `python run.py`

## Disclamer :

this project is using code forked from:

[thtrieu/darkflow](https://github.com/thtrieu/darkflow): for the real-time object detections and classifications.

[nwojke/deep_sort](https://github.com/nwojke/deep_sort): for Simple Online Realtime Tracking with a Deep Association Metric.

Please follow the links to get an understanding of all the features of each project.

## Citation

### Yolov2 :

    @article{redmon2016yolo9000,
      title={YOLO9000: Better, Faster, Stronger},
      author={Redmon, Joseph and Farhadi, Ali},
      journal={arXiv preprint arXiv:1612.08242},
      year={2016}
    }

### deep_sort :

    @article{Wojke2017simple,
      title={Simple Online and Realtime Tracking with a Deep Association Metric},
      author={Wojke, Nicolai and Bewley, Alex and Paulus, Dietrich},
      journal={arXiv preprint arXiv:1703.07402},
      year={2017}
    }

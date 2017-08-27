# Cell Segmentation

## Introduction

This project aims at performing automated identification of cell boundaries from the pathological video data.
We are given the video file `cells.avi` as input. The problem statement can be found [here.](https://innovate.mygov.in/challenges/identifying-cell-boundaries-from-video-data/)

## Compatibility

* This code has been tested on Ubuntu 16.04 LTS and Windows 10
* **Dependencies** - Python 2.7 & 3.5, OpenCV 3.0+

## Methods Used

* Image Processing followed by Contours
* Adaptive Thresholding
* Watershed Algorithm
* Structured Forest Algorithm

## Results

The video `edge.avi` is the result after applying Structured Forest algorithm. Other outputs can be found in the `Outputs` folder.

## References

Our *Structured Forest* is an implementation of [Artanis CV python structured forest](https://github.com/ArtanisCV/StructuredForests).

## Future work

* U-net convolutional neural network can be used.

* Implementing the algorithm given in this [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5096676/).

## Disclaimer

This software is published for academic and non-commerical use only.

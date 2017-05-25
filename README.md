Cell Segmentation
==================


## Introduction

This project aims at performing automated identification of cell boundaries from the pathological video data.

We are given the video file `cells.avi` as input. 


## Compatibility

* This code has been tested on Ubuntu 16.04 LTS and Windows 10
* **Dependencies** - Python,OpenCV


## Methods Used

1. Image Processing followed by Contours
2. Adaptive Thresholding
3. Watershed Algorithm
4. Structured Forest Algorithm


## Results

The video `edge.avi` is the result after applying Structured Forest algorithm.


## References

Our *Structured Forest* is an implementation of [Artanis CV python implementation](https://github.com/ArtanisCV/StructuredForests).


## Disclaimer

This software is published for academic and non-commerical use only.

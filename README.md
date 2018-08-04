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
* [Structured Forests for Fast Edge Detection](https://pdollar.github.io/files/papers/DollarPAMI15edges.pdf)

## Usage

First clone the repository by typing: `git clone https://github.com/iitmcvg/Cell-Segmentation.git`.

### Structured Forest

* First execute `python framesaver.py` to save the frames for structured forest.
* Next execute `python StructuredForests.py` to apply the edge detection.
* Finally, execute `python videowriter.py` to write the outputs to a video file.

## Results

* The video `edge.avi` is the result after applying Structured Forest algorithm. Other outputs can be found in the `Outputs` folder.
* Outputs of all methods can be seen at once in [this](https://drive.google.com/file/d/1mmDtpkT1wQzZ-aafKzgkFz4BpQd9eV88/view?usp=sharing) video.

## References

Our *Structured Forest* is an implementation of [Artanis CV Structured Forest](https://github.com/ArtanisCV/StructuredForests).

## Future work

* U-net convolutional neural network can be used.

* Implementing the algorithm given in this [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5096676/).

## Disclaimer

This software is published for academic and non-commerical use only.

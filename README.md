# Real-Time Color Detection with OpenCV

This project is a simple real-time color detection tool that tracks green objects in a webcam feed using OpenCV and HSV thresholding. Feel free to adjust to any color you want.

## Overview

- Uses OpenCV to capture video from a camera and detect a specific color (default: green) in real time.
- Converts frames from BGR to HSV and thresholds them to build a mask for the target color range.
- Draws a bounding box around the largest detected region and displays the live result in a window. 

## Features

- Real-time video capture from a webcam using `cv2.VideoCapture`.
- Automatic HSV range calculation from a given BGR color using a utility function.
- Noise reduction with erosion and dilation before contour detection for more stable bounding boxes. 

## Requirements

- **Python** 
- **OpenCV**
- **NumPy**
- **Pillow**

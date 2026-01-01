# Image to Vector Converter

This project converts raster images (JPG, PNG, etc.) into vector formats (SVG and DXF) using computer vision techniques (OpenCV).

## How It Works

1. The input image is first converted to grayscale i.e black and white because most OpenCV algorithms operate on change in intensity of pixels rather than color information.

2. Noise is then reduced using Gaussian blurring, which smooths the image by averaging neighboring pixels. This helps suppress texture and small unwanted details that are not needed.

3. After preprocessing the algorithm detects sudden changes in brightness, which usually correspond to object boundaries and important shape outlines.

4. Contour extraction is then performed using OpenCV. A contour is a curve that joins continuous points along a boundary with the same intensity, and these contours represent the outlines of shapes present in the image.

5. The extracted contour points are converted into vector polylines and exported as SVG for scalable visualization and as DXF for CAD, AutoCAD, and manufacturing applications.

## Features of the project
- Raster to vector conversion (JPG/PNG → SVG, DXF)
- Noise reduction and edge detection
- Inner and outer contour extraction
- CAD compatible DXF export

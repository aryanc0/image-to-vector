# Image to Vector Converter

This project converts raster images (JPG, PNG, etc.) into vector formats (SVG and DXF) using computer vision techniques (OpenCV).

## How It Works

1. The input image is first converted to grayscale i.e black and white because most OpenCV algorithms operate on change in intensity of pixels rather than color information.

2. Noise is then reduced using Gaussian blurring, which smooths the image by averaging neighboring pixels. This helps suppress texture and small unwanted details that are not needed.

3. After preprocessing the algorithm detects sudden changes in brightness, which usually correspond to object boundaries and important shape outlines.

4. Contour extraction is then performed using OpenCV. A contour is a curve that joins continuous points along a boundary with the same intensity, and these contours represent the outlines of shapes present in the image.

5. The extracted contour points are converted into vector polylines and exported as SVG for scalable visualization and as DXF for CAD, AutoCAD, and manufacturing applications.

## Modular Architecture

- **preprocessing (cv2)**  
  Grayscale conversion and noise reduction using Gaussian blur.

- **edge_detection (cv2)**  
  Detection of object boundaries using Canny edge detection.

- **contour_extraction (cv2)**  
  Extraction of inner and outer contours representing shape geometry.

- **vector_export_svg (svgwrite)**  
  Conversion of contour points into SVG polylines for scalable visualization.

- **vector_export_dxf (ezdxf)**  
  Conversion of contour points into DXF polylines for CAD and manufacturing use.

- **main.py**  
  Orchestrates the complete image-to-vector pipeline.

## Libraries and Tools Used

- **OpenCV (cv2)**  
  Used for computer vision operations such as grayscale conversion, noise reduction, edge detection, and contour extraction.

- **ezdxf**  
  Used to generate DXF files by converting extracted contour points into CAD-compatible polylines.

- **svgwrite**  
  Used to export contour geometry as SVG vector graphics for scalable visualization.

- **NumPy**  
  Used internally by OpenCV for efficient numerical and image array operations.


## Features of the project
- Raster to vector conversion JPG/PNG to SVG, DXF files
- Noise reduction and edge detection
- Inner and outer contour extraction
- CAD compatible DXF export 
- SVG export for visual represntation

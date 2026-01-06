# 🆔 Card Detection & Face Extraction

This project is a Python script designed to detect a card from an input image using Computer Vision techniques. It performs a **Perspective Transform** to obtain a top-down (bird's-eye) view of the card and subsequently extracts the face region using a specific mask.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

## 📋 Key Features

* **Edge Detection:** Utilizes Canny Edge Detection combined with Gaussian Blur and Morphological Operations to accurately identify card boundaries.
* **Contour Processing:** Implements Convex Hull and `approxPolyDP` to locate the four corner points of the card.
* **Perspective Transform:** Warps the detected card area into a flat, rectangular view based on standard card aspect ratios.
* **Face Extraction:** apply a bitwise operation with a pre-defined mask to isolate and crop the face from the card.

## 🛠️ Installation

This project requires Python and standard data science/vision libraries. Install the dependencies using pip:

```bash
pip install opencv-python numpy matplotlib
```

## 📂 File Structure

Ensure your directory is organized as follows for the script to run correctly:

```
.
├── {ImagePath}.jpg           # Input image containing the card (update path in code)
├── {cardPath}.bmp            # Mask image for face location (update path in code)
├── CardDetector.py           # Main Python script
└── README.md
```

**Note:** Before running the script, update the file paths in `CardDetector.py`:
```python
inputImage = cv2.imread('{ImagePath}.jpg')  # Replace with your image path
Mask = cv2.imread('{cardPath}.bmp')         # Replace with your mask path
```

## 🚀 Pipeline Explanation

The processing pipeline consists of four main steps:

**Preprocessing:**

* Convert the image to Grayscale.
* Reduce noise using GaussianBlur.
* Detect edges using Canny and connect broken ridges using Morphological Closing.

**Card Detection:**

* Identify the largest contour in the image.
* Compute the Convex Hull and approximate the polygon to find the 4 corner points using approxPolyDP.

**Perspective Transform (Warping):**

* Order the 4 corner points (Top-Left, Top-Right, Bottom-Right, Bottom-Left).
* Calculate the Homography Matrix via getPerspectiveTransform.
* Warp the image to a top-down view using warpPerspective.

**Face Extraction:**

* Resize the mask to match the warped card dimensions.
* Apply bitwise_and to isolate the face region.
* Calculate the bounding box of the face and crop the final image (face.jpg).

## 💻 Usage

Run the Python script:

```bash
python main.py
```

The script will display the result using Matplotlib and save the cropped face image as `face.jpg` in the current directory.
# 🆔 Card Detection & Face Extraction

This project is a Python script that detects a card from an input image using **Computer Vision** techniques.  
It performs a **Perspective Transform** to obtain a top-down (bird’s-eye) view of the card and then **extracts the face region** using a predefined mask.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

## 🖼️ Example Input & Output

### 🔹 Input Image (Original Card)
This is the original image provided to the pipeline.  
The algorithm detects card edges, contours, and corner points from this image.

![Original Card Image](https://drive.google.com/uc?export=view&id=1WQAvaQh80WI5o2YsaL5mfwFlJCPLX8LM)

---

### 🔹 Output Image (Extracted Face)
After perspective warping and mask-based extraction, the face region is isolated and cropped.

![Extracted Face Image](https://drive.google.com/uc?export=view&id=11a_UMvLHt7GTkY9sa2o_JFNWU9cUYe8M)

---

## 📋 Key Features

- **Edge Detection**  
  Uses *Gaussian Blur* + *Canny Edge Detection* with *Morphological Closing* to clearly highlight card boundaries.

- **Contour Processing**  
  Identifies the largest contour, computes its **Convex Hull**, and applies `approxPolyDP` to estimate the four card corners.

- **Perspective Transform**  
  Warps the detected card into a flat, rectangular, top-down view using homography.

- **Face Extraction**  
  Applies a predefined mask with `bitwise_and` to isolate and crop the face region.

---

## 🛠️ Installation

Install the required dependencies:

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

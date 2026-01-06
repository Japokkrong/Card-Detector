import cv2 
from matplotlib import pyplot as plt
import numpy as np
## Change inputImage and Mask to your image path and mask path
inputImage = cv2.imread('{ImagePath}.jpg')
Mask = cv2.imread('{cardPath}.bmp')
GrayinputImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
blurred =cv2.GaussianBlur(GrayinputImage, (5,5), 0)
Edge_image = cv2.Canny(blurred, 80, 150)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
Edge_image = cv2.morphologyEx(Edge_image, cv2.MORPH_CLOSE, kernel)
#--- Find contour ---
contours, _ = cv2.findContours(Edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#---- Apply Convexhull on max contour----
largest_contour = max(contours, key= cv2.contourArea)
hull = cv2.convexHull(largest_contour)
#---- Approx polyDP ----
epsilon = 0.02* cv2.arcLength(hull, True)
approx = cv2.approxPolyDP(hull, epsilon, True)
# --- reshape ---
pts = approx.reshape(4,2).astype(np.float32)
#---- ordered point ----
def ordered_points(pts):
    rect = np.zeros((4,2), dtype=np.float32)
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)] #top left
    rect[2] = pts[np.argmax(s)] # top right 
    
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)] # bottom right
    rect[3] = pts[np.argmax(diff)] #bottom left
    return rect
src_pts = ordered_points(pts)
print(src_pts)
card_width = 600
card_height = int(card_width / 1.586)

dst_pts = np.array([
    [0, 0],
    [card_width-1, 0],
    [card_width-1, card_height-1],
    [0, card_height-1]
], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_pts, dst_pts)
warped_card = cv2.warpPerspective(inputImage, M, (card_width, card_height))

masked_resized = cv2.resize(Mask, (card_width, card_height))
mask_gray = cv2.cvtColor(masked_resized,cv2.COLOR_BGR2GRAY)

face = cv2.bitwise_and(warped_card, warped_card,mask=mask_gray)
face_contours, _  = cv2.findContours(mask_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(face_contours[0])
face_cropped = warped_card[y:y+h, x:x+w]
face_cropped_RGB = cv2.cvtColor(face_cropped, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(face_cropped_RGB)
plt.show()
cv2.imwrite('face.jpg', face_cropped)
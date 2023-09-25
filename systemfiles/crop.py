import cv2
im = cv2.imread("export.png")
crop = im[580:580+33, 980:980+763]
cv2.imwrite("footer.png", crop)
import cv2

# Function to handle mouse events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pixel coordinates: ({x}, {y})")

# Read the image
image_path = '1st_page.png'  # Replace with the path to your image
image = cv2.imread(image_path)

# Display the image
cv2.imshow('Image', image)

# Set the mouse callback function
cv2.setMouseCallback('Image', click_event)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
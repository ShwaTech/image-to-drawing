import numpy as np
import cv2

# Load the image
portrait_path = '/mnt/data/tyishimepass.jpeg'
portrait = Image.open(portrait_path)

# Convert image to grayscale
gray_portrait = cv2.cvtColor(np.array(portrait), cv2.COLOR_RGB2GRAY)

# Use edge detection to create a sketch effect
edges = cv2.Canny(gray_portrait, threshold1=50, threshold2=150)

# Invert the edges to get a sketch effect
inverted_edges = cv2.bitwise_not(edges)

# Convert back to PIL Image
sketch_portrait = Image.fromarray(inverted_edges)

# Save and display the sketch image
sketch_portrait_path = '/mnt/data/sketch_portrait.png'
sketch_portrait.save(sketch_portrait_path)
sketch_portrait.show()

sketch_portrait_path


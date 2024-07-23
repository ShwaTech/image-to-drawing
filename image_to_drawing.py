from PIL import Image, ImageDraw, ImageFilter

# Load the image
image_path = '/mnt/data/WhatsApp Image 2024-07-23 at 15.10.29.jpeg'
image = Image.open(image_path)

# Display the image to understand its structure and contents
image.show()
# Create a simplified drawing based on the original image
image = Image.open(image_path)
drawn_image = Image.new('RGB', image.size, (255, 255, 255))
draw = ImageDraw.Draw(drawn_image)

# Define the coordinates for the circles and lines based on the provided image
# Note: The coordinates are approximations for the simplicity of the demonstration
circle_radius = 50
circle_positions = [
    (150, 150),
    (150, 300),
    (150, 450),
    (450, 300)
]

line_positions = [
    (150 + circle_radius, 150, 450 - circle_radius, 300),
    (150 + circle_radius, 300, 450 - circle_radius, 300),
    (150 + circle_radius, 450, 450 - circle_radius, 300)
]

# Draw circles
for pos in circle_positions:
    x, y = pos
    draw.ellipse((x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius), outline='blue', width=5, fill='white')

# Draw lines
for line in line_positions:
    draw.line(line, fill='blue', width=5)

# Display the drawn image
drawn_image.show()

# Save the drawn image
drawn_image_path = '/mnt/data/drawn_logo.png'
drawn_image.save(drawn_image_path)
drawn_image_path


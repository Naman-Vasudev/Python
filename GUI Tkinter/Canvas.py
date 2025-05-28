# Complete Tkinter Canvas Tutorial with All Examples and Explanations
from tkinter import *

# Function to draw a perfect circle given center coordinates and radius
def draw_circle(canvas, center_x, center_y, radius, color='blue'):
    """
    To draw a circle, we need to calculate the bounding box coordinates
    Canvas uses create_oval(x1, y1, x2, y2) where:
    - (x1, y1) = top-left corner of bounding rectangle
    - (x2, y2) = bottom-right corner of bounding rectangle
    """
    x1 = center_x - radius  # Left edge of bounding box
    y1 = center_y - radius  # Top edge of bounding box
    x2 = center_x + radius  # Right edge of bounding box
    y2 = center_y + radius  # Bottom edge of bounding box
    return canvas.create_oval(x1, y1, x2, y2, fill=color, outline='black', width=2)

# Create the main window
window = Tk()  # Tk() is the main window class, instantiate creates a window object
window.title("Complete Canvas Tutorial")  # Set window title
window.geometry("600x600")  # Set window size (width x height)

# Create Canvas widget - this is our drawing area
canvas = Canvas(
    window,     # Parent widget (the window)
    height=500, # Canvas height in pixels
    width=500,  # Canvas width in pixels
    bd=5,       # Border width around canvas
    bg='lightgray',  # Background color of canvas
    relief='sunken'  # Border style (sunken, raised, flat, etc.)
)

# COORDINATE SYSTEM EXPLANATION:
# Canvas uses (x, y) coordinates where:
# - (0, 0) is at TOP-LEFT corner
# - X increases going RIGHT
# - Y increases going DOWN
# - So (500, 500) would be bottom-right corner of our 500x500 canvas

# 1. CREATE_LINE Examples
print("Drawing lines...")
# Basic diagonal line from top-left to bottom-right
canvas.create_line(
    0, 0,        # Starting point (x1, y1)
    500, 500,    # Ending point (x2, y2)
    fill='blue', # Line color
    width=3      # Line thickness in pixels
)

# Multi-point line (creates connected line segments)
canvas.create_line(
    50, 50,      # Point 1
    100, 20,     # Point 2 
    150, 80,     # Point 3
    200, 30,     # Point 4
    fill='red',
    width=2,
    smooth=True  # Makes line curved instead of sharp angles
)

# 2. CREATE_RECTANGLE Examples
print("Drawing rectangles...")
# Basic rectangle - specify opposite corners
canvas.create_rectangle(
    50, 100,     # Top-left corner (x1, y1)
    150, 150,    # Bottom-right corner (x2, y2)
    fill='green',    # Fill color
    outline='black', # Border color
    width=2          # Border thickness
)

# Rectangle with no fill (just outline)
canvas.create_rectangle(200, 100, 300, 150, outline='purple', width=3)

# 3. CREATE_OVAL Examples (Circles and Ovals)
print("Drawing ovals and circles...")
# Oval - width != height
canvas.create_oval(
    350, 100,    # Top-left of bounding box
    450, 150,    # Bottom-right of bounding box
    fill='yellow',
    outline='orange',
    width=2
)

# Perfect circle using our function - center at (125, 225), radius 30
draw_circle(canvas, 125, 225, 30, 'cyan')

# Another circle - center at (250, 250), radius 40
draw_circle(canvas, 250, 250, 40, 'pink')

# Manual circle (same as function but written out)
center_x, center_y, radius = 375, 225, 35
canvas.create_oval(
    center_x - radius,  # x1 = center_x - radius
    center_y - radius,  # y1 = center_y - radius  
    center_x + radius,  # x2 = center_x + radius
    center_y + radius,  # y2 = center_y + radius
    fill='lightblue',
    outline='navy',
    width=2
)

# 4. CREATE_ARC Examples (Partial circles, pie slices)
print("Drawing arcs...")
# Arc explanation:
# - start: starting angle in degrees (0° = 3 o'clock, 90° = 6 o'clock)
# - extent: how many degrees to draw from start point
# - Angles go clockwise

# Half circle (semi-circle)
canvas.create_arc(
    50, 300,     # Top-left of bounding box
    150, 400,    # Bottom-right of bounding box
    start=0,     # Start at 3 o'clock position (0°)
    extent=180,  # Draw 180° (half circle)
    fill='orange',
    outline='red',
    width=2
)

# Quarter circle
canvas.create_arc(200, 300, 300, 400, start=90, extent=90, fill='lightgreen')

# Almost full circle (your original example)
canvas.create_arc(
    350, 300,    # Bounding box coordinates
    450, 400,
    start=0,     # Start at 0°
    extent=359,  # Draw 359° (almost full circle, missing 1°)
    outline='black',
    width=3,
    style='arc'  # Just the arc outline, not filled
)

# Pac-Man shape
canvas.create_arc(
    50, 420,
    120, 490,
    start=30,    # Start at 30°
    extent=300,  # Draw 300° (leaves 60° gap for mouth)
    fill='yellow',
    outline='black',
    width=2
)

# 5. CREATE_POLYGON Examples (Custom shapes)
print("Drawing polygons...")
# Triangle - need at least 3 points
canvas.create_polygon(
    200, 450,    # Point 1 (x1, y1)
    170, 490,    # Point 2 (x2, y2)  
    230, 490,    # Point 3 (x3, y3)
    fill='red',
    outline='darkred',
    width=2
)

# Pentagon (5-sided shape)
canvas.create_polygon(
    300, 450,  # Top point
    285, 465,  # Upper left
    295, 485,  # Lower left
    305, 485,  # Lower right
    315, 465,  # Upper right
    fill='purple',
    outline='black',
    width=1
)

# 6. CREATE_TEXT Examples
print("Adding text...")
# Basic text
canvas.create_text(
    250, 50,     # Position (x, y) - this is the CENTER of text
    text="Canvas Drawing Tutorial",
    font=("Arial", 16, "bold"),  # (font_name, size, style)
    fill='darkblue'
)

# Text with different alignment
canvas.create_text(
    400, 75,
    text="Multiple\nLine\nText",  # \n creates new lines
    font=("Times", 12),
    fill='green',
    justify='center'  # Text alignment
)

# 7. Demonstrating Canvas Methods
print("Canvas created with methods:")
print("- create_line(): draws straight lines")
print("- create_rectangle(): draws rectangles and squares") 
print("- create_oval(): draws circles and ovals")
print("- create_arc(): draws partial circles/pie slices")
print("- create_polygon(): draws custom shapes with multiple points")
print("- create_text(): adds text to canvas")

# Additional useful canvas methods (not demonstrated but good to know):
# - create_image(): adds images (GIF, PGM, PPM formats)
# - create_bitmap(): adds bitmap images
# - delete(): removes items from canvas
# - move(): moves items to new position
# - coords(): gets or sets coordinates of items

# Pack the canvas into the window (makes it visible)
canvas.pack(
    padx=10,     # Horizontal padding around canvas
    pady=10      # Vertical padding around canvas
)

# Additional explanation of __init__ method:
# When you write Canvas(window, height=500, width=500, bd=5)
# Python automatically calls Canvas.__init__(self, window, height=500, width=500, bd=5)
# The __init__ method is a constructor that initializes the Canvas object with your settings
# It's like a setup function that runs when the object is created

# Start the GUI event loop - this keeps the window open and responsive
window.mainloop()  # This runs continuously, waiting for user interaction

# SUMMARY FOR EXAMS:
# 1. Canvas coordinates: (0,0) = top-left, X increases right, Y increases down
# 2. Circle from center/radius: x1=cx-r, y1=cy-r, x2=cx+r, y2=cy+r
# 3. Arc angles: start=starting angle, extent=degrees to draw, 0°=3 o'clock
# 4. All create_* methods return an ID that can be used to modify/delete the item later
# 5. Canvas must be packed/placed to be visible in window
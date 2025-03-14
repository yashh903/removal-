# -*- coding: utf-8 -*-
"""removal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Re-9JnE6SJJOo6BCJgX32lBNdmt2wo5a
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def remove_pipes_and_text(image_path, output_path):
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ---- Step 1: Detect Pipes ----
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    pipes_mask = np.zeros_like(gray)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(pipes_mask, (x1, y1), (x2, y2), 255, thickness=30)  # Increase thickness for better removal

    # ---- Step 2: Detect All Text ----
    text_mask = np.zeros_like(gray)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # Inverted binary image

    # Find contours (text regions)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 10 < w < 200 and 10 < h < 100:  # Ignore small noise
            cv2.rectangle(text_mask, (x, y), (x + w, y + h), 255, thickness=-1)

    # ---- Step 3: Keep Only Text on Pipes ----
    pipe_text_mask = cv2.bitwise_and(text_mask, pipes_mask)  # Text overlapping with pipes

    # ---- Step 4: Combine Pipe and Pipe Text Masks ----
    final_mask = cv2.bitwise_or(pipes_mask, pipe_text_mask)

    # ---- Step 5: Inpaint to Remove Pipes & Text ----
    inpainted = cv2.inpaint(image, final_mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    # Display results
    cv2_imshow(inpainted)

    # Save output
    cv2.imwrite(output_path, inpainted)
    print(f"Processed image saved at: {output_path}")

# Run function
remove_pipes_and_text("/content/input.jpg", "/content/processed_output.jpg")


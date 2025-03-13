Removing Connecting Lines (Pipes) from a Technical Diagram

Approach
This script removes connecting pipes and text from engineering diagrams using image processing techniques in OpenCV. The approach consists of the following steps:

1. **Load and Convert Image**: The image is read and converted to grayscale for processing.
2. **Detect Pipes**: Using Canny edge detection and Hough Line Transform, pipes are detected and masked.
3. **Detect Text**: A binary threshold is applied to identify text regions, and contours are used to create a text mask.
4. **Identify Text on Pipes**: A mask is created to retain only the text overlapping with pipes.
5. **Combine Masks**: The pipe mask and pipe-text mask are merged into a final mask.
6. **Inpainting**: OpenCV’s inpainting method is used to remove the detected pipes and text while preserving the background.
7. **Save Processed Image**: The modified image is displayed and saved.


### Installation
```
pip install opencv-python numpy
```
### Running the Script
1. Place the input image in the working directory.
2. Modify the script to point to the correct input image path.
3. Run the script in Google Colab or a local Python environment:
```python
remove_pipes_and_text("input.jpg", "processed_output.jpg")
```
4. The processed image will be saved as `processed_output.jpg`.

## Libraries Used
- **OpenCV**: For image processing (loading images, edge detection, contour detection, inpainting)
- **NumPy**: For array manipulations and mask operations

## Notes
- Adjust the `thickness` of the pipe mask if necessary to ensure better removal.
- Modify `minLineLength` and `maxLineGap` in `HoughLinesP` for better line detection.
- Tune `inpaintRadius` for better inpainting results.

import cv2
import numpy as np

class CannyEdgeDetector:
    def __init__(self, low_threshold, high_threshold):
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold

    def detect_edges(self, image):
        """
        Detect edges in an image using the Canny edge detection algorithm.

        Args:
            image: An image in which edges are to be detected.

        Returns:
            An image with edges detected.
        """
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Canny edge detector
        edges = cv2.Canny(blurred, self.low_threshold, self.high_threshold)

        return edges

# Example usage
if __name__ == "__main__":
    # Read an image
    image = cv2.imread('path_to_your_image.jpg')

    # Initialize the Canny Edge Detector with thresholds
    detector = CannyEdgeDetector(low_threshold=50, high_threshold=150)

    # Detect edges
    edges = detector.detect_edges(image)

    # Display the edges
    cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

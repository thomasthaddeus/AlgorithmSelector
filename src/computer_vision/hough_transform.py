import cv2
import numpy as np

class HoughLineDetector:
    def __init__(self, rho, theta, threshold):
        self.rho = rho  # Distance resolution of the accumulator in pixels
        self.theta = theta  # Angle resolution of the accumulator in radians
        self.threshold = threshold  # Accumulator threshold parameter

    def detect_lines(self, image):
        """
        Detect lines in an image using the Hough Line Transform.

        Args:
            image: An image in which lines are to be detected.

        Returns:
            An image with detected lines.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Canny edge detector
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        # Apply Hough Line Transform
        lines = cv2.HoughLines(edges, self.rho, self.theta, self.threshold)

        # Draw lines on the original image
        if lines is not None:
            for rho, theta in lines[:,0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

        return image

# Example usage
if __name__ == "__main__":
    # Read an image
    image = cv2.imread('path_to_your_image.jpg')

    # Initialize the Hough Line Detector
    detector = HoughLineDetector(rho=1, theta=np.pi/180, threshold=100)

    # Detect lines
    lined_image = detector.detect_lines(image)

    # Display the lines
    cv2.imshow('Hough Lines', lined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

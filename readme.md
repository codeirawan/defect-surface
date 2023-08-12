# Defect Surface Analysis with Python

This tutorial will guide you through the process of setting up your Python environment, installing the required libraries, and building a program for Defect Surface analysis using image processing techniques and your logic.

## Prerequisites

- Python 3.x (https://www.python.org/downloads/)
- pip (Python package installer, usually comes with Python)

## Getting Started

1. **Clone the Repository**

    Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/codeirawan/defect-surface-analysis.git
    cd defect-surface-analysis
    ```

2. **Setup Virtual Environment (Optional, but recommended)**

    It's a good practice to create a virtual environment to manage your project dependencies separately. Run the following commands:

    ```bash
    # On Windows
    python -m venv venv

    # On macOS and Linux
    python3 -m venv venv
    ```

    Activate the virtual environment:

    ```bash
    # On Windows
    venv\Scripts\activate

    # On macOS and Linux
    source venv/bin/activate
    ```

3. **Install Required Libraries**

    Install the required Python libraries using pip:

    ```bash
    pip install opencv-python numpy
    ```

4. **Run the Program**

    Execute the Python script to run the Defect Surface analysis program:

    ```bash
    python defect-surface.py
    ```

    The program will analyze a sample Defect Surface image and display the result.

## Program Explanation

- The `DefectSurfaceAnalysis` class contains methods to preprocess the image, apply GrabCut segmentation, and perform Defect Surface analysis using your logic.
- The `preprocess_image` method resizes, converts to grayscale, and applies thresholding to the input image.
- The `apply_grabcut` method performs GrabCut segmentation on the preprocessed image.
- The `analyze_defect_surface` method orchestrates the entire analysis process.
- In the `if __name__ == "__main__":` block, the program creates an instance of the `DefectSurfaceAnalysis` class, analyzes the sample image, and displays the result using OpenCV.

## Conclusion

You've successfully set up your Python environment, installed necessary libraries, and run the Defect Surface analysis program. You can customize the program further to suit your needs or integrate it into larger projects.

Feel free to explore and experiment with different images and analysis techniques!
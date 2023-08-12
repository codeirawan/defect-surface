import cv2
import numpy as np

class DefectSurfaceAnalysis:
    def preprocess_image(self, image_path):
        # Load the image
        img = cv2.imread(image_path)
        
        # Resize the image to a fixed size (200x150)
        img_resize = cv2.resize(img, (200, 150))
        
        # Convert the resized image to grayscale
        img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
        
        # Apply Otsu's thresholding to create a binary image
        ret, th = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        return th

    def apply_grabcut(self, img_resize, rect, iter_count=10):
        # Convert the grayscale image to color for grabCut
        img_color = cv2.cvtColor(img_resize, cv2.COLOR_GRAY2BGR)

        # Initialize mask, background, and foreground models
        mask = np.zeros(img_color.shape[:2], dtype="uint8")
        bg_model = np.zeros((1, 65), dtype="float")
        fg_model = np.zeros((1, 65), dtype="float")

        # Apply grabCut algorithm
        cv2.grabCut(
            img_color, mask, rect, bg_model, fg_model, iterCount=iter_count, mode=cv2.GC_INIT_WITH_RECT
        )

        # Create a binary mask from grabCut result
        output_mask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
        output_mask = (output_mask * 255).astype("uint8")

        # Apply the binary mask to the original image to obtain the result
        grabcut_result = cv2.bitwise_and(img_color, img_color, mask=output_mask)
        return grabcut_result

    def analyze_defect_surface(self, image_path):
        # Preprocess the image
        th = self.preprocess_image(image_path)
        
        # Define a rectangle for grabCut
        rect = (1, 1, 200, 150)
        
        # Apply grabCut algorithm
        grabcut_result = self.apply_grabcut(th, rect)
        return grabcut_result

if __name__ == "__main__":
    image_path = "image/ok.jpg"
    
    # Create an instance of the DefectSurfaceAnalysis class
    analysis = DefectSurfaceAnalysis()
    
    # Analyze the defect surface image using the defined processes
    result = analysis.analyze_defect_surface(image_path)

    # Display the result image if it is valid
    if result is not None and result.shape[0] > 0 and result.shape[1] > 0:
        cv2.imshow("Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to display the result image.")

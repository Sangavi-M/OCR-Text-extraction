import cv2
import pytesseract

# Path to the video file
video_path = 'sample1.mp4'

# Specify the path to the Tesseract executable if not in system PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path as per your installation

# Initialize the video capture object
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize a variable to hold the collected text
collected_text = ""

frame_count = 0
while True:
    ret, frame = cap.read()
    
    # Break the loop if no frame is returned
    if not ret:
        break
    
    frame_count += 1
    
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to get a binary image
    _, binary_frame = cv2.threshold(gray_frame, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Perform OCR on the frame
    text = pytesseract.image_to_string(binary_frame)
    
    # Append the extracted text to the collected_text variable
    collected_text += text + "\n"
    
    print(f"Processed frame {frame_count}")

# Release the video capture object
cap.release()

# Display the collected text
print("Collected OCR text from video:")
print(collected_text)
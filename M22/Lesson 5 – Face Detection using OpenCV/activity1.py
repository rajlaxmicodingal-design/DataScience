import os
import cv2

# Securely locate the built-in system path to OpenCV's Haar Cascade files
BUILTIN_CASCADE_PATH = os.path.join(
    cv2.data.haarcascades, "haarcascade_frontalface_default.xml"
)

# Safely track down the exact path of this python script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "person.jpg")

# Initialize the face recognition model
face_cascade = cv2.CascadeClassifier(BUILTIN_CASCADE_PATH)

# Verify image asset reads successfully
img = cv2.imread(IMAGE_PATH)

if img is None:
    print(f"Error: Could not open the image at: {IMAGE_PATH}")
    print("Please make sure 'mario.png' is dropped directly inside your code's folder!")
else:
    # Convert image to grayscale (Haar Cascades evaluate 1-channel pixel arrays)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    
    print(f"Detected face array matrices coordinates: {faces}")

    # Draw a green bounding box rectangle around every face structure detected
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # ====================================================================
    # CRITICAL FIX: Named window + waitKey holds the interface alive
    # ====================================================================
    cv2.imshow("Face Detection Result", img)   # Combined visualization window
    
    print("\n👉 Window opened! Click ON the image window and press ANY key to exit safely.")
    
    cv2.waitKey(0)          # Infinitely pauses script execution to display the image
    cv2.destroyAllWindows() # Completely purges memory handles upon keyboard key strike
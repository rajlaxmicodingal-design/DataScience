import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from vcam import meshGen, vcam

# 1. Locate the exact directory path of this python script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Auto-scan for hidden Windows file extensions
POSSIBLE_EXTENSIONS = ["minions.jpg", "minions.png", "minions.jpeg", "minions.JPG"]
IMAGE_PATH = None

for ext in POSSIBLE_EXTENSIONS:
    test_path = os.path.join(SCRIPT_DIR, ext)
    if os.path.exists(test_path):
        IMAGE_PATH = test_path
        break

# =====================================================================
# IMAGE LOADING & RENDERING LAYER
# =====================================================================
plt.figure(figsize=(20, 10))

if IMAGE_PATH is None:
    print(f"\n❌ ERROR: 'minions' image file was NOT found in: {SCRIPT_DIR}")
else:
    # -----------------------------------------------------------------
    # CRITICAL WORKAROUND FOR ENCODING CRASHES
    # Read the file as raw bytes so OpenCV doesn't read the folder path!
    # -----------------------------------------------------------------
    try:
        with open(IMAGE_PATH, "rb") as f:
            file_bytes = np.frombuffer(f.read(), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    except Exception as e:
        img = None
        print(f"File streaming failed: {e}")

    if img is None:
        print("❌ Error: Memory stream extraction failed. The file may be corrupt.")
    else:
        print("✔ Image array decoded perfectly in-memory!")
        H, W = img.shape[:2]

        # Creating the virtual camera object
        c1 = vcam(H=H, W=W)

        # Creating the 3D grid surface mesh object
        plane = meshGen(H, W)

        # Apply the runny mirror distortion math formula
        plane.Z += (
            20
            * np.exp(-0.5 * ((plane.X * 1.0 / plane.W) / 0.1) ** 2)
            / (0.1 * np.sqrt(2 * np.pi))
        )

        # Project the structural 3D vectors back into the 2D layout plane
        pts3d = plane.getPlane()
        pts3d = c1.project(pts3d)
        map_x, map_y = c1.getMaps(pts3d)

        # Execute pixel re-mapping logic using bilinear interpolation
        output = cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR)

        # Stack images horizontally for clear processing visualization
        visual_comparison = cv2.cvtColor(np.hstack((img, output)), cv2.COLOR_BGR2RGB)

        # Render results via matplotlib subplots panel canvas
        plt.subplot(1, 1, 1)
        plt.title("Runny Mirror Effect (Original vs. Distorted)", fontsize=16)
        plt.imshow(visual_comparison)
        plt.axis("off")  # Removes pixel grid numbers for a clean output look

        # Displays the final generated matplotlib layout window on screen
        plt.show()

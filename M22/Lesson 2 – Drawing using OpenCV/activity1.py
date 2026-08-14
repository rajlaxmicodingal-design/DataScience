import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import cv2
import matplotlib.pyplot as plt

emptyImg = np.zeros(shape=(512, 512, 3), dtype=np.int16)

plt.imshow(emptyImg)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define your input shape and number of classes based on your dataset
# Example: 28x28 pixels with 3 color channels (RGB), and 10 output classes
input_shape = (28, 28, 3)
num_classes = 10

# 1. Initialize the Sequential model
model = Sequential()

# 2. Add the Convolutional Layer
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))

# 3. Add the Pooling Layer for downsampling
model.add(MaxPooling2D(pool_size=(2, 2)))

# (Optional) You can add more Conv2D and MaxPooling2D layers here for deeper feature extraction
# model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))

# 4. Add the Flattening Layer to convert 2D maps to 1D feature vectors
model.add(Flatten())

# 5. Add the Dense Output Layer for classification
model.add(Dense(num_classes, activation='softmax'))

# View the architecture summary
model.summary()
import os
import cv2
import torch
from ultralytics import YOLO

# Paths and directories
MODEL_PATH = "yolov8m.pt"  # Path to pre-trained weights
DATASET_CONFIG = "data/tomato_flowers.yaml"  # Path to dataset configuration
TRAIN_IMAGES_DIR = "dataset/train/images"  # Directory for training images
VAL_IMAGES_DIR = "dataset/val/images"  # Directory for validation images
INPUT_DIR = "images/input"  # Directory for input images for inference
OUTPUT_DIR = "images/output"  # Directory for output results
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to train the model
def train_model():
    print("Starting training...")
    model = YOLO(MODEL_PATH)
    model.train(data=DATASET_CONFIG, epochs=50, batch=16, imgsz=640)
    print("Training completed.")
    return model

# Function to run inference on a single image
def detect_tomato_flowers(model, image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Run YOLOv8 inference
    results = model(image)

    # Draw detections on the image
    annotated_image = results[0].plot()

    # Save the annotated image
    cv2.imwrite(output_path, annotated_image)
    print(f"Processed and saved: {output_path}")

# Main execution
if __name__ == "__main__":
    # Step 1: Check for dataset directories
    if not os.path.exists(TRAIN_IMAGES_DIR) or not os.path.exists(VAL_IMAGES_DIR):
        print(f"Dataset directories missing: {TRAIN_IMAGES_DIR} or {VAL_IMAGES_DIR}")
        exit(1)

    # Step 2: Train the model
    model = train_model()

    # Step 3: Perform inference
    print("Starting inference...")
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"detected_{filename}")
            detect_tomato_flowers(model, input_path, output_path)

    print("Tomato flower detection completed.")

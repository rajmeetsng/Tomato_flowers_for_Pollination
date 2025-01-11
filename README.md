# Tomato_flowers_for_Pollination

This repository contains the Tomato flower dataset from Greenhouse, which is used for pollination task.

Detection dataset link: https://app.roboflow.com/raj-brtgt/flower-fnshn/2594

# Flower and Bud Detection Algorithm

This repository demonstrates object detection using the YOLOv8 model, a state-of-the-art deep learning architecture for detecting objects in images and videos. The implementation provides a streamlined pipeline for training, evaluation, and deployment.

## Features

- Efficient and accurate object detection using YOLOv8.
- Real-time inference on video streams or image directories.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Dataset Preparation](#dataset-preparation)
  - [Training](#training)
  - [Inference](#inference)
  - [Evaluation](#evaluation)
- [Results](#results)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/yolov8-object-detection.git
   cd yolov8-object-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify installation:
   ```bash
   python check_env.py
   ```

---

## Usage

### Dataset Preparation

1. Organize your dataset in the following structure:
   ```
   dataset/
   ├── train/
   │   ├── images/
   │   ├── labels/
   ├── val/
   │   ├── images/
   │   ├── labels/
   ```

2. Ensure the annotations are in YOLO format.

3. Update the `config.yaml` file with dataset paths:
   ```yaml
   train: dataset/train/images
   val: dataset/val/images
   nc: 2
   names: ["flowers", "bud"]
   ```

### Training

Train the YOLOv8 model on your dataset:
```bash
python train.py --data config.yaml --epochs 100 --batch-size 16 --weights yolov8m.pt
```

### Inference

Run inference on an image or directory of images:
```bash
python detect.py --weights best.pt --source images/
```

### Evaluation

Evaluate the trained model on the validation dataset:
```bash
python val.py --data config.yaml --weights best.pt
```

---

## Results

<img align="middle" src="Results/1.png" width="300"> <img align="middle" src="Results/2.jpg" width="200"> <img align="middle" src="Results/4.jpg" width="200">

---

# Citation
If you use this work, please cite:
```
R Singh et al. 2024. Deep learning approach for detecting tomato flowers and buds in greenhouses on 3P2R gantry robot. Scientific Reports, 14(1), p.20552.
```
BibTeX:
```
@article{singh2024deep,
  title={Deep learning approach for detecting tomato flowers and buds in greenhouses on 3P2R gantry robot},
  author={Singh, Rajmeet and Khan, Asim and Seneviratne, Lakmal and Hussain, Irfan},
  journal={Scientific Reports},
  volume={14},
  number={1},
  pages={20552},
  year={2024},

  publisher={Nature Publishing Group UK London}
}
```
---

## Acknowledgements

- YOLOv8: [Ultralytics](https://github.com/ultralytics/yolov8)

---

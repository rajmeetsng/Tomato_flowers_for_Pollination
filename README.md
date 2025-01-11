# Tomato_flowers_for_Pollination

This repository contains the Tomato flower dataset from Greenhouse, which is used for pollination task.

Detection dataset link: https://app.roboflow.com/raj-brtgt/flower-fnshn/2594

# Code

# Object Detection using YOLOv8 Model

This repository demonstrates object detection using the YOLOv8 model, a state-of-the-art deep learning architecture for detecting objects in images and videos. The implementation provides a streamlined pipeline for training, evaluation, and deployment.

## Features

- Efficient and accurate object detection using YOLOv8.
- Support for custom datasets and pre-trained models.
- Easy-to-use training and inference scripts.
- Real-time inference on video streams or image directories.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Dataset Preparation](#dataset-preparation)
  - [Training](#training)
  - [Inference](#inference)
  - [Evaluation](#evaluation)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

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
   nc: <number_of_classes>
   names: ["class_1", "class_2", ...]
   ```

### Training

Train the YOLOv8 model on your dataset:
```bash
python train.py --data config.yaml --epochs 50 --batch-size 16 --weights yolov8m.pt
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

## Model Architecture

YOLOv8 introduces enhancements in both the backbone and head for more efficient feature extraction and prediction. The YOLOv8m variant is optimized for medium-sized deployments, balancing speed and accuracy.

---

## Results

Include example results and metrics, such as:
- Mean Average Precision (mAP): 0.85
- Inference time: 15ms per image

| Image | Detection |
|-------|-----------|
| ![example1](results/example1.png) | ![example2](results/example2.png) |

---

## Contributing

Contributions are welcome! If you encounter any issues or want to enhance the repository, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- YOLOv8: [Ultralytics](https://github.com/ultralytics/yolov8)
- Contributors and community feedback.





# Results

<img align="middle" src="Results/1.png" width="300"> <img align="middle" src="Results/2.jpg" width="200"> <img align="middle" src="Results/4.jpg" width="200">

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


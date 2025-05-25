# NexaQuanta AI-CV Engineer Assessment

This repository contains complete solutions for all 5 tasks assigned in the Nexaquanta AI-CV Engineer Test. The tasks include Python fundamentals, algorithm implementation, deep learning with CNNs, and object detection using both YOLOv8 and Faster R-CNN. The solutions are clean, modular, reproducible, and aligned with professional standards.

---

## Task 1: Python and Algorithmic Problem Solving

- **1.1 Fix Broken Code:** Corrected a syntactically broken Python function by handling logic, indentation, and structure.
- **1.2 Remove Duplicates (No Built-ins):** Manually removed duplicates from a list using only loops and conditionals.
- **1.3 Sort List of Tuples:** Sorted a list of tuples by the second element using a custom key function.
- **1.4 Aggregate CSV Data:** Parsed a CSV file, aggregated values by category, and wrote output to a new CSV file using only `csv.reader` and `csv.writer`.
- **1.5 Parse JSON to Nested Dict:** Recursively parsed and converted a complex JSON file into Python dictionaries and lists.

---

## Task 2: Implement KMeans Algorithm from Scratch

- Implemented KMeans using only NumPy.
- Steps included:
  - Random centroid initialization
  - Euclidean distance-based assignment
  - Centroid updates
  - Convergence check
- Visualization included for clustered outputs with distinct colors for each cluster.

---

## Task 3: CNN Model Using PyTorch

- Built a custom Convolutional Neural Network for image classification using PyTorch.
- Included:
  - Conv2D → ReLU → MaxPool2D → Linear layers
  - CrossEntropyLoss and Adam optimizer
  - Training loop with loss/accuracy tracking
  - Evaluation on validation data
- Followed best practices with `torchvision.transforms` for image normalization and augmentation.

---

## Task 4: Object Detection Using YOLOv8

- **Dataset:**
  - Images: `/kaggle/input/road-sign-detection/images`
  - Pascal VOC Annotations: `/kaggle/input/road-sign-detection/annotations`
- **Annotation Conversion:**
  - Converted `.xml` files to YOLOv8 `.txt` format.
  - Stored labels in `/kaggle/working/labels`.
- **Data.yaml:**
  - Configured with correct paths and class names without subdirectories.
- **Training:**
  - Trained YOLOv8n for 30 epochs using Ultralytics API.
- **Evaluation:**
  - Achieved:
    - mAP@0.5: 0.994
    - mAP@0.5:0.95: 0.912
    - Precision: 0.996
    - Recall: 0.984
    - Inference speed: ~2.2ms per image
- **Visualization:**
  - Used OpenCV and Matplotlib to display predictions with bounding boxes and confidence scores.

---

## Task 5: Object Detection Using Faster R-CNN

- **Dataset:**
  - Images: `/kaggle/input/road-sign-detection/images`
  - Annotations: `/kaggle/input/road-sign-detection/annotations`
- **Custom Dataset:**
  - Built PyTorch `Dataset` class to parse VOC `.xml` files and load images.
- **Model:**
  - Used `torchvision.models.detection.fasterrcnn_resnet50_fpn`
  - Replaced classification head with `FastRCNNPredictor` for 4 road sign classes.
- **Training:**
  - Trained for 10 epochs using SGD optimizer.
  - Loss reduced from 29.00 → 10.28.
- **Evaluation:**
  - Used `torchmetrics.MeanAveragePrecision` to calculate:
    - mAP@0.5: ~0.98
    - mAP@0.5:0.95: ~0.90
  - Verified via both metric output and visual inspection.
- **Visualization:**
  - Plotted predictions with class labels and confidence scores using OpenCV and Matplotlib.

---

## Final Comparison

| Metric         | YOLOv8n     | Faster R-CNN |
|----------------|-------------|--------------|
| mAP@0.5        | 0.994       | ~0.98        |
| mAP@0.5:0.95   | 0.912       | ~0.90        |
| Precision      | 0.996       | High         |
| Recall         | 0.984       | High         |
| Inference Time | ~2.2 ms/img | ~100+ ms/img |

---

## Conclusion

- **YOLOv8n is the preferred model** for real-time road sign detection due to:
  - High mAP, precision, and recall
  - Extremely fast inference suitable for deployment
  - Simple training pipeline using Ultralytics
- **Faster R-CNN** is more suitable for:
  - Academic research and custom control
  - Scenarios where speed is not critical
  - Projects requiring full PyTorch modularity
- Both models achieved strong results, but YOLOv8n is recommended for production-grade systems.

---

## Submission Notes

- All 5 tasks are completed thoroughly as per the provided PDF.
- All requirements — from directory structure to output formats — have been strictly followed.
- The code is modular, reproducible, professional, and ready for review.
- Notebooks include inline documentation, plots, loss curves, prediction visuals, and evaluation metrics.

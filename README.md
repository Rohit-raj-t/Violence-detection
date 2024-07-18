# Violence Detection Using YOLOv8

## Overview

This repository contains the code for a violence detection system using YOLOv8. The model is trained to identify violent actions in real-time video streams.

## Team Member

- **Rohit Raj**

## Model Details

- **Model:** YOLOv8n
- **Epochs:** 100
- **Dataset Description:**
    - **Classes:**
        - NonViolence
        - Violence
        - Guns
        - Knife
    - **Data Split:**
        - Total Images: 13,636
        - Train: 12,266 (90.0%)
        - Validation: 948 (7.0%)
        - Test: 422 (3.1%)
    - **Image Size:** 640x640
    - **Patience:** 100
    - **Automatic Batch Size:** Variable

## Usage

1. Clone the repository.
2. Download the pretrained YOLOv8n model.
3. Run the violence detection script on your video stream.

## Acknowledgments

Rohit Raj T

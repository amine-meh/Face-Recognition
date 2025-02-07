# Face Recognition Program

## Description
This project is a Python-based face recognition system that utilizes the `face_recognition` library to detect, extract, and match faces from images. The repository consists of four Python scripts:

1. **Face Detection**: Identifies faces in an image.
2. **Face Extraction**: Extracts and saves detected faces as individual image files.
3. **Face Matching**: Compares faces to check if they belong to the same person.
4. **Face Recognition**: Recognizes known individuals from a group image and labels them.

## Features
- Detect faces from images.
- Extract faces and save them as separate image files.
- Compare two faces to determine if they belong to the same person.
- Recognize faces in a group image and label them.

## Installation
### Prerequisites
Ensure you have Python installed (>= 3.6) along with the following dependencies:

```bash
pip install face_recognition pillow numpy
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/face_recognition_program.git
cd face_recognition_program
```

## Usage
### 1. Face Detection
Run the face detection script to locate faces in an image:
```bash
python face_detection.py
```

### 2. Face Extraction
Extract faces and save them as separate image files:
```bash
python face_extraction.py
```

### 3. Face Matching
Compare two faces and check if they belong to the same person:
```bash
python face_matching.py
```

### 4. Face Recognition
Recognize known individuals in a group image:
```bash
python face_recognition.py
```

## File Structure
```
face_recognition_program/
│── img/
│   ├── known/   # Folder containing known faces
│   ├── groups/  # Folder containing test images
│── face_detection.py  # Detects faces in an image
│── face_extraction.py  # Extracts and saves faces as separate images
│── face_matching.py  # Compares faces to check for matches
│── face_recognition.py  # Recognizes and labels known individuals
│── requirements.txt  # List of dependencies
│── README.md  # Project documentation
```

## Dependencies
- `face_recognition`
- `Pillow`
- `numpy`

## License
This project is licensed under the MIT License.

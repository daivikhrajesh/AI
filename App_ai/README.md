# Digit Recognition Web Application

This repository contains a web application built with Flask for recognizing hand-written digits using a convolutional neural network (CNN) trained on the MNIST dataset.


## Features

- Upload an image containing a hand-written digit (`.jpg`, `.jpeg`, `.png` formats supported).
- Uses a pre-trained CNN model (`mnist_cnn.h5`) to predict the digit from the uploaded image.
- Displays the uploaded image and the predicted digit on a results page.

## Prerequisites

- Python 3.x
- Flask
- TensorFlow 2.x
- PIL (Python Imaging Library)
- numpy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/digit-recognition-flask.git
   ```

2. Navigate into the project directory:

   ```bash
   cd digit-recognition-flask
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000` to use the application.

3. Upload an image file containing a hand-written digit.

4. Click on the "Predict" button to see the predicted digit and the uploaded image.

## Training the Model

If you wish to retrain the CNN model:

1. Navigate to the `train_model.py` file.

2. Execute the script to train the model:

   ```bash
   python train_model.py
   ```

   This will train a new model using the MNIST dataset and save it as `mnist_cnn.h5`.

## Files Structure

- `app.py`: Flask application for serving the web interface and handling image uploads.
- `train_model.py`: Script to train the CNN model on the MNIST dataset and save it as `mnist_cnn.h5`.
- `templates/`: HTML templates for the web pages (`index.html`, `upload.html`).
- `static/`: Contains CSS styles and uploaded images.
- `mnist_cnn.h5`: Pre-trained CNN model for digit recognition.
>>>>>>> db091e62b56ac7d51b588e8ff36dc7bf3dc024c9

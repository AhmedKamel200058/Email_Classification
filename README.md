# Spam SMS Classifier

This project implements and evaluates machine learning models to classify SMS messages as either 'spam' or 'ham' (not spam). The goal is to build an effective model that can accurately detect unwanted messages.

## Table of Contents

1.  [Project Description](#project-description)
2.  [Dataset](#dataset)
3.  [Models Used](#models-used)
4.  [Evaluation Metrics](#evaluation-metrics)
5.  [Setup and Installation](#setup-and-installation)
6.  [Usage](#usage)
7.  [Deployment](#deployment)

## Project Description

This notebook demonstrates the process of building a spam SMS classification system. It covers:

*   **Data Loading and Preprocessing:** Loading the SMS dataset, checking for class imbalance, and converting text data into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency).
*   **Model Training:** Training two common classification models: Multinomial Naive Bayes and Logistic Regression.
*   **Model Evaluation:** Assessing model performance using metrics suitable for imbalanced datasets, such as Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
*   **Model Comparison:** Comparing the performance of the trained models.
*   **Model Export:** Saving the trained Logistic Regression model using `pickle`.
*   **Dependency Management:** Generating a `requirements.txt` file for easy environment setup.

## Dataset

The dataset used is `sms.csv`, which contains SMS messages labeled as 'spam' or 'ham'.

## Models Used

Two machine learning models were implemented and evaluated:

1.  **Multinomial Naive Bayes (MultinomialNB):** A probabilistic classifier well-suited for text classification tasks.
2.  **Logistic Regression:** A linear model for binary classification, often used as a baseline and known for its interpretability.

## Evaluation Metrics

Given the imbalanced nature of spam detection datasets (typically far more 'ham' messages than 'spam'), the following metrics were used for a comprehensive evaluation:

*   **Accuracy:** Overall correctness of the model.
*   **Precision:** The proportion of positive identifications that were actually correct.
*   **Recall:** The proportion of actual positives that were identified correctly.
*   **F1-Score:** The harmonic mean of precision and recall, providing a balance between the two.
*   **Confusion Matrix:** A table summarizing the performance of the classification model.

## Setup and Installation

To run this project, you'll need Python and the libraries listed in `requirements.txt`.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AhmedKamel200058/Email_Classification.git
    cd Email_Classification
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the environment is set up, you can run the Jupyter notebook `Email_Classification.ipynb` (or similar name) to see the full analysis, model training, and evaluation steps. 

## Deployment

The trained Logistic Regression model is saved as `logistic_regression_model.pkl`. This file can be loaded into a production environment for making predictions on new, unseen SMS messages. The `requirements.txt` file ensures that the necessary dependencies with compatible versions are installed in your deployment environment.
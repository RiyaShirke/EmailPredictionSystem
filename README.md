# Email Engagement Prediction System

This repository contains the code and dataset for building an **Email Engagement Prediction System** that classifies customer email responses as **Cold**, **Hot**, or **High** engagement levels. The system uses features such as the email's subject, customer response body, time of day, response time, and more to predict the engagement level.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Modeling](#modeling)
- [Dependencies](#dependencies)
- [Steps to Run](#steps-to-run)
- [Testing the Model](#testing-the-model)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to predict the engagement level of a customer based on their email response. The model is trained to classify emails as one of three levels:
1. **Cold**: Low engagement, e.g., disinterested or late response.
2. **Hot**: High engagement, e.g., prompt and positive response.
3. **High**: Moderate engagement, e.g., interested but delayed response.

This project is built using **scikit-learn**, **TF-IDF** vectorization, and a **Random Forest Classifier**. The dataset contains email subjects, customer response bodies, the time the response was sent, and other relevant features.

## Dataset

The dataset contains the following features:
- **Email Subject**: The subject of the email (from the business to the customer).
- **Email Body**: The customer’s response to the email.
- **Time Sent**: The time when the initial email was sent.
- **Response Time**: The time when the customer responded.
- **Level**: The target label that classifies the engagement as `Cold`, `Hot`, or `High`.
- **Engagement Score**: A score that reflects the engagement level, with higher scores indicating more interest.

You can find the dataset in this repository, or load it using a URL directly in Google Colab.

## Modeling

The model uses a **Random Forest Classifier** to predict the engagement level of an email response. Features such as the email length, time sent, response delay, and the text content of the subject and body are used for classification.

Key steps include:
1. **Feature Engineering**: Adding features such as `Email Length`, `Response Delay`, and `Time Sent Hour`.
2. **Text Vectorization**: Using **TF-IDF** vectorization to convert the email subject and response body into numerical data.
3. **Balancing the Dataset**: Using **SMOTE** (Synthetic Minority Over-sampling Technique) to handle class imbalances between `Cold`, `Hot`, and `High`.
4. **Model Training**: Training the Random Forest Classifier on the dataset.
5. **Model Evaluation**: Testing the model on unseen data and evaluating accuracy.

## Dependencies

The following libraries are required to run this project:

- `pandas`
- `numpy`
- `scikit-learn`
- `imbalanced-learn`
- `datetime`

To install the necessary libraries, run:

```bash
pip install pandas numpy scikit-learn imbalanced-learn
```

## Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/EmailPredictionSystem.git
   cd EmailPredictionSystem
   ```

2. **Load the Dataset**:
   You can load the dataset from the provided URL or use your own dataset. In the code, the dataset is loaded like this:

   ```python
   import pandas as pd

   url = "https://raw.githubusercontent.com/yourusername/EmailPredictionSystem/main/Email_Engagement_Dataset.csv"
   email_response_df = pd.read_csv(url)
   ```

3. **Run the Code**:
   You can run the Jupyter notebook or Python script to train the model and make predictions. The key steps include:
   - Data preprocessing and feature engineering.
   - Training the model using Random Forest Classifier.
   - Evaluating the model's accuracy on the test data.

4. **Test the Model**:
   After training the model, you can test it on sample customer responses. Here's an example of how to do that:

   ```python
   sample_responses = pd.DataFrame({
       'Email Subject': ["Meeting Request Response", "Special Offer Response", "Follow-Up Response"],
       'Email Body': [
           "Sure, let's schedule the meeting for tomorrow at 10 AM.",
           "I am interested in your offer. Can you send more details?",
           "Thanks, but I am currently not interested in pursuing this further."
       ],
       'Time Sent Hour': [12, 16, 11],  # Example response hours
       'Email Length': [len("Sure, let's schedule the meeting for tomorrow at 10 AM."),
                        len("I am interested in your offer. Can you send more details?"),
                        len("Thanks, but I am currently not interested in pursuing this further.")],
       'Response Delay': [2, 24, 72]  # Example response delays in hours (Hot, High, Cold)
   })

   # Vectorize and predict the engagement level using the trained model
   X_sample_combined = # (use the same process as in your training pipeline)
   y_sample_pred = model.predict(X_sample_combined)
   ```

5. **Evaluate Results**:
   The predicted engagement levels for the sample inputs will be either `Cold`, `Hot`, or `High`.

## Testing the Model

You can test the model using sample customer responses. For instance, provide the customer's response body along with other features like the time of day they responded and the delay in response. The model will predict whether the email response signifies `Cold`, `Hot`, or `High` engagement.

Sample test code is provided in the [test section](#test-the-model).




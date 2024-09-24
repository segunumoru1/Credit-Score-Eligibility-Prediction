The dataset consists of 2,000 records and 6 columns. Below is a description of the data, which will be included in the README file for the project:

### Dataset Overview
This dataset contains financial information related to individuals, along with a binary target variable indicating whether a client defaulted on a loan. It includes the following columns:

1. **clientid**: Unique identifier for each client (integer).
2. **income**: Annual income of the client (float).
3. **age**: Age of the client in years (float).
4. **loan**: Loan amount granted to the client (float).
5. **LTI (Loan-to-Income ratio)**: The ratio of the loan amount to the client’s income (float).
6. **default**: Binary target variable indicating loan default status, where `1` represents default and `0` indicates no default (integer).

The goal of this project is to predict whether a client will default on their loan based on the given features.

### Methodology
The following methodology was used to build the predictive model:

1. **Data Ingestion**: The data was loaded into a Python environment using pandas.
2. **Data Preprocessing and Validation**:
   - Checked for missing values, anomalies, and ensured data types were correctly set for each feature.
3. **Feature Selection**: All features were retained as they are considered relevant for the prediction task.
4. **Balancing the Data**: The dataset was balanced using the SMOTE (Synthetic Minority Over-sampling Technique) to handle any class imbalance in the `default` column.
5. **Train-Test Split**: The data was split into training and testing sets to ensure that the model's performance can be evaluated on unseen data.
6. **Data Scaling**: The features were scaled using the Min-Max Scaler to normalize the data before model training.
7. **Model Selection**: Several machine learning algorithms were evaluated, with a Random Forest classifier chosen as the baseline model.
8. **Model Evaluation**: The model was evaluated using various metrics, including:
   - **Accuracy**
   - **Precision**
   - **Recall**
   - **F1-score**
   - **AUC-ROC score**
9. **Hyperparameter Tuning**: RandomizedSearchCV was used to perform hyperparameter tuning on the Random Forest model, yielding the following performance metrics:
   - **Accuracy**: 0.999
   - **Precision**: 1
   - **Recall**: 1
   - **F1-score**: 1
10. **Model Saving**: The final model was saved using Python's pickle module for future predictions.

---

This README file provides an overview of the project, the data, and the steps taken to develop the predictive model.

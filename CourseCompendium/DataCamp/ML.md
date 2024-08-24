# Supervised Learning with scikit-learn

## What is Machine Learning?
Machine learning is the process by which computers can learn to make decisions from data without explicit programming.

## Examples of Machine Learning
- **Spam Detection:** Predicting whether an email is spam based on its content and sender.
- **Clustering Books:** Grouping books into categories based on their content and assigning new books to existing clusters.

## Unsupervised Learning
Unsupervised learning uncovers hidden patterns from **unlabeled data**.  
**Example:** A business grouping customers by purchasing behavior without predetermined categories (clustering).

## Supervised Learning
Supervised learning involves predicting known values using features to predict a target variable.  
**Example:** Predicting a basketball player's position based on their points per game.  
This course will focus exclusively on supervised learning.

## Types of Supervised Learning
| Type           | Description                                                              | Example                                                 |
|----------------|--------------------------------------------------------------------------|---------------------------------------------------------|
| **Classification** | Predicts the label/category of an observation                         | Identifying fraudulent vs. non-fraudulent bank transactions (binary classification) |
| **Regression**     | Predicts continuous values                                        | Predicting property prices based on features like the number of bedrooms and size |

## Naming Conventions
* **Feature:** Predictor variable or independent variable.
* **Target Variable:** Dependent variable or response variable.

## Before You Use Supervised Learning
Requirements for performing supervised learning include:
- Data must not have **missing values**.
- Data must be in **numeric format**.
- Data should be stored as **pandas DataFrames/Series** or **NumPy arrays**.

**Exploratory Data Analysis** (EDA) is essential to ensure data is formatted correctly. Useful tools include descriptive statistics and data visualizations.

## scikit-learn Syntax
scikit-learn maintains a consistent syntax across all supervised learning models, enhancing workflow repeatability. 

1. **Import Model:** Import the appropriate scikit-learn model (algorithm).
   - Example: k-Nearest Neighbors model.
   
2. **Instantiate Model:** Create a variable `model` and instantiate the model.
  
3. **Fit Model:** Fit the model to the data:
   - Use `X` for feature arrays.
   - Use `y` for target variable arrays.

4. **Make Predictions:** Use the model’s `predict` method with new observations:
   - Example: Feeding features from six emails to a spam classification model yields an array of predictions (1 for spam, 0 for not spam).
  



# Classification Challenge and k-Nearest Neighbors (KNN)

## 1. The Classification Challenge
- Supervised learning involves using labeled data to build classification models or classifiers for predicting labels of unseen data.

## 2. Classifying Labels of Unseen Data
- The process consists of four steps:
  1. Build a classifier that learns from labeled training data.
  2. Pass unlabeled data to the classifier to predict labels.

## 3. k-Nearest Neighbors (KNN)
- KNN is a popular algorithm for classification problems.
- It predicts a data point’s label by looking at the k closest labeled data points and using majority voting to assign the label.

## 4. KNN Example
- **Using a Scatter Plot:**
  - For k=3: The black observation is classified as red since two of the three closest observations are red.
  - For k=5: The black observation is classified as blue.
![image](https://github.com/user-attachments/assets/46bd7d2c-0bbc-4a86-86f8-91332e92bed2)

## 5. KNN Intuition
- A scatter plot visualizing total evening charge against total day charge for telecom customers illustrates how KNN works.
- Observations are colored blue for churned customers and red for non-churned.
- A decision boundary is created with k set to 15, predicting churn (gray background) or no churn (red background).
![image](https://github.com/user-attachments/assets/9df035a3-e727-4306-98b4-9aa07aa68abf)

## 6. Using scikit-learn to Fit a Classifier
- Steps to fit a KNN model using scikit-learn:
  1. Import `KNeighborsClassifier` from `sklearn.neighbors`.
  2. Split data into features (X) and target (y) arrays.
  3. Convert X and y to NumPy arrays.
  4. Create an instance of `KNeighborsClassifier` with n_neighbors set to 15.
  5. Fit the classifier to labeled data using the `fit` method.

## 7. Predicting on Unlabeled Data
- A new set of observations (X_new) is checked for shape (3 rows and 2 columns).
- Use the classifier's `predict` method on the unseen data.
- Predictions for X_new yield binary values: 
  - 1 for 'churn' (first observation),
  - 0 for 'no churn' (second and third observations).

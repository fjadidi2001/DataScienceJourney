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

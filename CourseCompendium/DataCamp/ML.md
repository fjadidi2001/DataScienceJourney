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



# Measuring Model Performance and Complexity in Classification

## 1. Introduction
After training a classifier, it's crucial to evaluate its performance to determine if it's making correct predictions.

## 2. Measuring Model Performance
### Accuracy
Accuracy is a commonly used metric in classification, defined as the number of correct predictions divided by the total number of observations. While easy to compute, evaluating accuracy solely on the training data isn’t sufficient, as it doesn’t reflect the model's ability to generalize to unseen data.

## 3. Computing Accuracy
### Train/Test Split
To properly measure accuracy, we typically split the dataset into a training set and a test set. The classifier is fitted to the training data, and its accuracy is then evaluated against the test set.

- **Implementation Steps**:
  - Import `train_test_split` from `sklearn.model_selection`.
  - Split the data, commonly using 20-30% of the data as the test set (e.g., `test_size=0.3`).
  - Set `random_state` for reproducibility.
  - Ensure the split reflects the proportion of classes by setting `stratify=y`.

This process returns four arrays: `X_train`, `X_test`, `y_train`, and `y_test`. After fitting a KNN model to the training data, we can check its accuracy using the `score` method on the test data, achieving an accuracy of around 88%.

## 4. Model Complexity
### Understanding k in KNN
In KNN, the parameter k determines the number of neighbors considered for making predictions. As k increases, the decision boundary becomes less sensitive to individual observations, resulting in a simpler model. While simpler models may underfit the training data, more complex models can lead to overfitting by capturing noise rather than general patterns.

## 5. Analyzing Overfitting and Underfitting
To evaluate how different k values affect model performance, we can create a model complexity curve:

- Create dictionaries to store training and test accuracies.
- Use a range of k values to instantiate multiple KNN models.
- Fit each model to the training data and calculate accuracies for both training and test sets.

## 6. Plotting Results
After collecting accuracies, we can plot the training and test accuracies against k values. The resulting graph reveals insights into model performance:

- As k increases beyond a certain point (e.g., 15), performance plateaus, indicating underfitting.
- The optimal test accuracy is observed around 13 neighbors, balancing complexity and generalization.

## Conclusion
Measuring model performance through accuracy on a test set and interpreting model complexity via varying k values are key to developing reliable classifiers. Understanding these concepts aids in avoiding underfitting and overfitting, ultimately leading to better predictive models.

```python
# Import the module
from sklearn.model_selection import train_test_split
X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
knn = KNeighborsClassifier(n_neighbors=5)

# Fit the classifier to the training data
knn.fit(X_train, y_train)
# Print the accuracy
print(knn.score(X_test, y_test))

```


<br>

# Overfitting and Underfitting

Interpreting model complexity is a great way to evaluate supervised learning performance. Your aim is to produce a model that can interpret the relationship between features and the target variable, as well as generalize well when exposed to new observations.

The training and test sets have been created from the `churn_df` dataset and preloaded as `X_train`, `X_test`, `y_train`, and `y_test`.

In addition, `KNeighborsClassifier` has been imported for you along with `numpy` as `np`.

# v1
- train = 0.8, test = 0.2
- pre-processing
- Accuracy is strong across all models, but there may be some bias.

# v2
- Two-way data split
    - simple split
    - k-fold

- pre-processing
- Train the model using k-fold cross-validation to achieve high accuracy across all models.

# v3
This version continues from version 2, with TabNet models training on a straightforward split.

- split dataset into train, validation, and test
- pre-process data
- Train the model and obtain results; overfitting may occur.
  
# v4 
- pre-process data
- split dataset into train, validation, test
- TabNet's accuracy is quite poor at each level

# v5
- Three-level pre-processing
Save each level as a CSV file.
- split dataset into train, validation, test
- Train the TabNet model to achieve 80% accuracy and excellent results.

# v6
- Three-level pre-processing
Save each level as a CSV file.
- The provided evaluation metrics assess the performance of a TanNet model across three different levels (Level 1, Level 2, and Level 3). Here's a clear breakdown of the metrics for each level:

### Level 1:
- **Accuracy**: 0.8129 - The model correctly predicts about 81.29% of the instances.
- **Recall**: 0.4621 - The model identifies approximately 46.21% of the actual positive instances.
- **Precision**: 0.1094 - Of the instances predicted as positive, only about 10.94% are actually positive.
- **F1-Score**: 0.1769 - The harmonic mean of precision and recall, indicating a moderate balance between the two.
- **MCC (Matthews Correlation Coefficient)**: 0.1532 - A measure of the model's quality considering true and false positives and negatives, which is low.
- **AUC (Area Under the ROC Curve)**: 0.7289 - Indicates that the model has a good capability to distinguish between classes.

### Level 2:
- **Accuracy**: 0.7821 - The model's overall prediction accuracy is about 78.21%.
- **Recall**: 0.6471 - It captures approximately 64.71% of the positive instances.
- **Precision**: 0.1220 - About 12.20% of the predicted positives are true positives.
- **F1-Score**: 0.2053 - This score indicates a better balance between precision and recall than Level 1 but is still low.
- **MCC**: 0.2108 - A low but better correlation coefficient compared to Level 1, suggesting some predictive ability.
- **AUC**: 0.7893 - Indicates improved ability to distinguish classes over Level 1.

### Level 3:
- **Accuracy**: 0.7658 - The model correctly classifies about 76.58% of instances.
- **Recall**: 0.6241 - About 62.41% of positive instances are correctly identified.
- **Precision**: 0.1108 - Only around 11.08% of predicted positives are actual positives.
- **F1-Score**: 0.1882 - Shows some balance but remains low.
- **MCC**: 0.1880 - Reflects a low correlation ability in predicting outcomes.
- **AUC**: 0.7770 - Indicates decent performance in distinguishing between classes, similar to Level 2.

### General Notes:

- Metric trends show that while accuracy and recall generally improve from Level 1 to Level 2, precision remains low across all levels, indicating challenges in effectively classifying positive instances.


# v7
- Preprocess models  
- Split the dataset into training and testing (20%)  
- Logistic regression and XGBoost perform well, while TabNet has poor accuracy.

# v8
- Preprocess models
- Split the dataset into training, testing, and validation sets
- Evaluate models
Final Comparative Analysis Results:


| Model               | Accuracy | Precision | Recall | F1 Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression  | 0.9681   | 0.9839    | 0.9681 | 0.9747   |
| XGBoost             | 0.9952   | 0.9951    | 0.9952 | 0.9951   |
| TabNet              | 0.9897   | 0.9919    | 0.9897 | 0.9901   |
| Random Forest       | 0.9959   | 0.9959    | 0.9959 | 0.9958   |
| LightGBM           | 0.9953   | 0.9952    | 0.9953 | 0.9952   |



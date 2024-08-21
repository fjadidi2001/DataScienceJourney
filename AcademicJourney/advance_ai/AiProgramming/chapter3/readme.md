> AI covers a broad area, and one of the most important aspects of AI is machine learning.

<br>


What is Machine Learning?
<br>

    - Machine learning (ML) is basically a set of mathematical algorithms.
    - Ml is an important subset of AI
    - it is the science that aims to teach computers, or machines, to learn from data and to analyze data automatically, without human intervention.
    - It includes a set of mathematical algorithms that can make a decision or, more accurately, predict the results for a given set of data.

<br>

Four different categories of ML:

    1. Supervised Learning
        - trained with labeled data
        - algorithms continuously adjust the parameters of models until the error calculated between the output and the desired output for a given input is minimized
        - used in classification and regression
                - classification: identify, for a given input sample, which class belongs to
                    - most popular algorithms: support vector machines, naive Bayes, linear discriminant analysis, decision trees, k-­nearest neighbor algorithm, neural networks

                - regression: the given data, fit the data with a model to get the best-­fit parameters
                    - linear regression, logistic regression, and polynomial regression.
    2. Unsupervised Learning
        - fed with unlabeled data
        - algorithms will study the data and divide it into groups according to features
        - used for clustering and association
            - clustering: dividing the data into groups
                - K-means clustering
            - association: means to discover rules that describe the majority portion of the data.
                - Apriori algorithm
    3. Semi-Supervised Learning
        - both labeled data and unlabeled data are used
        - The basic procedure is to group the data into different clusters using an unsupervised learning algorithm
        - then using the existing labeled data to label the rest of the unlabeled data.
        - most popular alghorithem: self-­training, generative methods, mixture models, and graph-­based methods.
        - can typically be used in speech analysis, internet content classification, and protein sequence classification.
    4. Reinforcement learning
        - algorithms learn to find, through trial and error, which actions can yield the maximum cumulative reward
        - used in robotics, video gaming, and navigation


<br>

### commonly terminologies
    1. Class: The categories of the data
    2. Features: The measurements
    3. Samples: The data points
    4. Parameters: The variables of the model


<br>

# SVM
    - Support vector machine (SVM) is the best-­known supervised learning algorithm.
    - can be used for both classification and regression problems
    - robust prediction methods, based on the statistical learning framework.
    

# PCA
    - Principal component analysis
    - maximizes the variance of the projected points
    - minimizing the sum-of-squares of the projection errors
    - used for : dimensionality reduction, lossy data compression, feature extraction, and data visualization

# Multi-layer perceptron



# Random forest classifier

# Decision Trees

# Regressions
Regression means
fitting the data with a mathematical model using a technique called least squares
fitting.
<br>

regressions
1. linear => fit the data with a straight line => f(x) = ax + b => a is the slope, and b is the intercept
    calculated the sum of the squares of the errors ( ei ), calculate the
    distances between the data points and the straight line, and adjust the slope
    (a) and the intercept (b) of the straight line, until we have reached the smallest
    sum of the squares (x^2), which is why it’s called least squares
2. non-linear => For nonlinear regression, we fit the data with more complicated mathematical
models, such as exponentials and polynomials
    - logestic regression => for the data this is dichotomous => based on a set of independent variables
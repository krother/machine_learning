## Machine Learning with Scikit-Learn

Initialize the following dataset:

    from sklearn.datasets import load_wine
    import pandas as pd

    data = load_wine()
    df = pd.DataFrame(data['data'], columns=data['feature_names'])
    X = df.values
    y = data['target']

Complete the following tasks:

    # 1. Split the data into a training and test portion

    # 2. Scale the data

    # 3. Train a Linear SVC

    # 4. Inspect the training accuracy

    # 5. Determine accuracies from a 5-fold cross-validation

    # 6. Inspect the test accuracy

    # 7. Get a prediction for the test set

    # 8. Print a confusion matrix for the test set

    # 9. Calculate confidence scores for each prediction

    # 10. Plot the confidence scores as a histogram



from sklearn.metrics import accuracy_score, mean_squared_error

def evaluate_classification(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def evaluate_regression(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)
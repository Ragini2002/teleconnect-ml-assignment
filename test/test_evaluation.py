import numpy as np
from src.evaluation import evaluate_classification, evaluate_regression

# -----------------------------

# Test Classification Evaluation

# -----------------------------

def test_classification_accuracy():
y_true = np.array([1, 0, 1, 1, 0])
y_pred = np.array([1, 0, 1, 0, 0])

```
acc = evaluate_classification(y_true, y_pred)

assert 0 <= acc <= 1, "Accuracy should be between 0 and 1"
```

# -----------------------------

# Test Perfect Classification

# -----------------------------

def test_perfect_classification():
y_true = np.array([1, 1, 0, 0])
y_pred = np.array([1, 1, 0, 0])

```
acc = evaluate_classification(y_true, y_pred)

assert acc == 1.0, "Accuracy should be 1.0 for perfect prediction"
```

# -----------------------------

# Test Regression Evaluation

# -----------------------------

def test_regression_mse():
y_true = np.array([10, 20, 30])
y_pred = np.array([12, 18, 33])

```
mse = evaluate_regression(y_true, y_pred)

assert mse >= 0, "MSE should be non-negative"
```

# -----------------------------

# Test Perfect Regression

# -----------------------------

def test_perfect_regression():
y_true = np.array([5, 10, 15])
y_pred = np.array([5, 10, 15])

```
mse = evaluate_regression(y_true, y_pred)

assert mse == 0.0, "MSE should be 0 for perfect prediction"
```

# -----------------------------

# Test Shape Mismatch (Optional)

# -----------------------------

def test_shape_mismatch():
y_true = np.array([1, 2, 3])
y_pred = np.array([1, 2])

```
try:
    evaluate_regression(y_true, y_pred)
except ValueError:
    assert True
else:
    assert False, "Should raise ValueError for mismatched shapes"
```

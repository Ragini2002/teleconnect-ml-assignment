# Initialize package

from .data_loader import load_data
from .preprocessing import preprocess_data
from .classifiers import train_classifier
from .regressors import train_regressor
from .evaluation import evaluate_classification, evaluate_regression
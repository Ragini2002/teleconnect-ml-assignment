import os
import joblib
import logging

# -----------------------------
# Create directories if not exist
# -----------------------------
def create_directory(path):
    os.makedirs(path, exist_ok=True)


# -----------------------------
# Save object (model, scaler, encoder)
# -----------------------------
def save_object(obj, filepath):
    joblib.dump(obj, filepath)


# -----------------------------
# Load object
# -----------------------------
def load_object(filepath):
    return joblib.load(filepath)


# -----------------------------
# Setup logging
# -----------------------------
def setup_logger(log_file="app.log"):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


# -----------------------------
# Print dataset summary
# -----------------------------
def data_summary(df):
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict()
    }
    return summary


# -----------------------------
# Split features & target
# -----------------------------
def split_features_target(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y
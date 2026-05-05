Regression Model Report

Overview

This report summarizes the performance of regression models used to predict the target variable. Multiple algorithms were trained and evaluated to identify the best-performing model.

Models Evaluated

Linear Regression
Decision Tree Regressor
Random Forest Regressor
K-Nearest Neighbors (KNN) Regressor

The following metrics were used:

Mean Absolute Error (MAE) → Measures average prediction error
Mean Squared Error (MSE) → Penalizes larger errors more
Root Mean Squared Error (RMSE) → Square root of MSE (interpretable scale)
R² Score (Coefficient of Determination) → Explains variance captured by model

Results Summary

Model	MAE	MSE	RMSE	R² Score
Linear Regression	4.21	28.50	5.34	0.78
Decision Tree Regressor	3.95	26.10	5.11	0.80
Random Forest Regressor	3.20	18.75	4.33	0.87
KNN Regressor	4.50	30.20	5.49	0.75

Random Forest Regressor achieved the best performance:

Lowest error (MAE, RMSE)
Highest R² score (0.87)
Better generalization on unseen data

Error Analysis

Linear Regression underperformed due to inability to capture non-linear relationships
Decision Tree showed moderate performance but prone to overfitting
KNN performance affected by feature scaling and noise
Random Forest reduced overfitting by averaging multiple trees
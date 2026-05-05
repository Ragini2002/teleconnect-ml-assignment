from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Example
    df = df.dropna()

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df.select_dtypes(include='number'))

    return df, scaler
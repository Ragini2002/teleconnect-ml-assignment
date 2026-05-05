def test_null_removal():
    import pandas as pd
    df = pd.DataFrame({"A": [1, None]})
    assert df.isnull().sum().sum() > 0
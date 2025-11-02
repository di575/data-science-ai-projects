import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    # Synthetic close prices
    n = 500
    rng = np.random.RandomState(0)
    trend = np.linspace(100, 150, n)
    noise = rng.randn(n)
    close = trend + noise

    df = pd.DataFrame({"close": close})
    df["lag1"] = df["close"].shift(1)
    df = df.dropna()

    X = df[["lag1"]].values
    y = df["close"].values
    model = LinearRegression().fit(X, y)
    print("Coef:", model.coef_, "Intercept:", model.intercept_)


if __name__ == "__main__":
    main()

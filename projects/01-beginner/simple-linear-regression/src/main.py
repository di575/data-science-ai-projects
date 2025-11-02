import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from joblib import dump
from pathlib import Path


def main():
    # Toy dataset (Boston alternatives due to deprecation)
    n = 300
    rng = np.random.RandomState(42)
    X = rng.rand(n, 1) * 10
    y = 3.5 * X[:, 0] + 7 + rng.randn(n) * 1.2

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_tr, y_tr)
    preds = model.predict(X_te)

    mae = mean_absolute_error(y_te, preds)
    r2 = r2_score(y_te, preds)

    out = Path("outputs")
    out.mkdir(exist_ok=True)
    dump(model, out / "linear_model.joblib")

    print({"MAE": mae, "R2": r2})


if __name__ == "__main__":
    main()

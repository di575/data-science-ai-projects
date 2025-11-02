import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


def main():
    n=500
    rng = np.random.RandomState(1)
    X = rng.rand(n, 5)
    y = (X[:,0]*0.6 + X[:,1]*0.3 + rng.rand(n)*0.2 > 0.8).astype(int)

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    clf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_tr, y_tr)
    proba = clf.predict_proba(X_te)[:,1]
    print("AUC:", roc_auc_score(y_te, proba))


if __name__ == "__main__":
    main()

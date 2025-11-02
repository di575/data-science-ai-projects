import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def main():
    data = pd.DataFrame({
        "text": ["I love this!", "This is terrible", "Amazing work", "So bad", "Great job"],
        "label": [1, 0, 1, 0, 1]
    })
    X_tr, X_te, y_tr, y_te = train_test_split(data["text"], data["label"], test_size=0.4, random_state=42)
    vec = TfidfVectorizer()
    Xtr = vec.fit_transform(X_tr)
    Xte = vec.transform(X_te)
    clf = LogisticRegression(max_iter=1000).fit(Xtr, y_tr)
    preds = clf.predict(Xte)
    print("F1:", f1_score(y_te, preds))


if __name__ == "__main__":
    main()

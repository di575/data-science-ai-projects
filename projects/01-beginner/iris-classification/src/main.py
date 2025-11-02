from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def main():
    data = load_iris()
    X, y = data.data, data.target

    pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe.fit(X_tr, y_tr)
    y_pred = pipe.predict(X_te)

    print(classification_report(y_te, y_pred))

    cm = confusion_matrix(y_te, y_pred)
    plt.figure(figsize=(4,3))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    out = Path("outputs"); out.mkdir(exist_ok=True)
    plt.savefig(out / "confusion_matrix.png", bbox_inches="tight")


if __name__ == "__main__":
    main()

import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Iris Classifier", layout="wide")
st.title("🌸 Iris Classification Dashboard")

data = load_iris()
X, y = data.data, data.target
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
pipe.fit(X_tr, y_tr)
y_pred = pipe.predict(X_te)

st.subheader("Classification Report")
st.text(classification_report(y_te, y_pred, target_names=data.target_names))

cm = confusion_matrix(y_te, y_pred)
fig, ax = plt.subplots(figsize=(4,3))
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", ax=ax)
ax.set_title("Confusion Matrix")
st.pyplot(fig)

st.subheader("Try a Prediction")
sepal_length = st.slider("Sepal length", 4.0, 8.0, 5.1, 0.1)
sepal_width  = st.slider("Sepal width",  2.0, 4.5, 3.5, 0.1)
petal_length = st.slider("Petal length", 1.0, 7.0, 1.4, 0.1)
petal_width  = st.slider("Petal width",  0.1, 2.5, 0.2, 0.1)

pred = pipe.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
st.success(f"Predicted: {data.target_names[pred]}")

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Tweet Sentiment", layout="centered")
st.title("💬 Sentiment Analysis (TF-IDF + LR)")

st.markdown("Paste some labeled tweets, train a quick baseline, and test.")

default = """I love this movie,1
This product is terrible,0
Amazing performance,1
So bad,0
Great job!,1
"""

csv = st.text_area("CSV (text,label)", value=default, height=150)
if st.button("Train"):
    from io import StringIO
    df = pd.read_csv(StringIO(csv), header=None, names=["text","label"])    
    X_tr, X_te, y_tr, y_te = train_test_split(df["text"], df["label"], test_size=0.4, random_state=42)
    vec = TfidfVectorizer()
    Xtr = vec.fit_transform(X_tr)
    Xte = vec.transform(X_te)
    clf = LogisticRegression(max_iter=1000).fit(Xtr, y_tr)
    acc = clf.score(Xte, y_te)
    st.success(f"Accuracy: {acc:.3f}")

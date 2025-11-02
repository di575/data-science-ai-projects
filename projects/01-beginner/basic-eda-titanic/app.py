import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from src.data_loader import TitanicDataLoader

st.set_page_config(page_title="Titanic EDA", layout="wide")
st.title("🚢 Titanic EDA Dashboard")

loader = TitanicDataLoader()
df = loader.load_data()

# Sidebar filters
st.sidebar.header("Filters")
cls = st.sidebar.multiselect("Pclass", options=sorted(df["Pclass"].unique()), default=list(sorted(df["Pclass"].unique())))
sex = st.sidebar.multiselect("Sex", options=df["Sex"].cat.categories.tolist(), default=df["Sex"].cat.categories.tolist())
emb = st.sidebar.multiselect("Embarked", options=df["Embarked"].cat.categories.dropna().tolist(), default=df["Embarked"].cat.categories.dropna().tolist())

mask = df["Pclass"].isin(cls) & df["Sex"].isin(sex)
if "Embarked" in df.columns:
    mask &= df["Embarked"].isin(emb)

fdf = df[mask].copy()

st.subheader("Dataset Preview")
st.dataframe(fdf.head(50))

c1, c2 = st.columns(2)
with c1:
    st.markdown("**Survival by Class**")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(data=fdf, x="Pclass", y="Survived", estimator=sum, errorbar=None, ax=ax)
    st.pyplot(fig)
with c2:
    st.markdown("**Age Distribution**")
    if "Age" in fdf.columns:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(fdf["Age"].dropna(), kde=True, ax=ax)
        st.pyplot(fig)

st.subheader("Correlation (numeric)")
num = fdf.select_dtypes(include=["number"]).corr()
st.dataframe(num.style.background_gradient(cmap="Blues"), use_container_width=True)

st.download_button("Download filtered CSV", data=fdf.to_csv(index=False), file_name="titanic_filtered.csv", mime="text/csv")

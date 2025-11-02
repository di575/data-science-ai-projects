import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


class TitanicVisualizer:
    def __init__(self, out_dir="reports/figures"):
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)

    def create_all_plots(self, df):
        plt.figure(figsize=(6,4))
        sns.countplot(x="Survived", data=df)
        plt.title("Survival Count")
        plt.savefig(self.out_dir / "survival_count.png", bbox_inches="tight")
        plt.close()

        if "Age" in df.columns:
            plt.figure(figsize=(6,4))
            sns.histplot(df["Age"].dropna(), kde=True)
            plt.title("Age Distribution")
            plt.savefig(self.out_dir / "age_dist.png", bbox_inches="tight")
            plt.close()

from src.data_loader import TitanicDataLoader
from src.eda_functions import EDAnalyzer
from src.visualizations import TitanicVisualizer


def main():
    loader = TitanicDataLoader()
    df = loader.load_data()

    eda = EDAnalyzer()
    viz = TitanicVisualizer()

    eda.basic_overview(df)
    eda.missing_value_analysis(df)
    viz.create_all_plots(df)

    print("Done. See reports/figures/")


if __name__ == "__main__":
    main()

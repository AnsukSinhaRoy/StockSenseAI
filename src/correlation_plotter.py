import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CorrelationPlotter:
    def plot(self, df: pd.DataFrame):
        """
        Receives a DataFrame of percentage changes for any number of stocks
        and plots a correlation heatmap.
        """
        if df.shape[1] < 2:
            raise ValueError("Input DataFrame must have at least two columns.")

        correlation_matrix = df.corr()

        plt.figure(figsize=(10, 8))  # Scales better for many stocks
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            linewidths=0.5,
            square=True,
            cbar_kws={"shrink": 0.75}
        )
        plt.title("Correlation Heatmap")
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()

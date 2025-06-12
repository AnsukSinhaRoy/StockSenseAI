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

    def compare_correlations(df: pd.DataFrame):
        """
        Receives a DataFrame of percentage changes for any number of stocks
        and prints two tables: one for positive and one for negative correlations.
        """
        if df.shape[1] < 2:
            raise ValueError("Input DataFrame must have at least two columns.")

        # Compute correlation matrix
        corr_matrix = df.corr()

        # Unstack to get pairs
        corr_unstacked = corr_matrix.unstack()

        # Remove self-correlations
        corr_unstacked = corr_unstacked[corr_unstacked.index.get_level_values(0) != corr_unstacked.index.get_level_values(1)]

        # Drop duplicate pairs (keep only one of (A,B) and (B,A))
        corr_unstacked = corr_unstacked.groupby(
            lambda x: tuple(sorted(x))
        ).mean()

        # Split into positive and negative
        positive_corrs = corr_unstacked[corr_unstacked > 0].sort_values(ascending=False)
        negative_corrs = corr_unstacked[corr_unstacked < 0].sort_values()

        # Display results
        print("\nTop Positive Correlations:")
        print(positive_corrs.to_frame("Correlation").head(20))

        print("\nTop Negative Correlations:")
        print(negative_corrs.to_frame("Correlation").head(20))

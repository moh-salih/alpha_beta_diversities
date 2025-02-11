import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bootstrap

# Function to compute rarefaction curve
def rarefaction_curve(sample, depths):
    """
    Simulates subsampling of reads at different depths and computes taxa richness.
    """
    richness = []
    total_reads = sample.sum()
    taxa = np.array(sample.index)

    print("Number of depths", len(depths))
    for depth in depths:
        if depth > total_reads:
            richness.append(np.nan)  # Avoid extrapolation
            continue

        subsample = np.random.choice(taxa, size=depth, replace=True, p=sample / total_reads)
        richness.append(len(set(subsample)))  # Count unique taxa

    return richness


def plot_rarefaction_curve(sample_by_feature):
    # Define rarefaction depths
    max_depth = sample_by_feature.max().max()
    depths = np.linspace(1, max_depth, num=100, dtype=int)

    # Compute rarefaction curves for both samples
    np.random.seed(42)  # For reproducibility
    adult_rarefaction = rarefaction_curve(sample_by_feature['Adult'], depths)
    larva_rarefaction = rarefaction_curve(sample_by_feature['Larva'], depths)

    # Plot rarefaction curves
    plt.figure(figsize=(8, 6))
    plt.plot(depths, adult_rarefaction, label='Adult', marker='o')
    plt.plot(depths, larva_rarefaction, label='Larva', marker='s')

    plt.xlabel("Sequencing Depth (Reads)")
    plt.ylabel("Observed Taxa (Richness)")
    plt.title("Rarefaction Curve")
    plt.legend()
    plt.grid()
    plt.show()
    
    

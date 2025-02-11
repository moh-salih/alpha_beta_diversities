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
    depths = np.linspace(100, max_depth, num=100, dtype=int)

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
    
    
    
def cumulative_richness(sample):
        """
        Computes the cumulative number of unique taxa as sequencing depth increases.
        """
        richness = []
        seen_taxa = set()

        for read_count, taxon in enumerate(sample.index):
            seen_taxa.add(taxon)
            richness.append(len(seen_taxa))

        return richness

    # Compute cumulative richness for each sample


def fire_it_like_its_brother(sample_by_feature):
    adult_cumulative = cumulative_richness(sample_by_feature['Adult'])
    larva_cumulative = cumulative_richness(sample_by_feature['Larva'])

    # Plot cumulative richness
    plt.figure(figsize=(8, 6))
    plt.plot(range(len(adult_cumulative)), adult_cumulative, label='Adult', marker='o')
    plt.plot(range(len(larva_cumulative)), larva_cumulative, label='Larva', marker='s')

    plt.xlabel("Sequencing Depth (Reads)")
    plt.ylabel("Observed Taxa (Richness)")
    plt.title("Cumulative Richness Curve")
    plt.legend()
    plt.grid()
    plt.show()

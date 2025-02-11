import pandas as pd


# Load the data, *without* setting the index yet
adult = pd.read_csv(r"adults_transicripts_report_MO_minimum-hit-groups_5_CS_003.txt", sep='\t', header=None, skipinitialspace=True)
larva = pd.read_csv(r"larva_transicripts_report_MO_minimum-hit-groups_5_CS_003.txt", sep='\t', header=None, skipinitialspace=True)

# Assign column names (same as before)
adult.columns = [
    "Relative_Abundance", "Reads", "Unique_Reads", "Total_Reads_in_Sample",
    "Total_Reads_in_Database", "Taxonomic_Level", "TaxID", "Taxonomy"
]
larva.columns = [
    "Relative_Abundance", "Reads", "Unique_Reads", "Total_Reads_in_Sample",
    "Total_Reads_in_Database", "Taxonomic_Level", "TaxID", "Taxonomy"
]

# --- Creating the Sample-by-Feature Table ---

# Set the 'Taxonomy' as index *after* assigning column names
adult = adult.set_index('Taxonomy')
larva = larva.set_index('Taxonomy')

# Create the DataFrames (no need to transpose if you set index after)
adult_reads_df = pd.DataFrame({'Adult': adult['Reads']})
larva_reads_df = pd.DataFrame({'Larva': larva['Reads']})

# Combine the DataFrames
sample_by_feature_table = pd.concat([adult_reads_df, larva_reads_df], axis=1) # axis=1 to concatenate columns

# Fill NaN with 0 (important if some taxa are missing in one sample)
sample_by_feature = sample_by_feature_table.fillna(0)


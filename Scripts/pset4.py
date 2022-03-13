# import metaData file in to a data frame
import pandas as pd 
meta = pd.read_csv('../Data/metaData.csv')

# filter the metadat to include only reads from donors with ra
# first select out all donors 
filtered = meta[meta['sampleID'].str.contains('donor')]

# then select out donors with ra 
filtered = filtered[filtered['status'].isin(['ra'])]

# count the distribution of cell types 
celltype_distribution = dict(filtered['cell_subtype'].value_counts())
#print((celltype_distribution))

# plot cell type distribution 
import matplotlib.pyplot as plt 
x = list(celltype_distribution.keys())
#plt.bar(range(len(x)), celltype_distribution.values(),tick_label=x)
plt.bar(x, celltype_distribution.values())
plt.xticks(rotation = -80)
plt.ylabel('Count')
plt.title('Cell Type Distributions in RA Donors')
plt.savefig('../Figures/pset4_Figure.png')

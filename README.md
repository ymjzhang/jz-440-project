# jz-440-project
Overview
This repository includes an RNAseq dataset from Synovial fibroblast found at https://singlecell.broadinstitute.org/single_cell/study/SCP469/synovial-fibroblast-positional-identity-controlled-by-inductive-notch-signaling-underlies-pathologic-damage-in-inflammatory-arthritis#study-summary
The script generates a figure showding the cell type distribution in this dataset 

Data
The dataset is from an RNAseq experiment as linked above. The data that is used to generate the figure is the metaData.csv file. 
The metaData file include informations such as sampleID, status, label, cell_type, cell_subtype, nUMI, nGene, percent_mito, and pseudotime


Folder structure 
There are three folders, Data, Figures, and Scripts
Data include the dataset that the scritps can access 
Figures include outputs from the scripts 
Scripts fold includes codes that can be executed 

Installation
Run the script "pset4.py" under the folder Scripts 
package versions:
python 3.8.8
matplotlib 3.5
pandas 1.4.1

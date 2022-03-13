# jz-440-project
Overview
This repository includes an RNAseq dataset from Synovial fibroblasts of patients with rheumatoid arthritis (RA) and Osteoarthritis (OA).
The script generates a figure showding the cell type distribution in RA patient donors. 

Data
The dataset is from an RNAseq experiment at Broad Institute Database: https://singlecell.broadinstitute.org/single_cell/study/SCP469/synovial-fibroblast-positional-identity-controlled-by-inductive-notch-signaling-underlies-pathologic-damage-in-inflammatory-arthritis#study-summary. The data that is used to generate the figure is the metaData.csv file. 
The metaData file include informations such as sampleID, status, label, cell_type, cell_subtype, nUMI, nGene, percent_mito, and pseudotime


Folder structure 
There are three folders, Data, Figures, and Scripts
Data folder includes the dataset that the scritps can access 
Figures folder include outputs from the scripts 
Scripts folder includes codes that can be executed 

Installation
Run the script "pset4.py" under the folder Scripts 
package versions:
python 3.8.8
matplotlib 3.5
pandas 1.4.1

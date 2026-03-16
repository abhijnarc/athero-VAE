import pandas as pd
import os

os.makedirs("./data/processed", exist_ok=True)

file_path = "./data/raw/GSE56046_methylome_normalized.txt.gz"

meth = pd.read_csv(file_path, sep="\t", index_col=0)

print("Matrix shape:", meth.shape)

meth.to_csv("./data/processed/methylation_matrix.csv")
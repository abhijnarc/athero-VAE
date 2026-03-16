import pandas as pd

expr = pd.read_csv("data/processed/expression_matrix.csv", index_col=0)
meth = pd.read_csv("data/processed/methylation_matrix.csv", index_col=0)

print("Expression:", expr.shape)
print("Methylation:", meth.shape)
import GEOparse
import os

DATA_DIR = "../data/raw"

os.makedirs(DATA_DIR, exist_ok=True)

print("Downloading GSE56045 (expression)")
gse_expr = GEOparse.get_GEO("GSE56045", destdir=DATA_DIR)

print("Downloading GSE56046 (methylation)")
gse_meth = GEOparse.get_GEO("GSE56046", destdir=DATA_DIR)

print("Download complete")
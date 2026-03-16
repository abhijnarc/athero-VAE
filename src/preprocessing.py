import GEOparse

gse = GEOparse.get_GEO("GSE56046", destdir="../data/raw")

print(gse.metadata)
print(gse.metadata["supplementary_file"])
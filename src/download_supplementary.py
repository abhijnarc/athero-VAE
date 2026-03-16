import GEOparse

gse = GEOparse.get_GEO("GSE56046", destdir="data/raw")

print("Downloading supplementary files...")
gse.download_supplementary_files()
#!/usr/bin/env python
import pandas as pd, sys
table = pd.read_csv(sys.argv[1], sep="\t", index_col=0)
meta = pd.read_csv(sys.argv[2], sep="\t", index_col=0)
merged = table.T.join(meta)
merged.to_csv(sys.argv[3], sep="\t")

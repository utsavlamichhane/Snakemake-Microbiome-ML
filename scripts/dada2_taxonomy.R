#!/usr/bin/env Rscript
library(dada2); library(phyloseq)
args <- commandArgs(TRUE)
path <- args[1]; out_tab <- args[2]; out_tax <- args[3]
fnFs <- sort(list.files(path, pattern="_R1_", full.names=TRUE))
fnRs <- sort(list.files(path, pattern="_R2_", full.names=TRUE))
# Filter
filtFs <- file.path(path, "filtered", basename(fnFs))
filterAndTrim(fnFs, filtFs, fnRs, filtRs)
# Learn & denoise
# ...
# Make table & assign taxonomy
seqtab <- makeSequenceTable(dadaFs)
tax <- assignTaxonomy(seqtab, "/path/to/silva_db.fasta.gz")
write.table(seqtab, out_tab, sep="\t", quote=FALSE)
write.table(tax, out_tax, sep="\t", quote=FALSE)

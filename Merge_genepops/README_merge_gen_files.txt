NOTE: Make sure the POS indexing is correct/matches between GEN files

1) perl genepop_print_snp_names_1_per_line.pl *RAW_GEN* > standard_GEN
		do this for all GEN files, I call this version the standard_GEN

2)subset_genepop_by_SNPs.pl *whitelist* *standard_GEN* > whitelisted.GEN
		use same whitelist for all gen files to merge
3)SNPs should be in same format between files, copy and paste into one merged file
#Author: Matt Bootsma
#last edit: 3/14/2019
#Notes:
    #This script is designed to subset sequences from a RAW catalog.fa file for use in geneious
    #When imported to geneious it will provide the sequence data
        #RAW data is only tested with a catalog.fa derived from STACKS_2
    #Script requires a whitelist of the #CHROM ID's that you wish to retain
        #Whitelist should have one value per locus of interest.
        #Values should be listed horizontally in first row of .csv
        #Values should be concatenated like so: cat(">","ID#")
        #IMPORTANT: fill first and last cell of .csv whitelist with "XXXX"
            # or some other string that is not present in data.
            # if you don't the script will fail to subset the first and last ID in whitelist
########################################################################################

import os
os.getcwd()
#navigate to the RAW data, whitelist should be in this file too
os.chdir("I:\WAE_RAD_Data\pre_IAGLR\STACKS_publish\Scripts\Python\geneious_data")
#read RAW data
RAW_fa_file = open("catalog.fa", "r")
RAW_fa_array = RAW_fa_file.readlines()
RAW_fa_file.close()
#read whitelist data
WHITELIST_file = open("subset_catalog_genomic_whitelist.csv", "r")
WHITELIST_array = WHITELIST_file.readlines()
WHITELIST_file.close()
#open the output file
out_file = open("1710_genomic_loci.fa", "w")

#iterate through lines in RAW data
iter_obj = iter(RAW_fa_array)
flag = "FAIL"

WHITELIST_list = WHITELIST_array[0].split(",")
#i = one line
for i in iter_obj:
        #splitting lines by whitespace iteratively
        split_RAW = i.rstrip().split(" ")
        #j captures the first value, either the CHROM ID or the whole sequence
        j = split_RAW[0]
        #whitelist only matches on the CHROM ID,
        # flag == "PASS" is only true if the CHROM ID matches
        if flag == "PASS":
            #write the sequence
            out_file.write(i)
            #toggle the flag off
            flag = "FAIL"

        #Test if the sequence number (which corresponds to CHROM_ID)
        #of a row is present in the whitelist
        if j in WHITELIST_list:
            out_file.write(i)
            flag = "PASS"

out_file.close()
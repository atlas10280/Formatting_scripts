#Author: Matt Bootsma
#last edit: 6/29/2020○
#Notes:
    #This script is designed to subset sequences from a RAW catalog.fa file for use in geneious or alignments
        
    #Only tested with raw catalog.fa data derived from STACKS_2, 
    #if your locus name in the .fa file has been altered, make sure you address this in lines 30-34
            
    #Script requires a whitelist of the #CHROM ID's that you wish to retain
        #Whitelist should have one value per locus of interest.
        #Values should be a single column 
########################################################################################

import os
os.getcwd()
#navigate to the RAW data, whitelist should be in this file too
os.chdir("D:\Great_Lakes_WAE\Genotypes\obtain_haps\\alignments")

#open the output file
out_file = open("loci_for_allignment_Great_Lakes_WAE.fa", "w")

#read whitelist data
WHITELIST_file = open("locus_whitelist_Great_Lakes_WAE.csv", "r")
WHITELIST_array = WHITELIST_file.readlines()
WHITELIST_file.close()

# compile elements of whitelist into a true list
WHITELIST_list = list()
for i in WHITELIST_array:
    # if you have real locus IDs that are just the CHROM number without aftermarket strings concatenated use the line below
    i = i.rstrip("\n")
    i = ">" + i
    #i = int(i)
    WHITELIST_list.append(i)

#read RAW data
RAW_fa_file = open("WA_mac3ind90mm20.maf.5kb.100k_baits.fa", "r")
RAW_fa_array = RAW_fa_file.readlines()
RAW_fa_file.close()

#iterate through lines in RAW data
iter_obj = iter(RAW_fa_array)
flag = "FAIL"


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
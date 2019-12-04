#Author: Matt Bootsma
#last edit: 3/14/2019
#Notes:
    #This script is designed to subset a RAW SNPs vcf file for use in geneious
    #When imported to geneious it will provide SNP annotation
        #RAW data is only tested with a vcf derived from STACKS_2
    #Script requires a whitelist of the #CHROM ID's that you wish to retain
        #Whitelist should have one value per locus of interest.
        #Values should be listed horizontally in first row of .csv
        #This was designed to pull haplotype data so all CHROM ID's that match will be subset out
        # IMPORTANT: fill first and last cell of .csv whitelist with "XXXX"
            # or some other string that is not present in data.
            # if you don't the script will fail to subset the first and last ID in whitelist
########################################################################################

import os
import re
os.getcwd()
#navigate to the RAW data, whitelist should be in this file too
os.chdir("I:\WAE_RAD_Data\STACKS_publish\Scripts\Python\geneious_data")
#read RAW data
RAW_vcf_file = open("v4_populations.snps.vcf", "r")
RAW_vcf_array = RAW_vcf_file.readlines()
RAW_vcf_file.close()
#read whitelist data
WHITELIST_file = open("whitelist_vcf2geneious_annotation_v3_HE.csv", "r")
WHITELIST_array = WHITELIST_file.readlines()
WHITELIST_file.close()
#open the output file
out_file = open("annotation_subset_4geneious_v3_HE.vcf", "w")

WHITELIST_list = WHITELIST_array[0].split(",")
#i = one line
for i in RAW_vcf_array:
    #recognize the header lines, write useful metadata
    if i.startswith("##fileformat"):
        out_file.write(i)
    elif i.startswith("##fileDate"):
        out_file.write(i)
    elif i.startswith("#CHROM"):
        #we know the data headers, so we can hardcode here
         out_file.write("#CHROM" + "\t" + "POS" + "\t" + "ID" + "\t" + "REF" + "\t" + "ALT" + "\t" + "QUAL" + "\t" + "FILTER" + "\t" + "INFO" + "\t" + "FORMAT" + "\n")
        # at this point we should have header line
    else:
        split_RAW = i.rstrip().split("\t")
        #j captures the first value of a row, i.e. CHROM ID
        j = split_RAW[0]
        #the following code will test if the CHROM ID of a row is present in the whitelist
        if j in WHITELIST_list:
            for k in range(9):
                out_file.write(split_RAW[k] + "\t")
            out_file.write("\n")

out_file.close()
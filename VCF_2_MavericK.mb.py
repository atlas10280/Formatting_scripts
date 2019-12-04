# -*- coding: utf-8 -*-

"""
Created on Wed Apr 10 10:01:31 2019
@author: mboot217

This script takes vcf data and formats it to be compatible with MavericK 

NOTE: Input data is NOT a raw VCF, rather it is a transposed VCF. I performed this step in R using >t(data) 
    and writing out the transposed data.

This script does NOT produce the optional metadata that can be included in MavericK, i.e., pop or ploidy
    if required I would suggest using R, but as of 4/10/2019 I have not tested this step.
"""

import os
import re
os.getcwd()
os.chdir("I:/WAE_RAD_Data/STACKS_publish/phase2-pop_Gen")
# open vcf file read all lines into an array, close file
raw_tsv_file = open("transposed_snps.tsv", "r")
raw_tsv_array = raw_tsv_file.readlines()
raw_tsv_file.close()

# open file you are going to write new results to
out_file = open("v6_SNPs_MavericK.txt", "w")
r = 1
# for each line in vcf file
a = str(0)
b = str(1)
for i in raw_tsv_array:
    # this is trying to recognize the header line
    if i.startswith("SNP_ID"):

        # hard code column header for first column
            out_file.write("sampleID" + "\t")
            
            #split elements in row (allele calls)
            header_line = i.rstrip().split("\t")
            
            # write individual names
            z = 0
            for j in header_line:
                                
                if z > 0 and z % 2 == 1:
                    out_file.write(j + "\t")  
                z = z + 1

            out_file.write("\n")
            # at this point we should have header line

    #Go to individual's genotypes
    elif "SNP_ID" not in i:
        
        #split indiviual's genotypes into elements
        split_SNP_line = i.rstrip().split("\t")
        #store the individual name for writing on 2 rows
        IND_name = split_SNP_line[0]
        
        #z serves as loop control, allowing us to print every other allele (i.e. allele_A or allele_B) on a single line
        z = 0
        #loop through an individual's alleles, first writing a row with allele_A for each SNP
        out_file.write(IND_name + ".1" + "\t")
        for k in split_SNP_line:
            if z > 0 and z % 2 != 0:
                out_file.write(k + "\t")
            z = z + 1
        out_file.write("\n")
        #then writing a second row with allele_B for each SNP at the same individual
        out_file.write(IND_name + ".2" + "\t")
        
        #reset z to control loop for allele_B writing
        z = 0    
        for j in split_SNP_line:
            if z > 0 and z % 2 == 0:
                out_file.write(j + "\t")
            z = z + 1
        #move to next individual
        out_file.write("\n")

out_file.close()  # script parse vcf file get alleles per individual
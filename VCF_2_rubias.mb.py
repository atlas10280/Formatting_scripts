# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:38:03 2019

@author: mboot217
"""

# script parse vcf file get alleles per individual
import os
import re
os.getcwd()
os.chdir("I:\WAE_RAD_Data\STACKS_publish\Populations\SNP")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("v4_populations.snps.vcf", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()

# open file you are going to write new results to
out_file = open("test2.vcf", "w")
r = 1
# for each line in vcf file
a = str(0)
b = str(1)
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you want
            out_file.write("SNP_ID" + "\t")
            header_line = i.rstrip().split("\t")
            # write individual names
            z = 0
            for j in header_line:
                z = z + 1                
                if z > 9 and z < len(header_line)+1:
                    out_file.write(j + "\t")                 
                #else: out_file.write(j)

            out_file.write("\n")
            # at this point we should have header line

    # use the if not # to go to the data
    elif "#" not in i:
        #write SNP name (allele 1)
        split_SNP_line = i.rstrip().split("\t")
        SNP_name = split_SNP_line[0]+"_"+split_SNP_line[1]
        #print SNP_name
        out_file.write(SNP_name + "\t")
        allele0 = split_SNP_line[3]
        allele1 = split_SNP_line[4]
         

        # iterates through individual SNP calls
        z = 0
        for j in split_SNP_line:
            #print j

            z = z + 1
            if z > 9 and z < len(header_line)+1:
                # split the genotype cell
                gen_data = j.split(":")
                #print gen_data[0]
                genotype = gen_data[0]
                #print genotype
                #the genotype call #/# has a " character attached, this next line removes the "
                genotype = re.sub('\"','',genotype)
                allele_data = genotype.split("/")
                X = allele_data[0]
                
                #print genotype
                #write out the first genotype call (allele character)

                if  X == a:
                  out_file.write(allele0 + "\t")
                elif X == b:
                  out_file.write(allele1 + "\t")
                else:
                  out_file.write("." + "\t")
        
        out_file.write("\n")

        out_file.write(SNP_name+".1" + "\t")
        z = 0
        for j in split_SNP_line:
            #print j

            z = z + 1
            if z > 9 and z < len(header_line)+1:
                # split the genotype cell
                gen_data = j.split(":")
          #      #print gen_data[0]
                genotype = gen_data[0]#.split("/")
                #print genotype
                #the genotype call #/# has a " character attached, this next line removes the "
                genotype = re.sub('\"','',genotype)
                allele_data = genotype.split("/")
                X = allele_data[1]
                #print genotype
                #write out the first genotype call
                if  X == a:
                  out_file.write(allele0 + "\t")
                elif X == b:
                  out_file.write(allele1 + "\t")
                else:
                  out_file.write("." + "\t")
                  
                
        out_file.write("\n")
        

out_file.close()  # script parse vcf file get alleles per individual
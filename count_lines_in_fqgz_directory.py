# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 07:09:22 2020

@author: mbootsma
"""

# script parse haps.vcf file get alleles per individual
# script parse vcf file get alleles per individual
import sys
import os
import gzip
#navigate to working directory
os.getcwd()
os.chdir("D:\\GTseq_publish_data\\RADseq\\Demultiplexed_reads\\true_SRA_upload_reads\\ftp_upload_batch2")
# open an output file and give it a header line
out_file = open("retained_reads_summary_1710_ftp_upload_batch2.csv", "w")
out_file.write("file_ID" + "," + "n_sequences" + "\n")



#read in the whitelist of fqgz file names to count sequences in
whitelist_file = open("fqgz_file_names_ftp_upload_batch2.txt", "r")
#loop through the files listed and count sequences for each, writing results as we go
for i in whitelist_file:
    print(i)
    #open file i
    fileObj = gzip.open(i.rstrip(), "rt")
    #count lines in file
    linecnt = 0
    for line in fileObj:

        linecnt += 1
    n_sequences = linecnt/4 #one retained read is composed of 4 lines
    out_file.write(i.rstrip() + "," + str(n_sequences) + "\n")
    fileObj = "NA"
    
out_file.close()

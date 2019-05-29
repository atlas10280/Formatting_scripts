#Note: this will take a 3 digit coded .gen file and turn it into a 2 digit coded .gen
#useful for arlequin and other stuff
# script: 
import os
import re
os.getcwd()
os.chdir("I:\WAE_RAD_Data\BARCODE_REPAIR_data\SNPs")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("v6_bcrepair_snps.gen", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()

# open file you are going to write new results to
out_file = open("v6_bcrepair_snps_code2.gen", "w")

# for each line in genepop file
for i in raw_vcf_array:
    if "," not in i:
        out_file.write(i)
    # this is trying to find population breaks
    #if i.startswith("Pop"):

        # hard code Population break
            #out_file.write("Pop" + "\n")
            
    # use the if not in to go to the data
    elif "," in i:
        #write individual ID
        split_SNP_line = i.rstrip().split()
        out_file.write(split_SNP_line[0] + "\t"+",""\t")
        
        L = len(split_SNP_line)
        L = int(L)
        
        #loop through the data following the ID, first genotype is at index 2
        for j in range(2, L, 1):
            #print j
            obj = split_SNP_line[j]
#This logic, while probably excessive and accounting for unreal genotypes
#is designed to account for all potential combinations. This was easier than 
#using my brain case to pick and choose what logic tests to include
            if obj == "000000":
                out_file.write("0000" + "\t")
            elif obj == "100100":
                out_file.write("0101" + "\t")
            elif obj == "100110":
                out_file.write("0102" + "\t")
            elif obj == "110100":
                out_file.write("0102" + "\t")
            elif obj == "100120": 
                out_file.write("0103" + "\t")
            elif obj == "120100":
                out_file.write("0103" + "\t")
            elif obj == "100130":
                out_file.write("0104" + "\t")
            elif obj == "130100":
                out_file.write("0104" + "\t")
            elif obj == "110110":
                out_file.write("0202" + "\t")
            elif obj == "110120":
                out_file.write("0203" + "\t")
            elif obj == "120110":
                out_file.write("0203" + "\t")
            elif obj == "110130":
                out_file.write("0204" + "\t")
            elif obj == "130110":
                out_file.write("0204" + "\t")
            elif obj == "120120":
                out_file.write("0303" + "\t")
            elif obj == "120130":
                out_file.write("0304" + "\t")
            elif obj == "130120":
                out_file.write("0304" + "\t")
            elif obj == "130130":
                out_file.write("0404" + "\t")

        out_file.write("\n")
        
        

out_file.close()  # script parse vcf file get alleles per individual

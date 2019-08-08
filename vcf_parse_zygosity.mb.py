# script turns a vcf from stacks 2 into single digit codes for zygosity of each genotype
#last edit: 8/1/2019
#author: Matt Bootsma
import os

os.getcwd()
os.chdir("I:/WAE_RAD_Data/novoseq2/STACKS/Filter_steps/genomics")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("v6_novoseq2_snps_genomic.recode.vcf", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()

# open file you are going to write new results to
out_file = open("v6_novoseq2_zygosity_genomic.txt", "w")
r = 1
# for each line in vcf file
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you wan
            out_file.write(
            "#Chrom" + "\t" + "POS" + "\t" + "REF1" + "\t" + "REF2" + "\t")
            header_line = i.rstrip().split("\t")
            # grabbing individual names
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
        # splits each thing into their respective cells by tabs
        split_ind_line = i.rstrip().split("\t")
        #write CHROM POS R1 R2
        out_file.write(split_ind_line[0] + "\t" + split_ind_line[1] + "\t" + split_ind_line[3] + "\t" + split_ind_line[4] + "\t")
        
        #split_info_line = split_ind_line[7].split(":")
        # outputs locus name, you're going to need to output stuff from other columns to
        

        
        #out_file.write(split_info_line[0] + "\t" + split_info_line[1] + "\t" + split_info_line[2] + "\t")
        # iterates through individual's genotypes
        #z = 0
        for j in split_ind_line[9:len(split_ind_line)]:
            gen_data = j.split(":")
            #print j
            #z = z + 1
            #print z
            #if z > 9:
                # split the genotype cell
            #gen_data = j.split(":")
                #print gen_data[0]
                # call zygosity based
                # "0" = homo1
                # "1" = Het
                # "2"= homo2
                # "-9" = no data
            zygosity = gen_data[0]
            if zygosity == "0/0":
                genotype_to_print = "0"
            elif zygosity == "0/1":
                genotype_to_print = "1"
            elif zygosity == "1/1":
                genotype_to_print = "2"
            else:
                genotype_to_print = "-9"

                # print out the genotype
            out_file.write(genotype_to_print + "\t")


        out_file.write("\n")


out_file.close()  # script parse vcf file get alleles per individual

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:35:40 2019

@author: mboot217
"""

# Author: Matthew Bootsma
# Last edit: 10/17/2019
# this script will take a genepop with only 1 pop delimiter (e.g., vcf2genepop converted .gen) and insert pop delimiters
# This is useful when you have a big file that notepad doesn't want to open (fuck excel, I don't trust it)

#NOTE: THIS CODE IS DESIGNED TO HAVE INDIVIDUAL ID'S SHARE THE FIRST 6 CHARACTERS WITHIN A POPULATION, 
# VARIABLE CHARACTERS IN THIS PORTION OF THE NAME FOR INDIVIDUALS OF THE SAME POP WILL RESULT IN THEM BEING PARSED INTO DIFFERENT POPS!!!!

#set working directory
import os
os.getcwd()
os.chdir("D:/GTseq_sturgeon")
# open file you are going to write new results to
out_file = open("stg.G30.meanDP15.mac3.G70.l50.ID_delimited.gen", "w")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("stg.G30.meanDP15.mac3.G70.l50.ID.gen", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()
# for each line in genepop file
line_n = 0
pop_name = "EMPTY"
raw_vcf_array[55112]


for i in raw_vcf_array:
    # This loop gets us to the point where we have reached indv 1 and can initialze a pop ID
    if pop_name == "EMPTY":
        # Skip the inserted title, SNP names, and first pop designator
        # Just write them as they are with no edits
        if i.startswith("#"):
         #print(line_n)
         out_file.write(i)
         line_n = line_n+1
                        
        elif i.startswith("SNP"):
         #print(line_n)
         out_file.write(i)
         line_n = line_n+1
        # when we find the first pop delimiter,
        # write the line, then initialize the name of our first pop
        elif i.startswith("Pop"):
         #print(line_n)
         out_file.write(i)
         indv_n = raw_vcf_array[line_n+1].rstrip().split(",")
         pop_name = indv_n[0][0:4]
         line_n = line_n+1
    # We enter this loop after handling all the data through INDV 1, now we check every new indv agains this to see if a new pop has been reached
    elif pop_name != "EMPTY":
        # Skip lines with SNP data, they should start with either a 1 or a 0
        if i[0] == str(0):
            out_file.write(i)
            line_n = line_n+1
            next
        elif i[0] == str(1):
            out_file.write(i)
            line_n = line_n+1
            next
        elif i[0] == str(2):
            out_file.write(i)
            line_n = line_n+1
            next
        elif i[0] == str(3):
            out_file.write(i)
            line_n = line_n+1    
            next
        elif i[0] == " ":
            out_file.write(i)
            line_n = line_n+1    
            next
        # if the line start does not look like data, then consider it a name and check it agains the current POP batch
        else:
            # if it looks to be from the same pop, write line and continue
            if i.rstrip().split(",")[0][0:4] == pop_name:
                out_file.write(i)
                line_n = line_n+1 
            # if the pop[i] doesn't look the same, insert a pop ID, then write the individual on a new line, then reset the POP ID to the new pop batch
            elif i.rstrip().split(",")[0][0:4] != pop_name:
                out_file.write("Pop\n")
                out_file.write(i)
                print(pop_name)
                pop_name = i.rstrip().split(",")[0][0:7]
                print(pop_name)
                line_n = line_n+1 
                


out_file.close()  # script parse vcf file get alleles per individual

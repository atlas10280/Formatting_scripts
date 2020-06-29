#!/bin/bash -l

#SBATCH --job-name=vcf2genepop
#SBATCH -o vcf2genepop.out
#SBATCH -e vcf2genepop.err
#SBATCH --ntasks 1
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end 

enable_lmod
module load PGDSpider



java -Xmx16384m -Xms16384m -jar /scratch-lustre/wlarson/1710_WAE/PGDSpider2-cli.jar -inputfile ./RAD_SNPs_GT_seq_positions.recode.vcf -inputformat VCF -outputfile ./RAD_SNPs_GT_seq_positions.recode.gen -outputformat GENEPOP -spid ./vcf2genepop.spid


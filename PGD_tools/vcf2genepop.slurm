#!/bin/bash -l

#SBATCH --job-name=vcf2genepop
#SBATCH -o vcf2genepop.out
#SBATCH -e vcf2genepop.err
#SBATCH --ntasks 1
#SBATCH --mail-user=mbootsma@uwsp.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end 

enable_lmod
module load PGDSpider



java -Xmx16384m -Xms16384m -jar ./PGDSpider2-cli.jar -inputfile ./v2_Great_Lakes_WAE_haps.recode.vcf -inputformat VCF -outputfile ./v2_Great_Lakes_WAE_haps.recode.gen -outputformat GENEPOP -spid ./vcf2genepop.spid


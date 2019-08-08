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



java -Xmx16384m -Xms16384m -jar /scratch-lustre/wlarson/1710_WAE/PGDSpider2-cli.jar -inputfile ./v6_novoseq2_snps_genomic.recode.vcf -inputformat VCF -outputfile ./v6_novoseq2_snps_genomic.gen -outputformat GENEPOP -spid ./vcf2gen.spid


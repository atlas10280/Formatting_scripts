#!/bin/bash -l

#SBATCH --job-name=genepop2vcf
#SBATCH -o genepop2vcf.out
#SBATCH -e genepop2vcf.err
#SBATCH --ntasks 1
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end 

enable_lmod
module load PGDSpider



java -Xmx16384m -Xms16384m -jar /scratch-lustre/wlarson/1710_WAE/PGDSpider2-cli.jar -inputfile ./whitelisted_snps_inland-GL.gen -inputformat GENEPOP -outputfile ./whitelisted_snps_inland-GL.vcf -outputformat VCF -spid ./genepop2vcf.spid


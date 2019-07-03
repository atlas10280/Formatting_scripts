#!/bin/bash -l

#SBATCH --job-name=genepop2bayescan
#SBATCH -o genepop2bayescan.out
#SBATCH -e genepop2bayescan.err
#SBATCH --ntasks=8
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=end

enable_lmod
module load PGDSpider/2.1



java -Xmx16000m -Xms512m -jar '/scratch-lustre/wlarson/1710_WAE/STACKS_publish/filter_Populations/PGDSpider2-cli.jar' -inputfile './v6_SNPs_natural_pops.gen' -inputformat GENEPOP -outputfile './v6_SNPs_natural_pops.bayescan' -outputformat GESTE_BAYE_SCAN -spid './genepop2BayeScan.spid'
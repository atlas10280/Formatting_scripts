#!/bin/bash -l

#SBATCH --job-name=genepop2ped
#SBATCH -o genepop2ped.out
#SBATCH -e genepop2ped.err
#SBATCH --ntasks=8
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=end

enable_lmod
module load PGDSpider/2.1



java -Xmx16000m -Xms512m -jar /scratch-lustre/wlarson/1710_WAE/PGDSpider2-cli.jar -inputfile ./v4_MLB_novoseq2_snps_delimited.gen -inputformat GENEPOP -outputfile ./v4_MLB_novoseq2_snps_delimited.ped -outputformat PED -spid ./SPID_genepop2ped.spid
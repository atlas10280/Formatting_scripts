#!/bin/bash -l

#SBATCH --job-name=genepop2arlequin
#SBATCH -o genepop2arlequin.out
#SBATCH -e genepop2arlequin.err
#SBATCH --ntasks=8
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=end

enable_lmod
module load PGDSpider/2.1



java -Xmx16000m -Xms512m -jar /scratch-lustre/wlarson/1710_WAE/PGDSpider2-cli.jar -inputfile ./genomic_snps_allPops.gen -inputformat GENEPOP -outputfile ./genomic_snps_allPops.arp -outputformat ARLEQUIN -spid ./genepop2arlequin.spid
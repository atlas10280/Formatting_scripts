#!/bin/bash -l

#SBATCH --job-name=genepop2arlequin
#SBATCH -o genepop2arlequin.out
#SBATCH -e genepop2arlequin.err
#SBATCH --ntasks=8
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=end

enable_lmod
module load PGDSpider/2.1



java -Xmx16000m -Xms512m -jar /scratch-lustre/wlarson/1710_WAE/PGDSpider2-cli.jar -inputfile ./GL_mm0.7.maf.indv50.mm0.5.indv90.R2.mac4.W.recode.gen -inputformat GENEPOP -outputfile ./GL_mm0.7.maf.indv50.mm0.5.indv90.R2.mac4.W.recode.arp -outputformat ARLEQUIN -spid ./genepop2arlequin.spid
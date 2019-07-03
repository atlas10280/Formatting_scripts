#!/bin/bash -l

#SBATCH --job-name=genepop2arlequin
#SBATCH -o genepop2arlequin.out
#SBATCH -e genepop2arlequin.err
#SBATCH --ntasks=8
#SBATCH --mail-user=mboot217@uwsp.edu
#SBATCH --mail-type=end

enable_lmod
module load PGDSpider/2.1



java -Xmx16000m -Xms512m -jar '/scratch-lustre/wlarson/1710_WAE/STACKS_publish/filter_Populations/PGDSpider2-cli.jar' -inputfile '/scratch-lustre/wlarson/1710_WAE/barcode_repair_pipe/Raw_reads_18048_18050/U_out/v6_bcrepair_snps_NATURAL_POPS_code2.gen' -inputformat GENEPOP -outputfile './v6_bcrepair_snps_NATURAL_POPS.arp' -outputformat ARLEQUIN -spid './genepop2arlequin.spid'
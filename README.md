# manhattan-plots
This repo provides a tutorial on how to create manhattan plots of Population genetics variation measures such as Fixative index(fst) and TajimaD values using Python
# Description
the repository contains scripts as well as sample datasets on which the these scripts can be tested on. datasets are in the data directory and comprises of snps data (vcf format) and a list of sample ids (population) saved in text files. Fst values are generated using vcftools which takes as inputs snp data and list of populations on which the comparision is being done . The practice dataset comprises of two subpopulations BAN and GAM.
The snps data was taken from Pf3K project which can be found on the MalariaGen Database 


# Running the Pipeline

### Step 1: Clone or download the github repository
git clone https://github.com/vappiah/manhattan-plots

### Step 2: cd to the directory
cd manhattan-plots

### Step 3: verify that data and scripts have been downloaded
ls 

ls data

### Step 4: Add execution rights to the scripts
chmod +x *.{py,sh}

### Step 5: download and install tools : vcftools, mawk, python libraries(numpy,matplotlib,pandas,bioinfokit)
./download_tools.sh

### Step 6: Test tools
./test_tools.sh

### Step 7: filter snps
./filter_snps data/snps_indels.vcf.gz

### Step 8: compute fst values
./get_fst.sh data/BAN.txt data/GAM.txt snps.filtered.vcf.gz

### Generate manhattan plots
python plot_fst.py plot_fst data/BAN.txt data/GAM.txt 

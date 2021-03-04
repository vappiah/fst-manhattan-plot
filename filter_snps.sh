
vcf=$1
#mkdir tmp_filter
#cd tmp_filter

#filter to keep variants that are genotyped in 50% of individuals
vcftools --gzvcf $vcf --max-missing 0.5 --mac 3 --minQ 30 --recode --recode-INFO-all --out snps.raw.stage1

echo "FILTERING GENOTYPTES--------------"

#filter to select genotype with minimum depth of 3
vcftools --vcf snps.raw.stage1.recode.vcf --minDP 3 --recode --recode-INFO-all --out snps.raw.stage2

#get rid of individuals that did not sequence well
vcftools --vcf snps.raw.stage2.recode.vcf --missing-indv

#cat out.imiss
#create individuals with more thatn 50% missing data
mawk '$5 > 0.5' out.imiss | cut -f1 > lowDP.indv

#use the list to remove from vcf
vcftools --vcf snps.raw.stage2.recode.vcf --remove lowDP.indv --recode --recode-INFO-all --out snps.raw.stage3

#restrict data to variants called in high percentage of isolates
vcftools --vcf snps.raw.stage3.recode.vcf --max-missing 0.95  --remove-indels --maf 0.05 --recode --recode-INFO-all --min-meanDP 20 --stdout | gzip -c > snps.filtered.vcf.gz

#mv snps.filtered.vcf.gz ../
#cd ../
echo "SNP FILTERING COMPLETE"
echo "filtered file : ${pwd}/snps.filtered.vcf.gz"







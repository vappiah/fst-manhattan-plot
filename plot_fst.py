import pandas as pd
import sys
from manhattan import mhat

file_=sys.argv[1]
df=pd.read_csv(file_,sep='\t')
chroms=df['CHROM'].unique()
chroms=list(chroms)
chroms.sort()
df['CHROM_NEWHEADER']=df['CHROM'].apply(lambda i: chroms.index(i)+1)
selected=df.dropna()

mhat(selected,chr='CHROM_NEWHEADER',pv='WEIR_AND_COCKERHAM_FST',show=False,color=('black','red'))

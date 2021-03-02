import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from matplotlib.colors import ListedColormap
from bioinfokit.visuz import general

def mhat(df="dataframe", chr=None, pv=None, color=None, dim=(6,4), r=300, ar=None, gwas_sign_line=False,
             gwasp=5E-08, dotsize=8, markeridcol=None, markernames=None, gfont=8, valpha=1, show=False, figtype='png',
             axxlabel=None, axylabel=None, axlabelfontsize=9, axlabelfontname=None, axtickfontsize=9,
             axtickfontname="Arial", ylm=None, gstyle=1, figname='manhatten'):

        _x, _y = 'Chromosomes', r'$ -log_{10}(P)$'
        rand_colors = ('#a7414a', '#282726', '#6a8a82', '#a37c27', '#563838', '#0584f2', '#f28a30', '#f05837',
                       '#6465a5', '#00743f', '#be9063', '#de8cf0', '#888c46', '#c0334d', '#270101', '#8d2f23',
                       '#ee6c81', '#65734b', '#14325c', '#704307', '#b5b3be', '#f67280', '#ffd082', '#ffd800',
                       '#ad62aa', '#21bf73', '#a0855b', '#5edfff', '#08ffc8', '#ca3e47', '#c9753d', '#6c5ce7',
                       '#a997df', '#513b56', '#590925', '#007fff', '#bf1363', '#f39237', '#0a3200', '#8c271e')

        if not axylabel:
                axylabel=pv
        # minus log10 of P-value
        #df['tpval'] = -np.log10(df[pv])
        #df['tpval']=[i for i in df[pv]]
        
        # df = df.sort_values(chr)
        # if the column contains numeric strings
        df = df.loc[pd.to_numeric(df[chr], errors='coerce').sort_values().index]
        # add indices
        df['ind'] = range(len(df))
        df_group = df.groupby(chr)
        if color is not None and len(color) == 2:
            color_1 = int(df[chr].nunique() / 2) * [color[0]]
            color_2 = int(df[chr].nunique() / 2) * [color[1]]
            if df[chr].nunique() % 2 == 0:
                color_list = list(reduce(lambda x, y: x+y, zip(color_1, color_2)))
            elif df[chr].nunique() % 2 == 1:
                color_list = list(reduce(lambda x, y: x+y, zip(color_1, color_2)))
                color_list.append(color[0])
        elif color is not None and len(color) == df[chr].nunique():
            color_list = color
        elif color is None:
            # select colors randomly from the list based in number of chr
            color_list = sample(rand_colors, df[chr].nunique())
        else:
            print("Error: in color argument")
            sys.exit(1)

        xlabels = []
        xticks = []
        fig, ax = plt.subplots(figsize=dim)
        i = 0
        for label, df1 in df.groupby(chr):
            df1.plot(kind='scatter', x='ind', y=pv, color=color_list[i], s=dotsize, alpha=valpha, ax=ax)
            df1_max_ind = df1['ind'].iloc[-1]
            df1_min_ind = df1['ind'].iloc[0]
            xlabels.append(label)
            xticks.append((df1_max_ind - (df1_max_ind - df1_min_ind) / 2))
            i += 1

        # add GWAS significant line
        if gwas_sign_line is True:
            ax.axhline(y=-np.log10(gwasp), linestyle='--', color='#7d7d7d', linewidth=1)
        if markernames is not None:
            marker.geneplot_mhat(df, markeridcol, chr, pv, gwasp, markernames, gfont, gstyle, ax=ax)
        ax.margins(x=0)
        ax.margins(y=0)
        ax.set_xticks(xticks)
        ax.set_ylim([0, max(df[pv] + 1)])
        
        if ylm:
            ylm = np.arange(ylm[0], ylm[1], ylm[2])
        else:
            ylm = np.arange(0, 1.2, 0.2)
        ax.set_yticks(ylm)
        ax.set_xticklabels(xlabels, rotation=ar)
        # ax.set_yticklabels(ylm, fontsize=axtickfontsize, fontname=axtickfontname, rotation=ar)
        if axxlabel:
            _x = axxlabel
        if axylabel:
            _y = axylabel
        ax.set_xlabel(_x, fontsize=axlabelfontsize, fontname=axlabelfontname)
        ax.set_ylabel(_y, fontsize=axlabelfontsize, fontname=axlabelfontname)
       
        general.get_figure(show, r, figtype, figname)



#visuz.marker.mhat(selected,chr='CHROM_NEWHEADER',pv='WEIR_AND_COCKERHAM_FST',show=True,color=('black','red'))

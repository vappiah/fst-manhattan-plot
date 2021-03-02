#!/bin/bash
appsdir=$(pwd)/apps
vcftoolsdir=$appsdir/vcftools

export PATH=$PATH:$vcftoolsdir/bin

export PERLLIB=$vcftoolsdir/lib:$PERLLIB
export PERL5LIB=$vcftoolsdir/lib:$PERL5LIB

export PATH=$PATH:$appsdir/mawk/bin

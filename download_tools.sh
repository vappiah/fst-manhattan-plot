
#!/bin/bash

homedir=$(pwd)

mkdir apps

mkdir tmp

wget https://github.com/vcftools/vcftools/zipball/master -O tmp/master.zip
unzip tmp/master.zip
vcftools_raw=$(ls -d */|grep vcftools)
$vcftools_raw


vcftoolsdir=$homedir/apps/vcftools
mkdir $vcftoolsdir

cd $vcftools_raw

./autogen.sh
./configure --prefix $vcftoolsdir 
make
make install


#export PATH=$PATH:$vcftoolsdir/bin
mkdir $vcftoolsdir/lib
cp src/perl/{Vcf.pm,FaSlice.pm,VcfStats.pm} $vcftoolsdir/lib 
export PERLLIB=${homedir}/vcftools/lib:$PERLLIB
export PERL5LIB=${homedir}/vcftools/lib:$PERL5LIB

echo $PERLLIB
echo $PERL5LIB

#mv master.zip tmp

cd $homedir

mv -v $vcftools_raw tmp
wget https://invisible-island.net/datafiles/release/mawk.tar.gz -O tmp/mawk.tar.gz
#wget https://github.com/ThomasDickey/mawk-20140914

tar xvfz tmp/mawk.tar.gz
mawkdir=$(ls -d */|grep mawk)
mkdir $homedir/apps/mawk
cd $mawkdir
./configure --prefix=$homedir/apps/mawk
make
make install


cd $homedir
mv -v $mawkdir tmp

pip3 install virtualenv --user
virtualenv apps/fst-env

source apps/fst-env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

deactivate

echo "Tools have been installed"
echo "Please run the following commands" 
echo "Run \"source add_apps_to_path.sh\" to add apps to path"
echo "Run \"./test_tools.sh\" to test the installations"




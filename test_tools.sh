#TEST TOOLS

echo "________________________________________________________________"
vcftools --version
echo " "
echo "________________________________________________________________"

mawk -W version
echo " "
echo "________________________________________________________________"


python3 -c "import sys;print(\"Python version:\",sys.version)"
python3 -c "import bioinfokit;print(\"Bioinfokit version:\",bioinfokit.__version__)"
python3 -c "import matplotlib;print(\"Matplotlib version:\",matplotlib.__version__)"
python3 -c "import numpy;print(\"Numpy version:\",numpy.__version__)"
python3 -c "import pandas;print(\"Pandas version:\",pandas.__version__)"

echo " "
echo "________________________________________________________________"


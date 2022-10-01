# Jupiter_nexus
Repo for NASA hackaton

Download Anaconda in:
https://www.anaconda.com

To clone env:
conda env create --name jupiter_env -f jupiter_env.yml

To use conda in Windows:
1. conda init powershell
2. reset shell
3. conda config --set auto_activate_base false
4. conda activate jupiter_env


Make sure you're using python from the env, not the local one installed.

Useful .fits documentation with astropy (how to read a .fits):
https://hst-docs.stsci.edu/hstdhb/4-hst-data-analysis/4-4-working-with-fits-data-in-python

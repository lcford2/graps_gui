# graps_gui
GUI for creating GRAPS Input Files

Create python environment for running the GUI by using `conda env create -f environment.yml` from the command line.

If you do not have `conda` installed, you can get the correct version for your machine [here](https://www.anaconda.com/products/individual).

After you have created the environment, run `conda activate graps_gui` from the command line to activate the correct environment. To open then interface, run `python gui` in the command line from within the `graps_gui` directory. 

# GRAPS Model
To obtain the executables and source code for GRAPS, run `git submodule init` and `git submodule update` after you clone this repository. This will pull the code from the [GRAPS Repository](https://www.github.com/lcford2/GRAPS) and put in the `GRAPS` folder. After you export the model you create with the GUI, you can copy the executables from the folder for your operating system into the export folder and run the `multireservoir` executable. 
# GRAPS Interface
Graphical user interface to interact with the [GRAPS Model](https://github.com/lcford2/GRAPS)

Create python environment for running the GUI by using `conda env create -f environment.yml` from the command line.

If you do not have `conda` installed, you can get the correct version for your machine [here](https://www.anaconda.com/products/individual).

After you have created the environment, run `conda activate graps_gui` from the command line to activate the correct environment. To open then interface, run `python gui` in the command line from within the `graps_gui` directory. 


# Documentation
From within the interface you can access the documentation by clicking the *Help* button in the menu bar.

# GRAPS Model
In order to run the model from within the interface, you will need to also download the GRAPS model repository. It simplify this for users, we have embedded it as a submodule within this repository. To obtain the executables and source code for GRAPS, run `git submodule init` and `git submodule update` after you clone this repository. This will pull the code from the [GRAPS Repository](https://www.github.com/lcford2/GRAPS) and put in the `GRAPS` folder. After you export the model you create with the GUI, you can copy the executables from the folder for your operating system into the export folder and run the `multireservoir` executable. 

Alternatively you can simply clone the [GRAPS Repository](https://www.github.com/lcford2/GRAPS) separately and follow instructions in its [`README.md`](https://github.com/lcford2/GRAPS#graps) to run the model. Regardless, it is good to familiarize yourself with the information in the [GRAPS `README.md`](https://github.com/lcford2/GRAPS#graps). 

# Getting Code Updates
Because this software package is still largely in develepment, we have not made a release yet. To get recent gui updates, run `git pull` from within the `graps_gui` folder. To get recent GRAPS updates, run `git submodule update --remote` from within the `graps_gui` folder. If you have not ran the commands in the GRAPS Model section above, you will not be able to pull recent GRAPS updates or run the model. 

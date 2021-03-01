# 2dQGnum

-------------------------------------------------
Two-dimensional quasi-geostrophic numerical model
-------------------------------------------------

Author: 	Kristine Flacké Haualand

Year: 		2015

Location: 	Geophysical Institute, University of Bergen, Bergen, Norway


For questions/suggestions: Kristine.Haualand@uib.no

-----------
Description
-----------

A model exploring modal growth in baroclinic development. This code calculates the eigenvalue s (baroclinic wave frequency as a complex number) and eigenvector x (vertical profile of QG streamfunction and omega vertical velocity as complex numbers) from a matrix problem Ax=sBx based on the potential vorticity and omega equations for a set of predefined zonal wavenumbers. The wave structure of the eigenvectors is found for two dimensions (x,p) by using a wave solution exp(ikx).


Model is inspired by and extended from the analytical model by:

Mak, M. (1994). Cyclogenesis in a conditionally unstable moist baroclinic atmosphere. Tellus A, 46(1), 14-33, https://doi.org/10.1034/j.1600-0870.1994.00003.x.


Description of method and application can be found in:

Haualand, K. F., & Spengler, T. (2019). How does latent cooling affect baroclinic development in an idealized framework?. Journal of the Atmospheric Sciences, 76(9), 2701-2714, https://doi.org/10.1175/JAS-D-18-0372.1.

---------
Structure
---------

main.ipynb            --> main program run in Jupyter Notebook

input_variable.py     --> setup of experiments, definition of constants

plotting_settings.py  --> some general plotting settings

model_core.py         --> definition and solution of matrix problem

prepare_variables.py  --> calcucating new model variables and extending all model variables to two dimensions

plot_output.py        --> scripts for visualisation of model output

trajectories.py       --> calulcates backward trajectories

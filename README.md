# fokkerplanck
The file **fplanck.py** contains the python script to perform numerical integration of the Fokker Planck equation as described in the main paper (still to be uploaded). 

The script is meant to integrate Fokker Planck equation for two populations with initial condition a Dirac Delta centered in zero. 

Parameters for the integration (drift term, diffusion term, integration step, boundary conditions, length of the integration range and number of nodes over which integration must be computed,...) can be changed within the script. 
Diffusion term and drift term - set as constants for the purpose of the project - can be easily changed to become function of space and/or time. 

Language: python; libraries used: Numpy and Matplotlib

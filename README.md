# fokkerplanck

The content of this repository is the Supplementary material associated to the project *Modeling Hydrogen Deuterium Exchange as a Stochastic Process*. 
The comprehension of the content of the repository is strictly linked to the content of the main paper (still to be uploaded).

The file **solve.py** contains the script to perform numerical integration of the Michaelis Menten model that describes hydrogen deuterium uptake. 
The parameters of the integration (initial conditions, time step, total number of steps,...) can be changed within the script. 
Some double comments ## are present: when cancelled, the script gives the numerical proof of the equivalence between one model with initial conditions different from 0 for both states A and B and a system of two models of the same type but with initial conditions set at A(0)=1 in one case and B(0)=1 in the other. Further information in the main paper. 

The file **fplanck.py** contains the python script to perform numerical integration of the Fokker Planck equation as described in the main paper (still to be uploaded). 
The script is meant to integrate Fokker Planck equation for two populations with two different drift velocities and as initial condition a Dirac Delta centered in zero. 
Parameters for the integration (drift term, diffusion term, integration step, boundary conditions, length of the integration range and number of nodes over which integration must be computed,...) can be changed within the script. 
Diffusion term and drift term - set as constants for the purpose of the project - can be easily changed to become function of space and/or time. 

The file **b0.py** basically contains the plot shown in Figure 5 of the main paper. 
It implements the equation to calculate initial condition of state B out of the values of exchange rates.

Language: python; libraries used: Numpy and Matplotlib

******************************************************************************
# Monte Carlo based Pathway Search (MCPS) for exploring molecular processes in high-dimensional conformational space

Contributors: Archit Vasan and Nandan Haloi

Affiliation: University of Illinois at Urbana-Champaign

Emails: akvasan2@illinois.edu, nhaloi2@illinois.edu

## General overview: 

Method to efficiently and systematically sample high-dimensional molecular processes while considering multiple slow degrees of freedom. In our implementation, we focus on obtaining permeation pathways of antibiotics through outer membrane porins. 

## Procol involves 3 steps:

### 1. Exhaustive search for antibiotic poses 

####Code description:

Exhaustively searches for antibiotic poses within translational and rotational space.  After this search, a multidimensional energy landscape is created by evaluating antibiotic-protein interaction energy for each pose. (Found in Conf_Search directory) 

#### Divided into 4 substeps:

#### A. Exhaustive initial search of all poses for the antibiotic. Involves: generating multiple drug orientations, translating the drug to all possible positions within protein at points along a grid, and removing clashes or ring pierces between drug and protein. (Found in Conf_Search/Initial_Search) 

##### Required files:
        	
	Structure and coordinate files (i.e. psf, pdb) files stored as Conf_Search/Input_Files/system.psf and Conf_Search/Input_Files/system.pdb

##### How to run:
	
	cd Conf_Search/Initial_Search
	
	vmd

	source run.tcl

	Note: must first open vmd in gui mode and then source run.tcl

##### Output:

	dcds/dcdsstart_*.dcd: dcd containing each pose

#### B. Minimization of each pose obtained from initial search.  (Found in Conf_Search/Minimization) 
	
##### Required files:

	Structure and coordinate files (i.e. psf, pdb) files stored as Conf_Search/Input_Files/system.psf and Conf_Search/Input_Files/system.pdb

	Parameter files: stored in Conf_Search/Parameters
        
	fixedAtomsFile specifying atoms to be fixed: stored as ../../Input_Files/fix.pdb. The B column of each atom of the two molecules should equal 1 or 2 
        
##### How to run:

	bash run.sh

##### Output:

	minimize_output/dcdsstart_*.dcd

#### C. Evaluation of pair interaction energy of the minimized drug poses. (Found in Conf_Search/Analysis/PIE)

##### Required files:
	
	Structure and coordinate (e.g. psf and pdb) files stored in Conf_Search/Input_Files
	
	Parameter files: stored in Conf_Search/Parameters
	
	pairInteractionFile (PIE.pdb):specifying atoms of the pair of molecules for calculating PIE.  B column of each atom of the two molecules should equal 1 or 2 

##### How to run:
	
	bash run.sh 

##### Output:
	
	Output/PIE.dat

#### D. Evaluation of values for the slow coordinates (z-coordinate, inclination, azimuthal) for the drug poses. Very important to obtain this data to use in the MCPS algorithm (Found in Conf_Search/Analysis/Slow_Coordinates) 

##### Required files:
	
	Structure (i.e. psf) file stored as Conf_Search/Input_Files/system.psf

##### How to run:
	
	vmd slow_coor.tcl 

##### Output:

	slow_coor.dat: columns are z-coor, inclination, azimuthal data for each pose 

### 2. Monte Carlo Based Pathway Search (MCPS). 

#### Code description:

Algorithm to walk through the energy landscape using MC moves. Since rotation and translation are slow degrees of freedom, limited changes in antibiotic orientation and position are allowed in each MC move. Need to run this multiple times to obtain multiple trajectories such that interested conformational space is sufficiently sampled. You can determine the convergence by plotting the trajectory density, projected onto the individual conformation spaces. This code can be run on multiple processors. (Found in MCPS directory) 

##### How to run:

	python run.py

##### Output:

	Output_Files/transition_search.dat


### 3. Determination of most likely pathways sampled in our MCPS trajectories. The trajectory data is used to construct a transition matrix which is inputted into Dijkstra's algorithm to obtain the most likely path. Can also be used to distinguish diverging paths. (Found in MostLikelyPathway directory)

#### Divided into 2 substeps:

#### A. Filtering trajectories (Found in MostLikelyPathway)	

##### How to run:

	python Filter_Trajectories.py

##### Output:

	Traj_Group_Data/cluster1_paths.dat
		   
	Traj_Group_Data/cluster2_paths.dat

#### B. Idenfitication of most likely pathways (Found in MostLikelyPathway/Dijkstras) 

##### How to run:

	python Dijkstras/Find_Paths.py

##### Output:

	Cluster1/pathway.dat: Most Likely Path files for each group 
	Cluster2/pathway.dat

## Necessary softwares/programming environments:

	VMD
	Additional VMD plugins necessary: 
		Orient: Instructions to install are at https://www.ks.uiuc.edu/Research/vmd/script_library/scripts/orient/
	
	Python 3
	Modules necessary:
		numpy
		math
		random
		multiprocessing
		joblib
		csv
		matplotlib

	NAMD2

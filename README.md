# Prediciting-beta-turns-with-neural-network

# Introduction

Following code was developed as a final project during bachelors course. Goal was to predict if specyiffic aminoacid in a protein sequence will be a part of beta turn. 
I decided to use for that position of speciffic atoms (alfa carbon and nitrogen) of each aminoacid in relation to their neighbours. Neural network uses following distances and properties:

- distance between C(i) and N(i+3)
- distance between C(i) and C(i+3)
- distance between C(i) and C(i-3)
- coordinates of C alfa and N in 3D space
- information what aminoacid is in analyzed residue  

# Results:

- Developed model is capable of detecting around 80% of all amino acids being a part of beta turn
- 3 out of 4 amino acids marked by neural network as beta turn indeed are a part of beta turn

# Code

Version of neural network which ca be found in the repository is considered to be finall (at least for now)

Code used for creating data set was at first developed as a prototype and is still undergoing refactoring and development in order to be easy to use therfore for now version in this repository is complete in about 80%. Once the basic functionality will be uploaded, the idea is to further develop it and add abbility to create also diffrent datasets based on list PDB codes - containing diffrent informations about residues.

Proteins used in uploaded dataset were selected based on: Guruprasad K, Rajkumar S. ‘Beta-and gamma-turns in proteins revisited: a new set of amino acid turn-type dependent positional preferences and potentials.’ Journal of biosciences. 2000 6;25(2): 143–56.  

I am fine with anyone using code found in this repository as long as you give me credit.

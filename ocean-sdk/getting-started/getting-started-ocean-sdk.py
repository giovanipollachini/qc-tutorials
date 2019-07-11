##################################################
# Instructions
##################################################
'''
Runs the QUBO Algorithm for simulating a NOT gate on file 'qubo_not_gate.py'
on a local simulator (Ocean SDK).

Running this file on the Python Interpreter:
   01 - Open the virtual environment in which the Ocean SDK is installed
        >>> cd ~
        >>> source ocean/bin/activate
   01 - Run the following command in the interpreter
        >>> exec(open('qubo_not_gate.py').read())

The variables in these programs will be acessible in the interpreter.

NOT gate as a QUBO problem:
objective function:  2xz - x - z 
                     x,z in {0,1}
The minimum configurations for this function are the solution of the problem,
and the possible outcomes for the NOT gate.
QUBO upper diagonal matrix:
Q = [ -1 ,  2 ;
       0 , -1 ]

'''



##############################################
# EXACT SOLVER
##############################################

# Import libraries
import dimod


# Define Solver
solver = dimod.ExactSolver()


# Input QUBO coefficients
Q = {('x', 'x'): -1, ('x', 'z'): 2, ('z', 'x'): 0, ('z', 'z'): -1}
h = {'x': -1, 'z': -1}
J = {('x', 'z'): 2}
# J = {('x', 'z'): 1, ('z', 'x'): 1}


# Get response from Ising Solver
# response = solver.sample_ising(h,J)
# or
# bqm = dimod.BinaryQuadraticModel.from_ising(h, J)
# response = solver.sample(bqm)

# Get response from QUBO Solver
bqm = dimod.BinaryQuadraticModel.from_qubo(Q)
response = solver.sample(bqm)


# Print result sample and energy
# - the minimum energy corresponds to the answer to the problem
sample = []
energy = []
print('Energy and samples for the Hamiltonian:')
print('sample', ' | ' , 'energy')
for s, e in response.data(['sample', 'energy']): 
   print(s, ' | ',e)
   sample += [s]
   energy += [e]
print('\n')


# Find solutions (minimum energy)
n_sol = 0
index_sol = []
for index in range(len(energy)):
   if energy[index] == min(energy):
      n_sol += 1
      index_sol += [index]
      
print('Minimum energy solutions:')
for index in index_sol:
   print(sample[index], ' | ',energy[index])
print('\n')





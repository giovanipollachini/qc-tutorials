""" 
Use Forest SDK (Rigetti) to create an entanglement circuit 
for producing the Bell state
     |00> + |11>
    ------------- .
       sqrt(2)
The circuit is simulated on a local Quantum Virtual Machine.
Running this circuit on the Python Interpreter:
   01 - Open 3 terminals
   02 - On one of then, start the Quantum Virtual Machine
        qvm -S
   03 - On the other one, run the compiler
        quilc -S
   04 - On the third terminal, open the virtual environment
        in which the Pyquil/Forest is installed
        >>> cd ~
        >>> source ocean/bin/activate
        Then, move to the directory of this file and
        open the Python Interpreter:
        $ cd Directory/of/the/program
        $ python
   05 - Run file using the following command in the interpreter
        >>> exec(open('getting-started-forest-sdk.py').read())

The variables in this program will be acessible in the interpreter
after the program finishes running.


"""


##################################################
# Import PyQuil library
##################################################

import pyquil as pq
import numpy as np


##################################################
# Write program
##################################################

p = pq.Program(
    pq.gates.H(0),
    pq.gates.CNOT(0,1)
)
print('Quantum Program in PyQuil (without measurements):')
print(p)
print('\n')

##################################################
# Inspect Wavefunction
##################################################
print('Inspecting wavefunction after the quantum circuit:')
print(pq.api.WavefunctionSimulator().wavefunction(p))
print('\n')

##################################################
# Measurement
##################################################
ro = p.declare('ro','BIT',2)
p += pq.gates.MEASURE(0,ro[0])
p += pq.gates.MEASURE(1,ro[1])

##################################################
# Print program
##################################################
print('Quantum Program in PyQuil (complete):')
print(p)
print('\n')


##################################################
# Run the program on a local simulator
##################################################

# List available backends to run the circuit
av_backends = pq.list_quantum_computers()
av_backends_sim = []
for backend in av_backends:
   if backend[-3:] == 'qvm':
      av_backends_sim.append(backend)
print('Available backends for simulating the circuit:',
      *av_backends_sim,
      '2q-qvm',
      '3q-qvm',
      'nq-qvm for n = 2, 3, 4, ...',
      sep='\n   ')
print('\n')


# Request a 2 qubit QVM (quantum virtual machine)
print('Using backend 2q-qvm and creating quantum circuit.')
print('\n')
qc = pq.get_qc('2q-qvm')

# Compile the circuit
trials = 32
p.wrap_in_numshots_loop(trials)
qc_exec = qc.compile(p)


# Run the program on the QVM
print('Running the program on choosen backend.')
print('\n')

result = qc.run(qc_exec)
#result = qc.run_and_measure(p, trials=trials)


# Print the result of the tests
print('Results for the qubits in each shot:',
       '[q0 q1]',
       result,
       sep='\n')
print('\n')


# Counting the states (integer notation)
# Creating dictionary with key = state and value = counts
# (integer notation)
counts = dict(zip(list(range(4)),[0]*4))
# Passing counts to the dictionary
state = 0
for i in range(trials):
   state = int(result[i][0]) + 2*int(result[i][1])
   counts[state] =  counts[state] + 1
# Print the results (in integer notation)
print("The results of the simulation are:")
print("(integer notation)")
print('   ','State','  ','Counts')
for key,val in counts.items() :
   print('   ',key,'     ',val)
print('\n')


# Counting the states (binary notation)
# Creating list of possible binary states
states = []
for state_int in range(4):
   states.append(bin(state_int).split('b')[1].zfill(2))
# Creating dictionary with key = state and value = counts
# (binary notation)
counts = dict(zip(states,[0]*4))
# Passing counts to the dictionary
state = 0
for i in range(trials):
   state_int = int(result[i][0]) + 2*int(result[i][1])
   state_bin = bin(state_int).split('b')[1].zfill(2)
   counts[state_bin] =  counts[state_bin] + 1
# Print the results (in binary notation)
print("The results of the simulation are:")
print("(binary notation)")
print('   ','State','  ','Counts')
for key,val in counts.items() :
   print('   ',key,'     ',val)
print('\n')

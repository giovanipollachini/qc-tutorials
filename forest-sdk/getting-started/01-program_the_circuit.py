""" 
01-program_the_circuit.py

Use Forest SDK (Rigetti) to create an entanglement circuit 
for producing the Bell state
     |00> + |11>
    ------------- .
       sqrt(2)

Running this circuit on the Python Interpreter:
   01 - Open 3 terminals
   02 - On one of then, start the Quantum Virtual Machine
        qvm -S
   03 - On the other one, run the compiler
        quilc -S
   04 - on the third terminal, open the Python Interpreter
         in the same directory as this file:
        $ python
   05 - Run file using the following command in the interpreter
        >>> exec(open('01-program_the_circuit.py').read())

The variables in this program will be acessible in the interpreter.

After running this file, it is possible to run files
02-run_on_simulator.py
# 03-run_on_qc.py
to run the circuit on a QVM.

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
print('Inspecting Wavefunction:')
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
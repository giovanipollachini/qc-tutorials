""" 
01-program_the_circuit.py

Create entanglement circuit for producing Bell state
     |00> + |11>
    ------------- .
       sqrt(2)

Running this circuit on the Python Interpreter:
   01 - Open terminal in the same directory as this file
   02 - Open the Python Interpreter:
        $ python
   03 - Run file using the following command in the interpreter
        >>> exec(open('01-program_the_circuit.py').read())

The variables in this program will be acessible in the interpreter.

After running this file, it is possible to run files
02-run_on_simulator.py
03-run_on_qc.py
to run the circuit on a simulator or on an IBM quantum computer.

"""


##################################################
# Import Qiskit library
##################################################

import qiskit as qk

##################################################
# Basic definitions
##################################################

# Define classical and quantum registers
q = qk.QuantumRegister(2)
c = qk.ClassicalRegister(2)

# Define a quantum circuit
qc = qk.QuantumCircuit(q,c) 

##################################################
# Define operations inside the quantum circuit qc
##################################################

# Hadamard gate on the first qubit
qc.h(q[0])
# CNOT gate with controll q[0] and target q[1]
qc.cx(q[0],q[1])

##################################################
# Measurement in qc
##################################################

# Call measure method for the object QuantumCircuit
qc.measure(q,c)


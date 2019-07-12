""" 
Create entanglement circuit for producing Bell state
     |00> + |11>
    ------------- .
       sqrt(2)

Running this circuit on the Python Interpreter:
   01 - Open the virtual environment
        in which Qiskit is installed
        >>> cd ~
        >>> source qiskit/bin/activate
        cd to the same directory as this file
   02 - Open the Python Interpreter:
        $ python
   03 - Run file using the following command in the interpreter
        >>> exec(open('getting-started-qiskit.py').read())

The variables in this program will be acessible in the interpreter.


"""


##################################################
# Import Qiskit library.
##################################################

import qiskit as qk

##################################################
# Basic definitions.
##################################################

# Define classical and quantum registers
q = qk.QuantumRegister(2)
c = qk.ClassicalRegister(2)

# Define a quantum circuit
qc = qk.QuantumCircuit(q,c) 

##################################################
# Define operations inside the quantum circuit qc.
##################################################

# Hadamard gate on the first qubit
qc.h(q[0])
# CNOT gate with controll q[0] and target q[1]
qc.cx(q[0],q[1])


##################################################
# Measurement in qc.
##################################################

# Call measure method for the object QuantumCircuit
qc.measure(q,c)

##################################################
# Print the Quantum Circuit qc.
##################################################

# Print the Quantum Circuit qc
print('Quantum Circuit')
print(qc)
print('\n')

##################################################
# Define in which device / simulator the circuit will be executed.
##################################################

# List available backends to execute the circuit
# Each backend is a python object
av_backends_sim = qk.Aer.backends()
print('Available backends for running the circuit:',
      *av_backends_sim,
      sep='\n   ')
print('\n')

# Define backend to be the qasm_simulator
backend_sim = qk.Aer.get_backend('qasm_simulator')


##################################################
# Execute the quantum circuit qc within the choosen backend.
##################################################

# Execute a simulation of the quantum circuit
print('Running the circuit')
print('\n')
job_sim = qk.execute(qc, backend_sim)

# Show information about the execution
# job_sim.status()
job_sim_status_old = job_sim.status()
while True:
   if job_sim.status().name == 'DONE':
      print('Status of the execution:',
            job_sim.status().name,
            job_sim.status().value,
            sep='\n   ')
      print('\n')
      break
   elif job_sim.status().name != job_sim_status_old.name \
        and job_sim.status().name != 'DONE':
      print('Status of the execution:',
            job_sim.status().name,
            job_sim.status().value,
            sep='\n   ')
      print('\n')
      job_sim_status_old = job_sim.status()

# Show which backend was used in the execution
job_sim.backend()
print('Backend used in the execution:',
      job_sim.backend(),
      sep='\n   ')
print('\n')


##################################################
# Get results from simulation.
##################################################

result_sim = job_sim.result()
print("The results of the simulation are:")
print(result_sim.get_counts(qc))
print('   ','State','  ','Counts')
for key,val in result_sim.get_counts(qc).items():
   print('   ',key,'     ',val)



""" 
02-run_on_simulator.py

Run entanglement circuit provided on file '01-program_the_circuit.py' on simulator.

Running this file on the Python Interpreter:
   01 - Open terminal in the same directory as this file
   02 - Open the Python Interpreter:
        $ python
   03 - Run the following commands in the interpreter
        >>> exec(open('01-program_the_circuit.py').read())
        >>> exec(open('02-run_on_simulator.py').read())

The variables in these programs will be acessible in the interpreter.

"""

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


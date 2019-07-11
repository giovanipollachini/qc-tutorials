""" 
02-run_on_simulator.py

Run entanglement circuit provided on file '01-program_the_circuit.py' on a simulator (QVM).

Running this file on the Python Interpreter:
   01 - Open 3 terminals
   02 - On one of then, start the Quantum Virtual Machine
        qvm -S
   03 - On the other one, run the compiler
        quilc -S
   04 - on the third terminal, open the Python Interpreter
         in the same directory as this file:
        $ python
   05 - Run the following commands in the interpreter
        >>> exec(open('01-program_the_circuit.py').read())
        >>> exec(open('02-run_on_simulator.py').read())

The variables in these programs will be acessible in the interpreter.

"""


##################################################
# Run the program on a QVM
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
print('Result of the qubits:',
       '[q0 q1]',
       result,
       sep='\n')
print('\n')


# Counting the states
state = []
counts = dict(zip(list(range(4)),[0]*4))
for i in range(trials):
   state.append(int(result[0][i]) + 2*int(result[1][i]))
   counts[state[i]] =  counts[state[i]] + 1

print("The results of the simulation are:")
print('   ','State','  ','Counts')
for key,val in counts.items() :
   print('   ',key,'     ',val)



# Qiskit

## How to install

### Instructions from Qiskit documentation

Instructions: https://github.com/Qiskit/qiskit-terra

### Creating virtual environment in Python
Often different projects require libraries with different versions. The virtual environment is a method to keep controll of the software needed in different projects and avoid conflicts of versions.

```shell
# Move to the directory you want to use to create the virtual environment
# (often created inside the home directory)
cd My/virtual/env/here
# Create virtual environment named "qiskit"
virtualenv qiskit
# Activate virtual environment
source qiskit/bin/activate
```
If you use an older version of python as default, you might need to specify a newer one when creating the virtual environment.
```shell
# Create virtual environment named "qiskit" with python version my-python-version
virtualenv qiskit --python=my-python-version
```

### Installing Qiskit
Once inside a virtual environment, you can install the software via:

```shell
pip install qiskit
```


## How to run a program (local simulation) on Python interpreter

First you need to activate the virtual environment in which the Ocean SDK is installed.

```shell
# Move to the directory of the virtual environment
# (often created inside the home directory)
cd My/virtual/env/here
# Activate virtual environment
source qiskit/bin/activate
```

Next, you need to enter the Python Interpreter from inside the directory of your python program.

```shell
# Move to the directory of the python program
cd My/python/program/directory
# Enter the python interpreter
python
```

The following command in python executes the python program and keeps the results and the variables in memory for further use. This behaviour is similar to Matlab, in which you run a .m script and the variables are kept in the workspace, where you can read or use them latter. 

```python
# Run Python program in the interpreter
exec(open('my-python-program.py').read())
```

## Getting Started

The program `getting-started-qiskit.py` is a simple example of how to write a program using Qiskit. 

### Purpose of the program
Create the Bell State:
![bell-state](images/bell-state.png)



### Operation principle 

The Bell state mentioned above can be created by the following quantum circuit:
![quantum-circuit](images/quantum-circuit.png)


### How to run the program

Let's suppose the virtual environment is set up in the home directory and this GitHub repository is in Desktop.
```shell
# Move to the directory of the virtual environment
# (often created inside the home directory)
cd ~
# Activate virtual environment
source qiskit/bin/activate
# Move to the directory of the program
cd Desktop/qc-tutorials/qiskit/getting-started
# Open Python interpreter
python
```

Inside the Python Interpreter:

```python
exec(open('getting-started-qiskit.py').read())
```

### Expected output

```
Quantum Circuit
         ┌───┐        ┌─┐
q2_0: |0>┤ H ├──■─────┤M├
         └───┘┌─┴─┐┌─┐└╥┘
q2_1: |0>─────┤ X ├┤M├─╫─
              └───┘└╥┘ ║ 
 c2_0: 0 ═══════════╬══╩═
                    ║    
 c2_1: 0 ═══════════╩════
                         


Available backends for running the circuit:
   qasm_simulator
   statevector_simulator
   unitary_simulator


Running the circuit


Status of the execution:
   RUNNING
   job is actively running


Status of the execution:
   DONE
   job has successfully run


Backend used in the execution:
   qasm_simulator


The results of the simulation are:
{'00': 497, '11': 527}
    State    Counts
    00       497
    11       527

```




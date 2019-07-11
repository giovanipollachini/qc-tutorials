# Ocean SDK

## How to install

### Instructions from Ocean SDK documentation

Instructions: https://docs.ocean.dwavesys.com/en/latest/overview/install.html

### Creating virtual environment in Python
Often different projects require libraries with different versions. The virtual environment is a method to keep controll of the software needed in different projects and avoid conflicts of versions.

```shell
# Move to the directory you want to use to create the virtual environment
# (often created inside the home directory)
cd My/virtual/env/here
# Create virtual environment named "ocean"
virtualenv ocean
# Activate virtual environment
source ocean/bin/activate
```
If you use an older version of python as default, you might need to specify a newer one when creating the virtual environment.
```shell
# Create virtual environment named "ocean" with python version my-python-version
virtualenv ocean --python=my-python-version
```

### Installing Ocean SDK
Once inside a virtual environment, you can install the software via:

```shell
pip install dwave-ocean-sdk
```

## How to run a program on Python interpreter

First you need to activate the virtual environment in which the Ocean SDK is installed.

```shell
# Move to the directory of the virtual environment
# (often created inside the home directory)
cd My/virtual/env/here
# Activate virtual environment
source ocean/bin/activate
```
Next, you need to enter the Python Interpreter from inside the directory of your python program.

```shell
# Move to the directory of the python program
cd getting-started
# Enter the python interpreter
python
```

The following command in python executes the python program and keeps the results and the variables in memory for further use. This behaviour is similar to Matlab, in which you run a .m script and the variables are kept in the workspace, where you can read or use them latter. 

```python
# Run Python program in the interpreter
exec(open('getting-started-ocean-sdk.py').read())
```


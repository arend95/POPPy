Welcome to the Physical OPtics for Python (POPPy) package!

-- PREREQS --\
A fully functioning [Python 3.8](https://docs.python-guide.org/starting/install3/linux/) installation.
If the PIP package manager was not automatically installed with your Python install, it can be installed [manually](https://pip.pypa.io/en/stable/installation/).
Run the following command to install the necessary Python packages:
```
    pip install numpy matplotlib scipy setuptools nose
```
The [g++](https://gcc.gnu.org/install/) compiler, capable of compiling code written in the C++11 standard, and [GNU make](https://www.gnu.org/software/make/). Both can be installed using:
```
    sudo apt-get install gcc build-essential
```

-- TESTING --\
To run the Python unittests, first go to the main POPPy directory and from there:
```
    cd ./tests/Python/
    nosetests
```

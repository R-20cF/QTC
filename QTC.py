# Create the complete teleportation circuit

from qiskit import QuantumCircuit
import numpy as np
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import Sampler
from qiskit.visualization import plot_histogram
from random import randint

# Initialise 3 qubits and 3 cbits
qc = QuantumCircuit(3, 3)

varphi = 0.5
theta = 1.5

# Prepare EPR pair through H and CNOT gates
qc.h(1)
qc.cx(1, 2)
qc.barrier() # For visual separation

# Unitary U is applied to qubit 0 to initialise a random state to be teleported
qc.u(theta, varphi, 0.0, 0)
qc.barrier()

# Entangle qubit 0 with qubit 1
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# 

qc.draw(output='mpl')
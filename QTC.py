# Create the complete teleportation circuit without any Bloch sphere visualisations

from qiskit import QuantumCircuit
import numpy as np
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import Sampler
from qiskit.visualization import plot_histogram
from random import randint

# Initialise 3 qubits and 3 cbits
qc = QuantumCircuit(3, 3)

# Set random values for parameters of U
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

# Measure qubits 0 and 1
qc.measure(0, 0)
qc.measure(1, 1)

# After classical communication, corrections are applied to qubit 2
with qc.if_test((0, 1)):
    qc.z(2)
with qc.if_test((1, 1)):
    qc.x(2)
qc.barrier()

# Verify that the correct state was teleported by applying inverse U
qc.u(theta, varphi, 0.0, 0).inverse()
qc.measure(2, 2)

# Visualise the complete circuit
qc.draw(output='mpl')

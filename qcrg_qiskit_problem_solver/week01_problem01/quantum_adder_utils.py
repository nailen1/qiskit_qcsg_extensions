from qiskit import QuantumCircuit
from qcrg_qiskit_problem_solver.general_utils import simulate_quantum_circuit, get_result_of_simualtion

def set_initial():
    qc = QuantumCircuit(4,2)
    return qc

def set_00():
    qc = QuantumCircuit(4, 2)
    qc.id(0)
    qc.id(1)
    return qc

def set_01():
    qc = QuantumCircuit(4, 2)
    qc.id(0)
    qc.x(1)
    return qc

def set_10():
    qc = QuantumCircuit(4, 2)
    qc.x(0)
    qc.id(1)
    return qc

def set_11():
    qc = QuantumCircuit(4, 2)
    qc.x(0)
    qc.x(1)
    return qc

def set_input_qubits(a=None, b=None, two_qubits=None):
    two_qubits = str(a) + str(b) if a is not None and b is not None else two_qubits
    mappping_two_qubits = {
        '00': set_00,
        '01': set_01,
        '10': set_10,
        '11': set_11
    }
    return mappping_two_qubits[two_qubits]()

def set_f_s(qc):
    qc.cx(0, 2)
    qc.cx(1, 2)
    return qc

# alias
set_two_cnots = set_f_s
set_xor = set_f_s

def set_f_c(qc):
    qc.ccx(0, 1, 3)
    return qc

# alias
set_toffoli = set_f_c
set_and = set_f_c

def set_measure_on_i_and_save_in_j(qc, i, j):
    qubit_index_to_be_measured = i
    classical_register_index_to_be_saved = j
    qc.measure(qubit_index_to_be_measured, classical_register_index_to_be_saved)
    return qc

def set_measure_on_s(qc):
    return set_measure_on_i_and_save_in_j(qc, 2, 0)

def set_measure_on_c(qc):
    return set_measure_on_i_and_save_in_j(qc, 3, 1)


def set_quantum_adder(qc):
    qc = set_f_s(qc)
    qc = set_f_c(qc)
    qc = set_measure_on_s(qc)
    qc = set_measure_on_c(qc)
    return qc

set_the_oracle = set_quantum_adder
set_f = set_quantum_adder

def run_quantum_adder(a=None, b=None, two_qubits=None, shots=1024):
    qc = set_input_qubits(a, b, two_qubits)
    qc = set_f(qc)
    simulation = simulate_quantum_circuit(qc, shots)
    result = get_result_of_simualtion(simulation)
    counts = result.get_counts()
    if a is not None and b is not None and two_qubits is None:
        two_qubits = str(a) + str(b)
    dct = {
        'input_ab': two_qubits,
        'output_counts': counts,  
        'qc': qc    
    }
    return dct

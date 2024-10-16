import itertools
import numpy as np

def get_binary_labels(n):
    num_qubits = int(np.log2(n))
    binary_labels = [''.join(x) for x in itertools.product('01', repeat=num_qubits)]
    return [np.str_(label) for label in binary_labels]
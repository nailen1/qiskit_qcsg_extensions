from qiskit.quantum_info import Statevector
from .utils import get_binary_labels
import pandas as pd
import numpy as np

class Ket:
    def __init__(self, labels=None, create_basis=True):
        self.labels = labels
        self.state = self.create_state(labels)
        self.latex = self.show_latex()
        self.amplitudes = self.get_amplitudes()
        self.probabilities = self.get_probabilities()
        self.basis_label = get_binary_labels(len(self.amplitudes))

        if create_basis:
            self.basis = [Ket(label, create_basis=False) for label in self.basis_label]
        else:
            self.basis = None  

        self.df = self.get_df()

    def create_state(self, labels):
        # Bell state
        if isinstance(labels, tuple) and labels[0] == 'Bell':
            bell_index = labels[1]
            return self.get_bell_state(bell_index)
        
        # n-qubits (e.g. '00', '01', '++')
        elif isinstance(labels, str) and all(char in '01+-' for char in labels):
            return Statevector.from_label(labels)
        
        # single qubit (e.g. '0', '1')
        elif isinstance(labels, str) and len(labels) == 1:
            return Statevector.from_label(labels)
        
        else:
            raise ValueError(f"Invalid input for Ket: {labels}")

    def get_bell_state(self, index):
        if index == 0:
            return self.normalize(Statevector.from_label('00') + Statevector.from_label('11'))
        elif index == 1:
            return self.normalize(Statevector.from_label('00') - Statevector.from_label('11'))
        elif index == 2:
            return self.normalize(Statevector.from_label('01') + Statevector.from_label('10'))
        elif index == 3:
            return self.normalize(Statevector.from_label('01') - Statevector.from_label('10'))
        else:
            raise ValueError(f"Invalid Bell state index: {index}")

    def normalize(self, state):
        norm = np.linalg.norm(state.data)
        return Statevector(state.data / norm)

    def __getattr__(self, name):
        return getattr(self.state, name)

    def show_latex(self):
        return self.state.draw('latex')

    def get_amplitudes(self):
        return self.state.data

    def get_probabilities(self):
        return self.state.probabilities()

    def get_df(self):
        basis = [f'|{base}>' for base in self.basis_label]
        amplitudes = list(self.state.data)
        probabilities = list(self.state.probabilities())
        data = {'basis': basis, 'amplitudes': amplitudes, 'probabilities': probabilities}
        df = pd.DataFrame(data).set_index('basis')
        return df


class Bell(Ket):
    def __init__(self, index):
        super().__init__(labels=('Bell', int(index)), create_basis=True)

import pandas as pd
from qiskit.quantum_info import Statevector
from .utils import get_binary_labels

class Qubit:
    def __init__(self, label, create_basis=True):
        self.label = label
        self.state = Statevector.from_label(label)  # self.state 초기화
        self.latex = self.show_latex()
        self.amplitudes = self.get_amplitudes()
        self.basis_label = get_binary_labels(len(self.amplitudes))
        if create_basis:
            self.basis = self.create_basis()        
        self.probabilities = self.get_probabilities()
        self.df = self.get_df()


    def create_basis(self):
        return [Qubit(label, create_basis=False) for label in self.basis_label]

    def __getattr__(self, name):
        # self.state가 존재하는지 확인한 후 getattr 호출
        if hasattr(self, 'state'):
            return getattr(self.state, name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def show_latex(self):
        return self.state.draw('latex')
    
    def get_amplitudes(self):
        return self.state.data
    
    def get_probabilities(self):
        return self.state.probabilities()
    
    def get_df(self):
        basis = [f'|{base}>' for base in self.basis_label]
        amplitudes = list(self.amplitudes)
        probabilities = list(self.probabilities)
        data = {'basis': basis, 'amplitudes': amplitudes, 'probabilities': probabilities}
        df = pd.DataFrame(data).set_index('basis')
        return df

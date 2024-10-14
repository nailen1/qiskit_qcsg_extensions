from qiskit.quantum_info import Statevector

class Qubit:
    def __init__(self, label):
        self.label = label
        self.state = Statevector.from_label(label)
        self.latex = self.show_latex()
        self.amplitudes = self.get_amplitudes()

    def show_latex(self):
        return self.state.draw('latex')
    
    def get_amplitudes(self):
        return self.state.data
    
    def get_probabilities(self):
        return self.state.probabilities()
    
    def get_info(self):
        return self.state.probabilities_dict()
    
    
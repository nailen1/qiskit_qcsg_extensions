class Operator:
    def __init__(self, num_qubits, data=None):
        self.num_qubits = num_qubits
        self.data = data
        self.matrix = self.get_matrix()
        self.latex = self.show_latex()
        self.eigenvalues = self.get_eigenvalues()
        self.eigenvectors = self.get_eigenvectors()
        self.df = self.get_df()

    def get_matrix(self):
        pass
# qiskit_qcsg_extensions

`qiskit_qcsg_extensions` is a Python library designed to provide an abstraction over [Qiskit](https://qiskit.org/), making it more user-friendly and adhering to standard physics notation. The module simplifies working with quantum states by replacing Qiskit objects and classes with more intuitive representations commonly used in theoretical physics.

## Features

- **Physics-Friendly Notation**: Replace standard Qiskit objects with familiar physics notations, such as `Ket` and `Bra`.
- **User-Friendly Interface**: Simplifies the interaction with quantum states, making it easier to create and manipulate quantum systems.
- **Abstraction Layer**: Wraps around Qiskit’s core functionality for a more intuitive workflow.

## Installation

You can install the module using `pip`:

```bash
pip install qiskit_qcsg_extensions
```

## Usage

Here’s a basic example of how `qiskit_qcsg_extensions` works compared to standard Qiskit:

### Standard Qiskit Usage

```python
from qiskit.quantum_info import Statevector

# Create a quantum state and draw it in LaTeX
state = Statevector.from_label('+')
state.draw('latex')
```

### qiskit_qcsg_extensions Usage

```python
from qiskit_qcsg_extensions import Ket

# Create a quantum state and draw it in LaTeX
ket = Ket('+')
ket.latex
```

With `qiskit_qcsg_extensions`, the user can directly use the `Ket` class, which simplifies the quantum state creation and makes the interaction more aligned with physics notation.

### Examples

#### Single-Qubit State

```python
from qiskit_qcsg_extensions import Ket

# Create a |+⟩ state and display it in LaTeX
ket = Ket('1')
ket.latex
```

#### Multi-Qubit State

```python
# Create a |00⟩ state and display it in LaTeX
ket = Ket('00')
ket.latex
```

#### Bell State

```python
# Create the Bell state |Φ+⟩
bell = Bell(0)
bell.latex
```

## API Reference

- **`Ket(label)`**: Initializes a quantum state based on the provided label (e.g., `Ket('+')`, `Ket('00')`, or `Ket(('Bell', 0))`).
  - **Attributes**:
    - `latex`: Returns the LaTeX representation of the quantum state.
    - `amplitudes`: Accesses the statevector amplitudes.
    - `probabilities`: Computes the probability distribution.
  - **Methods**:
    - `get_df()`: Returns a Pandas DataFrame containing the amplitudes and probabilities.

## Contribution

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Repository

You can find the repository here:

[https://github.com/nailen1/qiskit_qcsg_extensions](https://github.com/nailen1/qiskit_qcsg_extensions)

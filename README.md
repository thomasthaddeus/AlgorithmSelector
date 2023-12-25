# Algorithm Selector

[![Publish to PyPI](https://github.com/thomasthaddeus/AlgorithmSelector/actions/workflows/workflow.yml/badge.svg)](https://github.com/thomasthaddeus/AlgorithmSelector/actions/workflows/workflow.yml) [![PyPI](https://img.shields.io/pypi/v/AlgorithmSelector.svg)](https://pypi.org/project/AlgorithmSelector/)

## Overview

This repository contains a comprehensive collection of algorithms across various domains including computational algorithms, data structures, machine learning, cryptographic methods, and more. Each algorithm is implemented with a focus on clarity, efficiency, and adherence to best practices.

## Table of Contents

- [Algorithm Repository](#algorithm-repository)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Directory Structure](#directory-structure)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To get started with this repository, clone it to your local machine using:

```bash
git clone https://example.com/algorithm-repository.git
cd algorithm-repository
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Each algorithm is encapsulated in its own class and can be used independently. Here's an example of how to use an algorithm from the repository:

```python
from src.data_structures.binary_search_tree import BinarySearchTree

# Example usage
bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
print(bst.search(1))  # Output: True or False
```

## Directory Structure

The repository is organized as follows:

- `src/`: Contains the source code for all algorithms.
  - `computational/`: Computational algorithms like FFT, Monte Carlo, etc.
  - `data_structures/`: Common data structures like AVL Tree, Heap, etc.
  - `ml/`: Machine learning algorithms like k-means, linear regression, etc.
  - `...` (other directories following a similar structure)
- `tests/`: Contains unit tests for each algorithm.
- `docs/`: Documentation related to the algorithms.
- `scripts/`: Useful scripts like setup or build scripts.
- `requirements.txt`: List of dependencies for the project.
- `pyproject.toml`: Project metadata and configuration.

## Testing

To run the tests, navigate to the root directory of the project and run:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions to the repository are welcome! Here's how you can contribute:

1. Fork the repository and create your branch from `main`.
2. Write your algorithm or improvement.
3. Ensure your code passes all existing tests and add new tests if necessary.
4. Submit a pull request.

Please ensure your code adheres to the existing style conventions and add relevant documentation.

## License

This project is licensed under the [MIT License](LICENSE.txt).

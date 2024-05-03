# Algorithm Selector

[![Publish to PyPI][shield1]](https://github.com/thomasthaddeus/AlgorithmSelector/actions/workflows/workflow.yml) [![PyPI][shield2]](https://pypi.org/project/AlgorithmSelector/) ![License][shield3] ![Python Version][shield4] ![Code Size][shield5] ![Last Commit][shield6] ![Issues][shield7] ![Pull Requests][shield8] ![Build Status][shield10] ![Coverage][shield9]

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
  git clone https://github.com/thomasthaddeus/AlgorithmSelector.git
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

This project is licensed under the [MIT License](LICENSE).

<!-- Links in document -->
[shield1]: <https://github.com/thomasthaddeus/AlgorithmSelector/actions/workflows/workflow.yml/badge.svg> "Publish to PyPi Status Shield"
[shield2]: <https://img.shields.io/pypi/v/AlgorithmSelector.svg> "Version of package on PyPI"
[shield3]: <https://img.shields.io/github/license/thomasthaddeus/AlgorithmSelector.svg> "LICENSE Type"
[shield4]: <https://img.shields.io/pypi/pyversions/AlgorithmSelector.svg> "Python versions supported"
[shield5]: <https://img.shields.io/github/languages/code-size/thomasthaddeus/AlgorithmSelector.svg> "Size of the package on PyPI"
[shield6]: <https://img.shields.io/github/last-commit/thomasthaddeus/AlgorithmSelector.svg> "Time of last commit to the repository"
[shield7]: <https://img.shields.io/github/issues-raw/thomasthaddeus/AlgorithmSelector.svg> "Open issues"
[shield8]: <https://img.shields.io/github/issues-pr/thomasthaddeus/AlgorithmSelector.svg> "Open pull requests"
[shield9]: <https://img.shields.io/codecov/c/github/thomasthaddeus/AlgorithmSelector.svg> "Codecov status"
[shield10]: <https://img.shields.io/travis/com/thomasthaddeus/AlgorithmSelector/main.svg> "TravisCI status"

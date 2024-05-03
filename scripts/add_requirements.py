"""add_requirements.py

Module to generate a requirements file from imported libraries in Python
scripts.

_extended_summary_

Returns:
    _type_: _description_
"""

import os
import re

ST_DIR = "../src/"


def find_python_files(start_dir):
    """Recursively find all Python files in the directory."""
    python_files = []
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def extract_imports(file_path):
    """Extract imported libraries from a Python file."""
    with open(file_path, mode="r", encoding="utf-8") as file:
        contents = file.read()
    imports = re.findall(
        r"^\s*(?:import|from)\s+([a-zA-Z0-9_]+)", contents, re.MULTILINE
    )
    return set(imports)


def get_external_libraries(python_files):
    """Get a set of external libraries imported in Python files."""
    try:
        with open("stdlib.txt", encoding="utf-8") as file:
            std_lib = set(file.read().splitlines())
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            "The stdlib.txt file was not found. Please make sure it exists in the root directory."
        ) from exc

    external_libs = set()
    for file in python_files:
        imports = extract_imports(file)
        external_libs.update(imports.difference(std_lib))
    return external_libs


def write_requirements(libraries, filename="requirements.txt"):
    """Write the libraries to the requirements file."""
    with open(filename, "w", encoding="utf-8") as file:
        for lib in sorted(libraries):
            file.write(lib + "\n")


def main():
    """Main function to generate requirements file from Python imports."""
    py_files = find_python_files(ST_DIR)
    ext_libs = get_external_libraries(py_files)
    write_requirements(ext_libs)
    print(f"Requirements file created with {len(ext_libs)} libraries.")


if __name__ == "__main__":
    main()

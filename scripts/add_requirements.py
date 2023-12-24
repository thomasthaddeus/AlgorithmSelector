import os
import re

def find_python_files(start_dir):
    """Recursively find all Python files in the directory."""
    python_files = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def extract_imports(file_path):
    """Extract imported libraries from a Python file."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        contents = file.read()
    imports = re.findall(r'^\s*(?:import|from)\s+([a-zA-Z0-9_]+)', contents, re.MULTILINE)
    return set(imports)

def get_external_libraries(python_files):
    """Get a set of external libraries imported in Python files."""
    std_lib = set(open('stdlib.txt').read().splitlines())  # Assuming a list of standard libraries
    external_libs = set()
    for file in python_files:
        imports = extract_imports(file)
        external_libs.update(imports.difference(std_lib))
    return external_libs

def write_requirements(libraries, filename='requirements.txt'):
    """Write the libraries to the requirements file."""
    with open(filename, 'w') as file:
        for lib in sorted(libraries):
            file.write(lib + '\n')

# Specify the start directory, e.g., 'src'
st_dir = 'src'
py_files = find_python_files(st_dir)
external_libraries = get_external_libraries(py_files)
write_requirements(external_libraries)

print(f"Requirements file created with {len(external_libraries)} libraries.")

#  Importance of Virtual Environment
"""
This script demonstrates the importance of using a virtual environment in Python projects.

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to manage dependencies for different projects separately, avoiding conflicts between them.

Key points:
- Isolate project dependencies
- Avoid version conflicts
- Simplify dependency management
- Facilitate reproducibility

Usage:
1. Create a virtual environment:
    python -m venv <env_name>

2. Activate the virtual environment:
    - On Windows: <env_name>\Scripts\activate
    - On Unix or MacOS: source <env_name>/bin/activate

3. Install dependencies within the virtual environment:
    pip install <package_name>

4. Deactivate the virtual environment when done:
    deactivate
"""
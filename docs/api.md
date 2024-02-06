# API Reference

## Class: DependencyScanner

The `DependencyScanner` class provides functionality to write a set of package names into a requirements file, typically used in Python projects to list all external packages. This document details the API for the `write_requirements` class method within the `DependencyScanner` class.

### Method: write_requirements

Writes the provided set of package names to a `requirements.txt` file, sorted alphabetically.

#### Parameters:

- **packages** (`Set[str]`): A set of package names to be written to the requirements file.
- **file_path** (`str`, optional): The name of the file to write the requirements to. Defaults to `"requirements.txt"`.

#### Returns:

- **None**

#### Description:

This method takes a set of package names and writes them into a specified file, sorted alphabetically. If no filename is specified, 'requirements.txt' is used by default. This functionality is commonly used to create a requirements file for Python projects, listing all external packages that are needed.

The method opens the specified file (or creates it if it does not exist) in write mode, ensuring that the file's content is encoded in UTF-8. It then iterates over the sorted set of package names, writing each one to a new line in the file. After all packages have been written, the file is closed, and a confirmation message is printed to the console indicating the path to the requirements file that was created or updated.

#### Example Usage:

```python
from typing import Set

# Define a set of package names
packages: Set[str] = {"flask", "requests", "numpy"}

# Call the write_requirements class method
DependencyScanner.write_requirements(packages)

# Output: Requirements written to requirements.txt
```

In this example, a set of package names is defined and passed to the `write_requirements` method of the `DependencyScanner` class. The method writes these packages, sorted alphabetically, to a file named `requirements.txt`. If the file already exists, it is overwritten; otherwise, it is created. The method concludes by printing a message indicating that the requirements have been successfully written to the specified file.

The `DependencyScanner` class provides functionality related to dependency scanning and management for Python projects. This document details the API for the `find_pypi_package_name` asynchronous class method within the `DependencyScanner` class.

### Method: find_pypi_package_name

Asynchronously checks if the given package name exists on PyPI (Python Package Index).

#### Parameters:

- **package_name** (`str`): The package name to check.

#### Returns:

- **bool**: `True` if the package exists on PyPI, `False` otherwise.

#### Description:

This method performs an asynchronous HTTP GET request to the PyPI website to check if a package with the specified name exists. It constructs the URL based on the provided package name, targeting the JSON representation of the package on PyPI.

The method uses `aiohttp.ClientSession` to manage the HTTP session, making it suitable for asynchronous execution in an event loop. It awaits the response from the PyPI server and checks the HTTP status code of the response. If the status code is 200 (OK), it indicates that the package exists on PyPI, and the method returns `True`. If the package does not exist or an error occurs (resulting in a different status code), the method returns `False`.

This method is particularly useful for verifying the existence of a package on PyPI before attempting to add it to a project's dependencies or requirements file.

#### Example Usage:

```python
import asyncio
from depscanner import DependencyScanner

async def check_package():
    package_name = "requests"
    exists = await DependencyScanner.find_pypi_package_name(package_name)
    print(f"Package '{package_name}' exists on PyPI: {exists}")

# Run the async function
asyncio.run(check_package())

# Expected output (assuming the package exists):
# Package 'requests' exists on PyPI: True
```

In this example, an asynchronous function `check_package` is defined to check if the "requests" package exists on PyPI using the `find_pypi_package_name` method of the `DependencyScanner` class. The `asyncio.run` function is then used to execute the asynchronous function. The method's result indicates whether the specified package exists on PyPI.

### Method: find_python_files

Recursively finds all Python files (`.py`) in the specified directory and returns their paths.

#### Parameters:

- **directory** (`str`): The directory path to search in.

#### Returns:

- **List[str]**: A list of paths to Python files found within the directory.

#### Description:

This method traverses a given directory recursively, including all subdirectories, to find files that end with the `.py` extension, indicating Python source files. It uses the `os.walk` function to iterate through the directory tree, checking each file to see if it matches the criteria (ends with `.py`). If a file matches, its path is constructed using `os.path.join` to combine the root directory and the file name, ensuring the path is correct regardless of the operating system. These paths are collected in a list, which is returned once the entire directory has been searched.

This functionality is particularly useful for tools and scripts that need to operate on Python source files, such as linters, formatters, or custom analysis tools.

#### Example Usage:

```python
from depscanner import DependencyScanner

# Specify the directory to search in
directory_path = "/path/to/your/project"

# Call the find_python_files class method
python_files = DependencyScanner.find_python_files(directory_path)

# Print the list of found Python file paths
for file_path in python_files:
    print(file_path)

# This will print the paths to all Python files found in the specified directory and its subdirectories.
```

In this example, the `find_python_files` method is used to find all Python files within a specified directory and its subdirectories. The method returns a list of file paths, which are then printed. This can be useful for various purposes, such as batch processing of Python files, analyzing project structure, or automating tasks that involve Python source code.

### Method: extract_imports

Extracts import statements from a specified Python file, filtering out packages that are part of the Python standard library. It specifically looks for lines that begin with 'from' or 'import'.

#### Parameters:

- **file_path** (`str`): The path to the Python file to analyze.
- **python_version** (`str`): The target Python version used to determine which packages are part of the standard library.

#### Returns:

- **Set[str]**: A set of non-standard library package names extracted from the file.

#### Description:

This method analyzes a Python file, searching for import statements to identify dependencies. It uses regular expressions to find lines that match the patterns of import statements, either `import module` or `from module import something`, considering only those that start at the beginning of a line.

The method filters out any imports that are part of the Python standard library for the specified Python version. This filtering is essential for focusing on external dependencies that might need to be included in a project's `requirements.txt` file or installed via a package manager.

To determine what constitutes the standard library for a given Python version, the method relies on the `stdlib_list` function (not shown in the snippet) which should return a set of standard library module names for the specified version.

#### Example Usage:

```python
from depscanner import DependencyScanner

# Specify the path to the Python file and the target Python version
file_path = "/path/to/your/file.py"
python_version = "3.8"

# Call the extract_imports class method
non_std_lib_imports = DependencyScanner.extract_imports(file_path, python_version)

# Print the set of extracted non-standard library imports
print(non_std_lib_imports)

# The output will be a set of package names that are not part of the Python 3.8 standard library.
```

In this example, the `extract_imports` method is used to analyze a Python file, identifying import statements and filtering out those that are part of the Python standard library for the specified version (Python 3.8 in this case). The result is a set of package names that represent external dependencies, which could be further used for dependency management tasks, such as generating a `requirements.txt` file or assessing the project's external dependencies.

### Method: group_files_by_package_name

Groups a list of file paths by their inferred package names.

#### Parameters:

- **files** (`List[str]`): A list of file paths.

#### Returns:

- **Dict[str, List[str]]**: A dictionary where each key is a package name, and its value is a list of files belonging to that package.

#### Description:

This method processes a list of Python file paths, grouping them by their inferred package names into a dictionary. It makes a specific assumption about how to infer the package name from a file path:

- For files named `__init__.py`, it assumes the package name is the name of the parent directory. This convention follows Python's package structure, where `__init__.py` signifies that its directory should be treated as a package.
- For all other files, it assumes the file name (excluding the file extension) is the package name.

This approach allows for a straightforward grouping of Python source files based on their package affiliation, which can be particularly useful for analyzing project structures, generating documentation, or managing dependencies.

#### Example Usage:

```python
from depscanner import DependencyScanner

# List of file paths
files = [
    "/path/to/package1/__init__.py",
    "/path/to/package1/module1.py",
    "/path/to/package2/__init__.py",
    "/path/to/package2/module2.py",
]

# Call the group_files_by_package_name static method
grouped_files = DependencyScanner.group_files_by_package_name(files)

# Print the grouped files
for package_name, file_paths in grouped_files.items():
    print(f"Package: {package_name}")
    for path in file_paths:
        print(f" - {path}")

# The output will display the files grouped by their inferred package names.
```

In this example, the `group_files_by_package_name` method is used to group a list of file paths by their package names based on the method's assumptions. The result is a dictionary mapping package names to lists of file paths belonging to those packages. This can be very useful for organizing files by package for further analysis or processing.

### Method: async_scan_project

Asynchronously scans a project directory to identify Python packages used, distinguishing between project-specific and external packages. It also checks which of the external packages are available on the Python Package Index (PyPI).

#### Parameters:

- **project_directory** (`str`): The path to the project directory to be scanned.
- **python_version** (`str`, optional): The version of Python used in the project. Defaults to `"3.8"`.

#### Returns:

- **Dict[str, Any]**: A dictionary containing information about all identified packages, including those found on PyPI, those not found on PyPI, and project-specific packages grouped by package name.

#### Description:

The `async_scan_project` method performs several key operations:

1. **Finding Python Files**: It first identifies all Python files within the specified project directory.
2. **Grouping Files by Package Name**: It then groups these files by their inferred package names, based on the file and directory structure.
3. **Extracting Imports**: For each Python file, it extracts import statements to identify both external and project-specific packages.
4. **Checking PyPI Availability**: It asynchronously checks the availability of identified external packages on PyPI, differentiating between those that are available and those that are not.

This method is particularly useful for analyzing project dependencies in an efficient, non-blocking manner, making it well-suited for integration into tools that require asynchronous operations, such as web servers or GUI applications that manage or inspect Python projects.

#### Example Usage:

```python
import asyncio
from depscanner import DependencyScanner

async def scan_project():
    project_directory = "/path/to/your/project"
    python_version = "3.8"
    
    # Perform an asynchronous scan of the project
    scan_result = await DependencyScanner.async_scan_project(project_directory, python_version)
    
    # Process the scan results
    print("All Packages:", scan_result['all_package'])
    print("Found in PyPI:", scan_result['found_in_pypi'])
    print("Not Found in PyPI:", scan_result['not_found_in_pypi'])
    print("Project-specific Packages:", scan_result['project_package'])

# Run the asynchronous scan
asyncio.run(scan_project())
```

In this example, the `async_scan_project` method is used to perform an asynchronous analysis of a Python project, identifying both external and project-specific packages. It differentiates between packages that are available on PyPI and those that are not. This method provides a comprehensive overview of a project's dependencies, useful for dependency management, auditing, or integration into development tools and pipelines.

### Method: get_installed_packages

Asynchronously retrieves a list of installed Python packages along with their versions by executing the `pip freeze` command.

#### Returns:

- **List[str]**: A list of strings, each representing an installed package and its version in the format `"package==version"`.

#### Description:

The `get_installed_packages` method provides an asynchronous mechanism to fetch the list of all Python packages currently installed in the environment from which the method is invoked. It does this by running the `pip freeze` command in a subprocess and capturing its output. The method then parses this output, returning a list of package names and their corresponding versions.

This method is particularly useful for applications that need to programmatically determine the current Python environment's state, such as dependency managers, environment inspectors, or automated build and deployment tools.

#### Example Usage:

```python
import asyncio
from depscanner import DependencyScanner

async def list_installed_packages():
    # Get a list of installed packages and their versions
    installed_packages = await DependencyScanner.get_installed_packages()
    
    # Print each installed package
    for package in installed_packages:
        print(package)

# Run the asynchronous task
asyncio.run(list_installed_packages())
```

In this example, the `get_installed_packages` method is used to asynchronously fetch and print a list of all packages installed in the current Python environment, along with their versions. This can be particularly useful for generating reports, auditing environments, or ensuring that necessary dependencies are installed for a project to run correctly.

### Method: get_package_dependencies

Asynchronously retrieves the dependencies of a specified Python package by executing the `pip show` command.

#### Parameters:

- **package_name** (`str`): The name of the package whose dependencies are to be fetched.

#### Returns:

- **List[str]**: A list of strings, each representing the name of a dependency package.

#### Description:

The `get_package_dependencies` method asynchronously executes the `pip show` command for a specified package name to fetch its dependencies. It parses the output to extract the list of dependencies listed under the 'Requires:' section. This method is useful for applications that need to programmatically determine the dependencies of a specific package, such as for dependency resolution, package management tools, or for auditing purposes.

#### Example Usage:

```python
import asyncio
from depscanner import DependencyScanner

async def show_package_dependencies(package_name):
    # Get a list of dependencies for the specified package
    dependencies = await DependencyScanner.get_package_dependencies(package_name)
    
    # Print each dependency
    print(f"Dependencies for {package_name}:")
    for dep in dependencies:
        print(f" - {dep}")

# Specify the package name
package_name = "requests"

# Run the asynchronous task
asyncio.run(show_package_dependencies(package_name))
```

In this example, the `get_package_dependencies` method is used to asynchronously fetch and print the dependencies of the specified package (`requests` in this case). This can be particularly useful for developers and system administrators who need to understand package dependencies for troubleshooting, upgrading, or ensuring compatibility within Python environments.

### Method: analyze_dependencies

Asynchronously analyzes the dependency relationships of all installed Python packages, focusing on identifying primary packages and their dependencies.

#### Returns:

- **Dict[str, List[str]]**: A dictionary where each key is a string representing an installed package (including its version), and its value is a list of strings representing the names of its dependencies.

#### Description:

The `analyze_dependencies` method performs a comprehensive analysis of the Python environment's installed packages. It first retrieves a list of all installed packages with their versions. Then, for each package, it asynchronously fetches its dependencies. The method constructs a dictionary mapping each package to its list of dependencies.

To emphasize primary packages (packages not listed as dependencies of other packages), the method further processes the gathered data. It filters out packages that appear as dependencies, focusing on those that serve as the foundation of the environment.

This method is particularly useful for understanding the dependency graph of a Python environment. It can aid in tasks such as identifying unnecessary dependencies, troubleshooting conflicting dependencies, or optimizing package installations.

#### Example Usage:

```python
import asyncio
from depscanner import DependencyScanner

async def analyze_and_print_dependencies():
    # Analyze dependencies of all installed packages
    primary_packages = await DependencyScanner.analyze_dependencies()
    
    # Print the dependencies of primary packages
    for pkg, deps in primary_packages.items():
        print(f"{pkg} depends on:")
        for dep in deps:
            print(f" - {dep}")
        print("")

# Run the asynchronous analysis
asyncio.run(analyze_and_print_dependencies())
```

In this example, the `analyze_dependencies` method is used to asynchronously fetch and print the dependencies of primary packages installed in the current Python environment. This can be particularly valuable for developers, system administrators, or any individual interested in the maintenance and optimization of Python environments, providing insights into the structure and relationships between installed packages.

### Method: scan_project

Performs a synchronous scan of a Python project's dependencies by serving as a wrapper around an asynchronous scanning method.

#### Parameters:

- **project_directory** (`str`): The path to the directory of the Python project to be scanned.
- **python_version** (`str`, optional): The Python version to consider during the scan. Defaults to `"3.8"`.

#### Returns:

- **Dict[str, Any]**: A dictionary containing the results of the scan. The structure of this dictionary will include keys and values relevant to the scan's findings, such as identified packages, their versions, and their dependencies.

#### Description:

The `scan_project` method provides a convenient synchronous interface to the asynchronous dependency scanning capabilities of the `DependencyScanner` class. It is designed to analyze a specified Python project directory, identifying both external dependencies and project-specific packages. The method takes into account the specified Python version to ensure compatibility and accuracy in the scan results.

This method is particularly useful for applications that require a synchronous approach to dependency scanning, such as CLI tools, scripts, or other scenarios where asynchronous execution may not be feasible or preferred.

#### Example Usage:

```python
from depscanner import DependencyScanner

def main():
    project_directory = "/path/to/your/project"
    python_version = "3.8"
    
    # Perform a synchronous scan of the project
    scan_result = DependencyScanner.scan_project(project_directory, python_version)
    
    # Process and display the scan results
    print("All Packages:", scan_result['all_packages'])
    print("Found in PyPI:", scan_result['found_in_pypi'])
    print("Not Found in PyPI:", scan_result['not_found_in_pypi'])
    print("Project-specific Packages:", scan_result['project_specific_packages'])

if __name__ == "__main__":
    main()
```

In this example, the `scan_project` method is used to perform a synchronous scan of a Python project, identifying its dependencies and categorizing them based on various criteria. This method simplifies the process of analyzing project dependencies, making it accessible for a wide range of applications and use cases.

### Method: scan_pipenv

Conducts a synchronous scan of the current environment managed by pipenv, determining the dependency relationships of all installed packages and returning a dictionary mapping package names (including their versions) to lists of their dependencies.

#### Returns:

- **Dict[str, List[str]]**: A dictionary where each key represents a package name with its version, and the corresponding value is a list of package names (dependencies) that the key package depends on.

#### Description:

The `scan_pipenv` method synchronously scans the current Python environment managed by pipenv to extract and analyze the dependency relationships of all installed packages. It utilizes the `analyze_dependencies` method to obtain the necessary information, providing a simplified interface for users who prefer synchronous execution.

This method is particularly useful for scenarios where a synchronous approach is preferred, such as in scripts, utilities, or environments where asynchronous execution is not feasible or desired.

#### Example Usage:

```python
from depscanner import DependencyScanner

def main():
    # Synchronously scan the current pipenv-managed environment
    dependencies = DependencyScanner.scan_pipenv()
    
    # Process and utilize the dependency information
    for package, deps in dependencies.items():
        print(f"{package} depends on:")
        for dep in deps:
            print(f" - {dep}")

if __name__ == "__main__":
    main()
```

In this example, the `scan_pipenv` method is used to synchronously scan the current pipenv-managed environment, providing clear insights into the dependency relationships of installed packages. This method simplifies the process of understanding and utilizing package dependencies, catering to a wide range of use cases and preferences.
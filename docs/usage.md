# Usage
The `scan_project` method provides a convenient synchronous interface to the asynchronous dependency scanning capabilities of the `DependencyScanner` class. It is designed to analyze a specified Python project directory, identifying both external dependencies and project-specific packages. The method takes into account the specified Python version to ensure compatibility and accuracy in the scan results.

This method is particularly useful for applications that require a synchronous approach to dependency scanning, such as CLI tools, scripts, or other scenarios where asynchronous execution may not be feasible or preferred.

## Example Usage:

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

The `scan_pipenv` method synchronously scans the current Python environment managed by pipenv to extract and analyze the dependency relationships of all installed packages. It utilizes the `analyze_dependencies` method to obtain the necessary information, providing a simplified interface for users who prefer synchronous execution.

This method is particularly useful for scenarios where a synchronous approach is preferred, such as in scripts, utilities, or environments where asynchronous execution is not feasible or desired.

## Example Usage:

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
# FME Python Utilities

A collection of Python scripts that can be used as standalone utilities or as custom transformers within FME (Feature Manipulation Engine). These tools enhance FME's capabilities by providing additional functionality for workflow automation, process monitoring, and data transformation.

## Overview

This repository includes utilities for monitoring system processes, coordinating asynchronous workspaces, and other specialized operations that extend FME's native capabilities. Each script is designed to be easily integrated into FME workspaces while maintaining flexibility for standalone Python usage.

The primary focus is on providing practical solutions for common FME workflow challenges, with emphasis on robustness, configurability, and clear documentation. These tools are particularly valuable for FME power users who need to coordinate complex processing tasks or integrate with external systems.

## Repository Contents

### [process_counter](./process_counter)
A utility for monitoring running processes on a system. This tool is particularly valuable for coordinating asynchronous FME workflows, ensuring all processes have completed before proceeding with subsequent operations.

## Requirements

- FME (tested with version 2020.0 and above)
- Python 3.6+
- Additional libraries as specified in individual script documentation

## Installation

### As Custom Transformer in FME
1. Download the desired Python script
2. Create a new custom transformer in FME
3. Add a PythonCaller transformer to the custom transformer
4. Configure the PythonCaller to use the script

### As Standalone Python Script
1. Download the desired Python script
2. Install required dependencies (specific to each script)
3. Import the necessary modules in your Python environment

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to submit a pull request or open an issue to improve these utilities.

## License

[MIT License](LICENSE)

## Author

[Davood Kazemi]
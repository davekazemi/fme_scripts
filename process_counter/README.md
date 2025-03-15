# check_process.py

## Description
`check_process.py` is a custom FME transformer implemented in Python that monitors the number of running processes on a system. This utility is particularly valuable for coordinating asynchronous FME workflows, ensuring all processes have completed before proceeding with subsequent operations.

## Features
- Monitor specific processes by name (e.g., `fme.exe`)
- Configure checking intervals and timeout periods
- Set threshold for desired process count
- Receive visual and audio notifications when threshold is reached
- Detailed logging of monitoring status

## Implementation
The transformer is implemented as a Python script for FME's PythonCaller transformer, utilizing the `psutil` library for process monitoring and `fmeobjects` for FME integration.

## Requirements
- FME (tested with version 2020.0 and above)
- Python 3.6+
- psutil library (included with standard FME installations)
- Windows OS for native notifications (monitoring works on all platforms)

## Usage
1. Import the custom transformer into your FME workspace
2. Configure parameters according to your workflow needs
3. Connect input/output ports appropriately
4. Use to coordinate asynchronous processing tasks

# FME Hub link
    https://hub.safe.com/publishers/davekazemi/transformers/processcounter

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| Process Name | Name of the process to monitor | `fme.exe` |
| Checking Interval | Frequency of checks in seconds | `5` |
| Timeout | Maximum wait time in seconds | `60` |
| Maximum Allowed Running Process | Target process count threshold | `1` |

## Example Use Cases
- Waiting for multiple asynchronous workspaces to complete
- Coordinating between FME and external processes
- Creating notification systems for batch processing 
- Implementing simple throttling mechanisms

## Installation
1. Download `check_process.py` and use it in pythoncaller or use custom transformer build and published in fme hub https://hub.safe.com/publishers/davekazemi/transformers/processcounter


## License
[Insert your chosen license here]

## Author
[Your name/organization]

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
# File Metadata Manager

A Python utility for managing custom metadata for files using FME (Feature Manipulation Engine). This tool allows you to set, get, and remove custom metadata associated with files.

## Features

- Set and get custom metadata for files
- Support for both key-value pairs and complete metadata objects
- JSON-based metadata storage
- FME integration for batch processing
- Robust error handling and type validation

## Installation

1. Ensure you have FME installed (tested with FME 2022+)
2. Clone this repository to your FME scripts directory
3. Configure your Python environment with required dependencies

Required Python environment paths:
```python
"C:/Program Files/FME"
"C:/Program Files/FME/python"
"C:/Program Files/FME/python311"
"C:/Program Files/FME/fmeobjects/python311"
```

## Usage

### Basic Usage

```python
from main import MetadataManager

# Create a metadata manager instance
metadata_manager = MetadataManager("path/to/your/file")

# Set a single metadata key
metadata_manager.set_custom_metadata_key("author", "John Doe")

# Get a metadata value
author = metadata_manager.get_custom_metadata_key("author")

# Set complete metadata
metadata = {
    "author": "John Doe",
    "created": "2024-03-20",
    "version": "1.0"
}
metadata_manager.set_custom_metadata(metadata)

# Remove metadata
metadata_manager.remove_custom_metadata()
```

### FME Integration

The script can be used within FME Workbench with the following parameters:

- `_Action`: Action to perform
  - "Set Custom Metadata"
  - "Get Custom Metadata"
  - "Remove Custom Metadata"
- `_FilePath`: Path to the target file
- `_MethodType`: Method type
  - "All" (complete metadata)
  - "Justkey" (single key-value pair)
- `_Metadata`: Complete metadata (for "All" method)
- `_SpeceficKey`: Key name (for "Justkey" method)
- `_SpeceficValue`: Value to set (for "Justkey" method)


## Development

### Project Structure

## Functions

### set_custom_metadata(file_path: str, metadata: str | dict)
Sets custom metadata for a specified file.

Parameters:
- `file_path`: Path to the target file
- `metadata`: Metadata to store, can be either a string or dictionary. Dictionaries will be converted to JSON.

### get_custom_metadata(file_path: str, custom_key: str = None)
Retrieves custom metadata from a specified file.

Parameters:
- `file_path`: Path to the target file
- `custom_key`: Optional key to retrieve specific metadata field. If not provided, returns all metadata.

Returns:
- If custom_key is provided: The value for that key, or None if not found
- If custom_key is not provided: The complete metadata dictionary, or None if no metadata exists

## Example Usage

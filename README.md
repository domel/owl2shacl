# OWL2SHACL

A simple Python script for converting OWL ontologies into SHACL shapes. This script allows you to specify input and output formats for greater flexibility.

## Requirements

- Python 3.x
- `rdflib` library (for parsing RDF files)

To install the required libraries, use:

```bash
pip install rdflib
```

## Usage

The script requires the input OWL file as a mandatory argument, with optional arguments for specifying the output file and formats. If no output file is specified, the result will be displayed on the standard output.

### Command Syntax

```bash
python owl2shacl.py [OPTIONS] input_file
```

### Options

```plaintext
-o, --output 
    Specify the output file path. If not provided, the result will be written to the standard output.

-if, --input_format 
    Specify the format of the input OWL file. Supported formats:
        json-ld
        nt (N-Triples)
        turtle (default)
        xml (RDF/XML)

-of, --output_format 
    Specify the format of the output SHACL file. Supported formats:
        json-ld
        nt
        turtle (default)
        xml

### Example

```bash
python owl2shacl.py -if turtle -of turtle examples/ont.ttl -o shapes.ttl
```

### Directory Structure

```plaintext
owl2shacl/
├── owl2shacl.py    # Main Python script
├── examples/
│   └── ont.ttl     # Example OWL ontology
```


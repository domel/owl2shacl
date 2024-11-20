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

The script requires the input OWL file and the output SHACL file as arguments, along with optional format specifications.

### Command Syntax

```bash
python owl2shacl.py [OPTIONS] input_file output_file
```

### Options

- `--input_format`
  Specify the format of the input OWL file. Supported formats:
  - `json-ld`
  - `nt` (N-Triples)
  - `turtle` (default)
  - `xml` (RDF/XML)

- `--output_format`
  Specify the format of the output SHACL file. Supported formats:
  - `json-ld`
  - `nt`
  - `turtle` (default)
  - `xml`

### Example

```bash
python owl2shacl.py --input_format turtle --output_format turtle examples/ont.ttl shapes.ttl
```

### Directory Structure

```plaintext
owl2shacl/
├── owl2shacl.py    # Main Python script
├── examples/
│   └── ont.ttl     # Example OWL ontology
```


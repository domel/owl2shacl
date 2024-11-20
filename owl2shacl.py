import argparse
from rdflib import Graph

def main():
    # List of allowed formats
    allowed_formats = ['json-ld', 'nt', 'turtle', 'xml']

    parser = argparse.ArgumentParser(description='Process an RDF file using a SPARQL CONSTRUCT query.')
    parser.add_argument('input_file', help='Path to the input RDF file')
    parser.add_argument('output_file', help='Path to the output RDF file')
    parser.add_argument('--input_format', default='turtle', choices=allowed_formats, help='Format of the input file (default: turtle)')
    parser.add_argument('--output_format', default='turtle', choices=allowed_formats, help='Format of the output file (default: turtle)')
    args = parser.parse_args()

    # Load the RDF graph from the input file
    g = Graph()
    g.parse(args.input_file, format=args.input_format)

    # Simple and general SPARQL CONSTRUCT query
    query = '''
    CONSTRUCT { ?s ?p ?o }
    WHERE { ?s ?p ?o }
    '''

    # Execute the SPARQL CONSTRUCT query
    results = g.query(query)

    # Get the resulting graph
    output_graph = results.graph

    # Serialize the results to the output file in the chosen format
    output_graph.serialize(destination=args.output_file, format=args.output_format)

if __name__ == "__main__":
    main()


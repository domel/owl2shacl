import argparse
import sys
from rdflib import Graph

def main():
    """
    Process an OWL RDF file using a SPARQL CONSTRUCT query.
    """
    # List of allowed formats
    allowed_formats = ['json-ld', 'nt', 'turtle', 'xml']

    parser = argparse.ArgumentParser(
        description='Process an RDF file using a SPARQL CONSTRUCT query.'
    )
    parser.add_argument(
        'input_file', 
        help='Path to the input RDF file'
    )
    parser.add_argument(
        '-o', '--output', 
        help='Path to the output RDF file (default: standard output)'
    )
    parser.add_argument(
        '-if', '--input_format', 
        default='turtle', 
        choices=allowed_formats, 
        help='Format of the input file (default: turtle)'
    )
    parser.add_argument(
        '-of', '--output_format', 
        default='turtle', 
        choices=allowed_formats, 
        help='Format of the output (default: turtle)'
    )
    args = parser.parse_args()

    # Load the RDF graph from the input file
    g = Graph()
    g.parse(args.input_file, format=args.input_format)

    # SPARQL CONSTRUCT query to retrieve all triples
    query = """
    CONSTRUCT { ?s ?p ?o }
    WHERE { ?s ?p ?o }
    """

    # Execute the SPARQL CONSTRUCT query
    results = g.query(query)

    # Get the resulting graph
    output_graph = results.graph

    # Serialize the results to the output in the chosen format
    if args.output:
        output_graph.serialize(
            destination=args.output, format=args.output_format
        )
    else:
        output_graph.serialize(
            destination=sys.stdout.buffer, format=args.output_format
        )

if __name__ == "__main__":
    main()

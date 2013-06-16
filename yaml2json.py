#!/usr/bin/python
"""
Simple utility to convert between YAML and JSON
"""

import argparse, sys, json
import yaml     # Requires PyYAML


def yaml2json(yamlDoc, indent=2, sort=False):
	yamlObj = yaml.load(yamlDoc)

	return json.dumps(yamlObj, indent=indent, sort_keys=sort)

def json2yaml(jsonDoc, indent=2, sort=False):
	jsonObj = json.loads(jsonDoc)

	return yaml.safe_dump(jsonObj, default_flow_style=False, indent=indent)

def main(args):
	input = sys.stdin.read()
	if input == "":
		sys.stderr.write("ERROR: No input given\n")
		sys.exit(1)

	if args.reverse:
		output = json2yaml(input, sort=args.sort)
	else:
		output = yaml2json(input, sort=args.sort)

	if output == "":
		sys.stderr.write("ERROR: Could not decode input\n")
		sys.exit(2)

	sys.stdout.write(output)
	sys.exit(0)

if __name__ == "__main__":
	# Read commandline args if we're executing as a script
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("-s", "--sort", 
		help="sort keys before output",
		action='store_true', default=False)
	parser.add_argument("--reverse", 
		help="accepts JSON from input and outputs YAML",
		action='store_true', default=False)
	args = parser.parse_args()

	main(args)

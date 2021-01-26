import argparse
from this_argparsl_config import parser_config

parser = argparse.ArgumentParser(**parser_config['parser'])
for argument, details in parser_config['arguments'].items():
    parser.add_argument(*argument, **details)

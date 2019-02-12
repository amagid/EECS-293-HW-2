import argparse
parser = argparse.ArgumentParser()
parser.add_argument('expression', metavar='expression', type=str, help='The expression to parse in string format')
args = parser.parse_args()

__all__ = [
    'abstract_token',
    'cache',
    'connector',
    'internal_node',
    'leaf_node',
    'node',
    'non_terminal_symbol',
    'parse_state',
    'symbol_sequence',
    'symbols',
    'terminal_symbol',
    'tokenclass',
    'variable'
]

def main():
    print(args.expression)
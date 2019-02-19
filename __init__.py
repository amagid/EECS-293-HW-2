import argparse
from utils import _str_to_token_list
from non_terminal_symbol import NonTerminalSymbol

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
    parser = argparse.ArgumentParser()
    parser.add_argument('expression', nargs='?', metavar='expression', type=str, help='The expression to parse in string format')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()

    # Guard against None expression
    if args.expression is None:
        print('No expression supplied')
        return None

    token_list = _str_to_token_list(args.expression)

    node = NonTerminalSymbol.parse_input(token_list)

    if args.verbose and node is not None:
        print(node)
        return node.to_list()
    elif args.verbose:
        print('Invalid Expression.')
        return None
    
    return node.to_list()
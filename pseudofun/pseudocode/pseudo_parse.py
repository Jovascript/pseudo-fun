'''Functions for parsing and executing pseudocode'''
import os

import tatsu
from tatsu.model import ModelBuilderSemantics

from .python_gen import PythonCodeGenerator, PseudoPythonSemantics

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_grammar():
    '''Loads the grammar file'''
    with open(os.path.join(PACKAGE_DIR, 'pseudocode.ebnf')) as f:
        grammar = f.read()
    return grammar

def get_ast(code):
    '''Parses the pseudocode'''
    parser = tatsu.compile(
        load_grammar()
        )
    return parser.parse(code)

def get_model(code):
    '''Gets the auto-generated model for the pseudocode'''
    parser = tatsu.compile(
        load_grammar(),
        semantics=ModelBuilderSemantics()
        )
    return parser.parse(code)

def get_python(code):
    '''Generates python code from the pseudocode'''
    parser = tatsu.compile(
        load_grammar(),
        semantics=PseudoPythonSemantics()
        )
    model = parser.parse(code)
    return PythonCodeGenerator().render(model)

def run(code):
    '''Runs the pseudocode'''
    exec(get_python(code))


def PRINT(*args):
    print(*args)


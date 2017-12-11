
import json
import os

import tatsu
from tatsu.model import ModelBuilderSemantics
from tatsu.util import asjson

from .python_gen import PythonCodeGenerator, PseudoPythonSemantics

package_directory = os.path.dirname(os.path.abspath(__file__))

def load_grammar():
    with open(os.path.join(package_directory, 'pseudocode.ebnf')) as f:
        grammar = f.read()
    return grammar

def get_ast(code):
    parser = tatsu.compile(
        load_grammar()
        )
    return parser.parse(code)

def get_model(code):
    parser = tatsu.compile(
        load_grammar(),
        semantics=ModelBuilderSemantics()
        )
    return parser.parse(code)

def get_python(code):
    parser = tatsu.compile(
        load_grammar(),
        semantics=PseudoPythonSemantics()
        )
    model = parser.parse(code)
    return PythonCodeGenerator().render(model)

def run(code):
    exec(get_python(code))


def PRINT(*args):
    print(*args)


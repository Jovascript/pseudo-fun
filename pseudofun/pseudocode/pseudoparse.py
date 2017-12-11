from tatsu.util import asjson
import tatsu
from tatsu.model import ModelBuilderSemantics

class PseudoSemantics(ModelBuilderSemantics):
    def number(self, ast):
        return float(ast)
    def string(self, ast):
        return ast[1:-1]



# -*- coding: utf-8 -*-
from tatsu.codegen import ModelRenderer
from tatsu.codegen import CodeGenerator
from tatsu.synth import synthesize
from tatsu.semantics import Node
import sys

from tatsu.model import ModelBuilderSemantics

symbol_conversions = {
    'AND': 'and',
    'OR': 'or',
    '<>': '!=',
    '=': '=='
}

class PseudoPythonSemantics(ModelBuilderSemantics):
    def SYMBOL(self, ast):
        if ast in symbol_conversions:
            ast = symbol_conversions[ast]
        return ast
    

THIS_MODULE = sys.modules[__name__]

class PythonCodeGenerator(CodeGenerator):
    def __init__(self):
        super(PythonCodeGenerator, self).__init__(modules=[THIS_MODULE])

class Script(ModelRenderer):
    template = '''{lines::\n:}'''
class Block(ModelRenderer):
    template = '''{lines:1:\n:}'''
class ForStatement(ModelRenderer):
    template = '''\
    for {identifier} in range(int({start}), int({end})+1):
        {body}
    '''

class WhileStatement(ModelRenderer):
    template = '''\
    while {condition}:
        {body}
    '''

class RepeatStatement(ModelRenderer):
    template = '''\
    while True:
        {body}
            if {condition}:
                break
    '''

class ConditionalStatement(ModelRenderer):
    template = '''\
    if {condition}:
        {body}
    '''
class AssignmentStatement(ModelRenderer):
    template = '''\
    {identifier} = {expression}'''

class Identifier(ModelRenderer):
    template = '''\
    {name}'''

class SumExpression(ModelRenderer):
    template = '''\
    {left} {operator} {right}\
    '''

class BracketedExpression(ModelRenderer):
    template = '''\
    ({expression})\
    '''

class FunctionCall(ModelRenderer):
    template = '''\
    {name}{arguments}'''

class ArgumentList(ModelRenderer):
    template = '''({arguments::,:})'''

class FunctionDef(ModelRenderer):
    template = '''\
    def {name}{arguments}:
        {body}
    '''
class ReturnStatement(ModelRenderer):
    template = '''return {expression}'''

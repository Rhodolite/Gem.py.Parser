#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Priority')
def module():
    share(
        'PRIORITY_ATOM',                     1,     #   atom
        'PRIORITY_TUPLE',                    2,     #   tuple
        'PRIORITY_POSTFIX',                  3,     #   . () and []
        'PRIORITY_POWER',                    4,     #   **
        'PRIORITY_UNARY',                    5,     #   unary '+', '-', '~'
        'PRIORITY_MULTIPLY',                 6,     #   *
        'PRIORITY_ARITHMETIC',               7,     #   +
        'PRIORITY_SHIFT',                    8,     #   << and >>
        'PRIORITY_LOGICAL_AND',              9,     #   &
        'PRIORITY_LOGICAL_EXCLUSIVE_OR',    10,     #   ^
        'PRIORITY_LOGICAL_OR',              11,     #   |
        'PRIORITY_NORMAL_LIST',             12,     #   Comma expression of PRIORITY_LOGICAL_OR
        'PRIORITY_COMPARE',                 13,     #   ==
        'PRIORITY_NOT',                     14,     #   not
        'PRIORITY_BOOLEAN_AND',             15,     #   'and'
        'PRIORITY_BOOLEAN_OR',              16,     #   'or'
        'PRIORITY_LAMBDA',                  17,     #   'lambda'
        'PRIORITY_TERNARY',                 18,     #   'if'
        'PRIORITY_TERNARY_LIST',            19,     #   Comma expression of PRIORITY_TERNARY
        'PRIORITY_SUBSCRIPT',               20,     #   Subscript of index expression
        'PRIORITY_SUBSCRIPT_LIST',          21,     #   Comma expresion of Subscripts
        'PRIORITY_MAP_ELEMENT',             22,     #   ':'
        'PRIORITY_MAP_LIST',                23,     #   Comma expression of ':'
        'PRIORITY_YIELD',                   24,     #   'yield'
        'PRIORITY_COMPREHENSION',           25,     #   'for' inside '()'
        'PRIORITY_ASSIGN',                  26,     #   '=',
        'PRIORITY_AS',                      27,     #   'as'
        'PRIORITY_AS_LIST',                 28,     #   Comma expression of 'as'
        'PRIORITY_STATEMENT',               29,     #   statement

        #
        #   PRIORITY_NORMAL is an alias for PRIORITY_LOGICAL_OR
        #
        'PRIORITY_NORMAL',                  11,
    )

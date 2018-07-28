#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.QuadrupleStatement')
def module():
    class QuadrupleStatement(QuadrupleTwig):
        __slots__                  = (())
        display_name               = 'quadruple-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
                t.a.dump_token(f)
                t.b.dump_token(f)
                t.c.dump_token(f)
                t.d.dump_token(f)


        def find_require_module(t, e):
            t.a.find_require_module(e)
            t.b.find_require_module(e)
            t.c.find_require_module(e)
            t.d.find_require_module(e)


        indentation     = indentation__a_indentation
        scout_variables = scout_variables__abcd


    conjure_quadruple_statement = produce_conjure_quadruple_twig('quadruple-statement', QuadrupleStatement)


    #
    #   .transform
    #
    QuadrupleStatement.transform = produce_transform__abcd('quadruple-statement', conjure_quadruple_statement)


    share(
        'conjure_quadruple_statement',  conjure_quadruple_statement,
    )

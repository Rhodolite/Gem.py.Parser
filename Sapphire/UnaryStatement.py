#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.UnaryStatement')
def gem():
    require_gem('Sapphire.UnaryExpression')


    class ElseStatement(UnaryExpression):
        __slots__    = (())
        display_name = 'else-statement'
        frill        = conjure_indented_else_colon(
                           empty_indentation,
                           conjure_keyword_else('else'),
                           conjure_colon(': '),
                       )

        is_any_else_header  = false
        is_else_header      = false
        is_statement        = true
        is_statement_header = false


        def display_token__frill(t):
            frill = t.frill

            return arrange('<else-statement+frill +%d %s %s %s>',
                           frill.a.total,
                           frill.b.display_token(),
                           frill.c.display_token(),
                           t.a.display_token())


        @property
        def indentation(t):
            return t.frill.a


    del Shared.conjure_indented_else_colon


    conjure_else_statement = produce_conjure_unary_expression('else-statement', ElseStatement)


    share(
        'conjure_else_statement',   conjure_else_statement,
    )

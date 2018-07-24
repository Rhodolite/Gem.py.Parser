#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.BookcaseStatement')
def gem():
    class ExpressionStatement(BookcaseExpression):
        __slots__                  = (())
        display_name               = 'expression-statement'
        frill                      = conjure_vw_frill(empty_indentation, LINE_MARKER)
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return conjure_expression_statement__with_frill(
                       conjure_commented_vw_frill(comment, frill.v, frill.w),
                       t.a,
                   )


        def display_token(t):
            return arrange('<expression-statement +%d %s>', t.frill.v.total, t.a.display_token())


        def display_token__frill(t):
            frill = t.frill

            return arrange('<expression-statement+frill +%d %s %s>',
                           frill.v.total,
                           t.a    .display_token(),
                           frill.w.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.v.total)
                t.a        .dump_token(f)
                r = frill.w.dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d', t.display_name, frill.v.total), '>'):
                comment.dump_token(f)
                t.a    .dump_token(f)
                frill.w.dump_token(f)


        find_require_gem = find_require_gem__0


        @property
        def indentation(t):
            return t.frill.v


        scout_variables = scout_variables__a


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)


    [
        conjure_expression_statement, conjure_expression_statement__with_frill,
    ] = produce_conjure_bookcase_expression('expression-statement', ExpressionStatement)


    #
    #   .transform
    #
    ExpressionStatement.transform = produce_transform__frill__a_with_priority(
                                        'expression_statement',
                                        PRIORITY_TERNARY_LIST,
                                        conjure_expression_statement__with_frill,
                                    )


    share(
        'conjure_expression_statement',     conjure_expression_statement,
    )

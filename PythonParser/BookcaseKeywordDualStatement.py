#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.BookcaseKeywordDualStatement')
def gem():
    require_gem('PythonParser.BookcaseDualExpression')


    class KeywordDualExpressionStatement(BookcaseDualExpression):
        __slots__ = (())


        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.v.a.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill = t.frill

            indented_keyword = frill.v

            return arrange('<%s+frill +%d %s %s %s %s %s>',
                           t.display_name,
                           indented_keyword.a.total,
                           indented_keyword.b.display_token(),
                           t               .a.display_token(),
                           frill           .w.display_token(),
                           t               .b.display_token(),
                           frill           .x.display_token())


        def dump_token(t, f, newline = true):
            frill            = t.frill
            indented_keyword = frill.v

            f.partial('<%s +%d ', t.display_name, indented_keyword.a.total)

            indented_keyword.b.dump_token(f)
            t               .a.dump_token(f)
            frill           .w.dump_token(f)
            t               .b.dump_token(f)
            r = frill       .x.dump_token(f, false)

            return f.token_result(r, newline)


        @property
        def indentation(t):
            return t.frill.v.a


    class AssertStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'assert-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_assert('assert ')),
                           COMMA__W,
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__ab


    @share
    class ExceptHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'except-header-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           conjure_keyword_as(' as '),
                           COLON__LINE_MARKER,
                       )

        is_any_except_or_finally = true
        is_statement             = false
        is_statement_header      = true
        split_comment            = 0

        add_comment     = 0
        scout_variables = scout_variables__a__b_with_write


    @share
    class ForHeader(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'for-header'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, FOR__W),
                           W__IN__W,
                           LINE_MARKER,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 1

        add_comment     = 0
        scout_variables = scout_variables__a_with_write__b


    class FromImportStatement(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'from-statement'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_from('from ')),
                           conjure_keyword_import(' import '),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


        def scout_variables(t, art):
            #
            #   Nothing to do with t.a, as does not access variables
            #
            t.b.write_variables(art)


        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.morph (vary, 0, PRIORITY_AS_LIST, 0)
            a__2     = a    .mutate(vary, PRIORITY_POSTFIX)
            b__2     = b    .mutate(vary, PRIORITY_NORMAL_LIST)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return t.conjure_with_frill(frill__2, a__2, b__2)


    class RaiseStatement_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'raise-statement-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           COMMA__W,
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__ab


    @share
    class WithHeader_2(KeywordDualExpressionStatement):
        __slots__    = (())
        display_name = 'with-header-2'
        frill        = conjure_vwx_frill(
                           conjure_indented_token(empty_indentation, WITH__W),
                           W__AS__W,
                           COLON__LINE_MARKER,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 1

        add_comment     = 0
        scout_variables = scout_variables__a__b_with_write


    [
        conjure_assert_statement_2, conjure_assert_statement_2__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'assert-statement-2',
            AssertStatement_2,

            produce_conjure_with_frill = 1,
        )


    [
        conjure_except_header_2, conjure_except_header_2__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'except-header2',
            ExceptHeader_2,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_for_header, conjure_for_header__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'for-header',
            ForHeader,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_from_statement, FromImportStatement.conjure_with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'from-statement',
            FromImportStatement,

            produce_conjure_with_frill = true,
        )

    conjure_raise_statement_2  = produce_conjure_bookcase_dual_expression('raise-statement-2',  RaiseStatement_2)

    [
        conjure_with_header_2, conjure_with_header_2__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'with-header-2',
            WithHeader_2,

            produce_conjure_with_frill = 1,
        )


    AssertStatement_2.transform = produce_transform__frill__ab_with_priority(
                                      'assert_statement_2',
                                      PRIORITY_TERNARY,
                                      PRIORITY_TERNARY,
                                      conjure_assert_statement_2__with_frill,
                                  )

    ExceptHeader_2.transform = produce_transform__frill__ab_with_priority(
                                   'except_header_2',
                                   PRIORITY_TERNARY,
                                   PRIORITY_ASSIGN,
                                   conjure_except_header_2__with_frill,
                                )


    ForHeader.transform = produce_transform__frill__ab_with_priority(
                              'for_header',
                              PRIORITY_NORMAL_LIST,
                              PRIORITY_ASSIGN,
                              conjure_for_header__with_frill,
                         )

    WithHeader_2.transform = produce_transform__frill__ab_with_priority(
                                 'with_header_2',
                                 PRIORITY_TERNARY,
                                 PRIORITY_ASSIGN,
                                 conjure_with_header_2__with_frill,
                            )


    share(
        'conjure_assert_statement_2',   conjure_assert_statement_2,
        'conjure_except_header_2',      conjure_except_header_2,
        'conjure_for_header',           conjure_for_header,
        'conjure_from_statement',       conjure_from_statement,
        'conjure_raise_statement_2',    conjure_raise_statement_2,
        'conjure_with_header_2',        conjure_with_header_2,
    )

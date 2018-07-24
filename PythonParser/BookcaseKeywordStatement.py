#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.BookcaseKeywordStatement')
def gem():
    empty_indentation__at_sign = conjure_indented_token(empty_indentation, conjure_at_sign('@'))


    def produce_add_comment(name, conjure_with_frill = 0):
        @rename('add_comment__%s', name)
        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return ((conjure_with_frill) or (t.conjure_with_frill))(
                       conjure_commented_vw_frill(comment, frill.v, frill.w),
                       t.a,
                   )

        return add_comment



    class KeywordExpressionStatement(BookcaseExpression):
        __slots__                  = (())
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        add_comment = produce_add_comment('keyword-expression-statement')


        def display_token(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s +%d%s %s>',
                           t.display_name,
                           frill.v.indentation.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           t.a.display_token())


        def display_token__frill(t):
            frill          = t.frill
            comment        = frill.comment
            indented_token = frill.v

            return arrange('<%s+frill +%d%s %s %s %s>',
                           t.display_name,
                           indented_token.indentation.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           indented_token.token.display_token(),
                           t.a                 .display_token(),
                           frill.w             .display_token())


        def dump_token(t, f, newline = true):
            assert newline is true

            frill          = t.frill
            comment        = frill.comment
            indented_token = frill.v

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, indented_token.indentation.total)

                indented_token.token.dump_token(f)
                t             .a    .dump_token(f)
                r = frill     .w    .dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d ', t.display_name, indented_token.indentation.total), '>'):
                comment             .dump_token(f)
                indented_token.token.dump_token(f)
                t             .a    .dump_token(f)
                frill         .w    .dump_token(f, false)

            return false


        @property
        def indentation(t):
            return t.frill.v.indentation


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)


    class AssertStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'assert-1'
        frill        = conjure_vw_frill(empty_indentation__at_sign, LINE_MARKER)

        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__a


    @share
    class DecoratorHeader(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = '@-header'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, AT_SIGN),
                           LINE_MARKER,
                       )

        is_class_decorator_or_function_header = true
        is_decorator_header                   = true
        is_statement                          = false
        is_statement_header                   = true
        split_comment                         = 1

        add_comment     = 0
        scout_variables = scout_variables__a


    class DeleteStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'delete-statement-1'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_delete('del ')),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


        def scout_variables(t, art):
            t.a.write_variables(art)


    @export
    class ElseIfHeader(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'else-if-header'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_else_if('elif ')),
                           COLON__LINE_MARKER,
                       )

        is_any_else         = true
        is_statement        = false
        is_statement_header = true
        split_comment       = 0

        add_comment     = 0
        scout_variables = scout_variables__a


    @share
    class ExceptHeader_1(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'except-header-1'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_except('except ')),
                           COLON__LINE_MARKER,
                       )

        is_any_except_or_finally = true
        is_statement             = false
        is_statement_header      = true
        split_comment            = 0

        add_comment     = 0
        scout_variables = scout_variables__a


    @share
    class IfHeader(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'if-header'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, IF__W),
                           LINE_MARKER,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 0

        add_comment     = 0
        scout_variables = scout_variables__a


    class ImportStatement(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'import-statement'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_import('import ')),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0


        def scout_variables(t, art):
            t.a.write_import(art)


    class RaiseStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'raise-statement'
        frill        = conjure_vw_frill(
                           conjure_indented_token(conjure_indentation('    '), RAISE__W),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__a


    class ReturnStatement(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'return-statement'
        frill        = conjure_vw_frill(
                           conjure_indented_token(conjure_indentation('    '), RETURN__W),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__a


    @export
    class WhileHeader(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'while-header'
        frill        = conjure_vw_frill(
                           conjure_indented_token(conjure_indentation('    '), WHILE__W),
                           COLON__LINE_MARKER,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 0

        add_comment     = 0
        scout_variables = scout_variables__a


    @share
    class WithHeader_1(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'with-header-1'
        frill        = conjure_vw_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('with ')),
                           COLON__LINE_MARKER,
                       )

        is_statement        = false
        is_statement_header = true
        split_comment       = 1

        add_comment     = 0
        scout_variables = scout_variables__a


    class YieldStatement_1(KeywordExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'yield-statement-1'
        frill        = conjure_vw_frill(
                           conjure_indented_token(conjure_indentation('    '), YIELD__W),
                           LINE_MARKER,
                       )

        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__a


    [
        conjure_assert_statement_1, conjure_assert_statement_1__with_frill,
    ] = produce_conjure_bookcase_expression('assert-statement-1', AssertStatement_1)

    [
        conjure_decorator_header, conjure_decorator_header__with_frill,
    ] = produce_conjure_bookcase_expression('decorator-header', DecoratorHeader)

    [
        conjure_delete_header, conjure_delete_statement_1__with_frill,
    ] = produce_conjure_bookcase_expression('delete-header', DeleteStatement_1)
    [
        conjure_else_if_header, conjure_else_if_header__with_frill,
    ] = produce_conjure_bookcase_expression('else-if-header', ElseIfHeader)

    [
        conjure_except_header_1, conjure_except_header_1__with_frill,
    ] = produce_conjure_bookcase_expression('except-header-1', ExceptHeader_1)

    [
        conjure_if_header, conjure_if_header__with_frill,
    ] = produce_conjure_bookcase_expression('if-header', IfHeader)

    [
        conjure_import_statement, conjure_import_statement__with_frill,
    ] = produce_conjure_bookcase_expression('import-statement', ImportStatement)

    [
        conjure_raise_statement_1, conjure_raise_statement_1__with_frill,
    ] = produce_conjure_bookcase_expression('raise-statement-1', RaiseStatement_1)

    [
        conjure_return_statement, conjure_return_statement__with_frill,
    ] = produce_conjure_bookcase_expression('return-statement', ReturnStatement)

    [
        conjure_while_header, conjure_while_header__with_frill,
    ] = produce_conjure_bookcase_expression('while-header', WhileHeader)

    [
        conjure_with_header_1, conjure_with_header_1__with_frill,
    ] = produce_conjure_bookcase_expression('with-header-1', WithHeader_1)

    [
        conjure_yield_statement_1, conjure_yield_statement_1__with_frill,
    ] = produce_conjure_bookcase_expression('yield-statement-1', YieldStatement_1)


    #
    #   .add_comment
    #
    AssertStatement_1.add_comment = produce_add_comment('assert_statement_1', conjure_assert_statement_1__with_frill)
    DeleteStatement_1.add_comment = produce_add_comment('delete_statement_1', conjure_delete_statement_1__with_frill)
    ImportStatement  .add_comment = produce_add_comment('import_statement',   conjure_import_statement__with_frill)
    RaiseStatement_1 .add_comment = produce_add_comment('raise_statement_1',  conjure_raise_statement_1__with_frill)
    ReturnStatement  .add_comment = produce_add_comment('return_statement',   conjure_return_statement__with_frill)
    YieldStatement_1 .add_comment = produce_add_comment('yield_statement_1',  conjure_yield_statement_1__with_frill)


    #
    #   .transform
    #
    AssertStatement_1.transform = produce_transform__frill__a_with_priority(
                                      'assert-1',
                                      PRIORITY_TERNARY,
                                      conjure_assert_statement_1__with_frill,
                                  )

    DecoratorHeader.transform = produce_transform__frill__a_with_priority(
                                    'decorator_header',
                                    PRIORITY_POSTFIX,
                                    conjure_decorator_header__with_frill,
                                )

    DeleteStatement_1.transform = produce_transform__frill__a_with_priority(
                                      'assert-1',
                                      PRIORITY_NORMAL,
                                      conjure_delete_statement_1__with_frill,
                                  )

    ElseIfHeader.transform = produce_transform__frill__a_with_priority(
                                 'else_if_header',
                                 PRIORITY_TERNARY,
                                 conjure_else_if_header__with_frill,
                             )

    ExceptHeader_1.transform = produce_transform__frill__a_with_priority(
                                   'except_header_1',
                                   PRIORITY_TERNARY,
                                   conjure_except_header_1__with_frill,
                               )

    IfHeader.transform = produce_transform__frill__a_with_priority(
                             'if_header',
                             PRIORITY_TERNARY,
                             conjure_if_header__with_frill,
                         )

    ImportStatement.transform = produce_transform__frill__a_with_priority(
                                    'import_statement',
                                    PRIORITY_AS_LIST,
                                    conjure_import_statement__with_frill,
                                )

    RaiseStatement_1.transform = produce_transform__frill__a_with_priority(
                                    'raise_statement_1',
                                    PRIORITY_TERNARY,
                                    conjure_raise_statement_1__with_frill,
                                )

    ReturnStatement.transform = produce_transform__frill__a_with_priority(
                                    'return_statement',
                                    PRIORITY_TERNARY_LIST,
                                    conjure_return_statement__with_frill,
                                )

    WhileHeader.transform = produce_transform__frill__a_with_priority(
                                'while_header',
                                PRIORITY_TERNARY,
                                conjure_while_header__with_frill,
                            )

    WithHeader_1.transform = produce_transform__frill__a_with_priority(
                                 'with_header_1',
                                 PRIORITY_AS_LIST,
                                 conjure_with_header_1__with_frill,
                             )

    YieldStatement_1.transform = produce_transform__frill__a_with_priority(
                                     'yield_statement_1',
                                     PRIORITY_TERNARY,
                                     conjure_yield_statement_1__with_frill,
                                 )


    share(
        'conjure_assert_statement_1',       conjure_assert_statement_1,
        'conjure_decorator_header',         conjure_decorator_header,
        'conjure_delete_header',            conjure_delete_header,
        'conjure_else_if_header',           conjure_else_if_header,
        'conjure_except_header_1',          conjure_except_header_1,
        'conjure_if_header',                conjure_if_header,
        'conjure_import_statement',         conjure_import_statement,
        'conjure_raise_statement_1',        conjure_raise_statement_1,
        'conjure_return_statement',         conjure_return_statement,
        'conjure_while_header',             conjure_while_header,
        'conjure_with_header_1',            conjure_with_header_1,
        'conjure_yield_statement_1',        conjure_yield_statement_1,
        'empty_indentation__at_sign',       empty_indentation__at_sign,
    )

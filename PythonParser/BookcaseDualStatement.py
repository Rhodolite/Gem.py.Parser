#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.BookcaseDualStatement')
def gem():
    def produce_add_comment(name, conjure_with_frill):
        @rename('add_comment__%s', name)
        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return conjure_with_frill(
                       conjure_commented_vwx_frill(comment, frill.v, frill.w, frill.x),
                       t.a,
                       t.b,
                   )


        return add_comment


    class DualExpressionStatement(BookcaseDualTwig):
        __slots__ = (())


        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def display_token(t):
            return arrange('<%s +%d %s %s>',
                           t.display_name,
                           t.frill.v.total,
                           t.a    .display_token(),
                           t.b    .display_token())


        def display_token__frill(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s+frill +%d%s %s %s %s %s>',
                           t.display_name,
                           frill.v.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           t.a    .display_token(),
                           frill.w.display_token(),
                           t.b    .display_token(),
                           frill.x.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.v.total)

                t        .a.dump_token(f)
                frill    .w.dump_token(f)
                t        .b.dump_token(f)
                r = frill.x.dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d ', t.display_name, frill.v.total), '>'):
                comment  .dump_token(f)
                t      .a.dump_token(f)
                frill  .w.dump_token(f)
                t      .b.dump_token(f)
                frill  .x.dump_token(f)

            return false



        @property
        def indentation(t):
            return t.frill.v


        def scout_variables(t, art):
            t.a.write_variables(art)
            t.b.scout_variables(art)


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)


    class AssignStatement_1(DualExpressionStatement):
        __slots__        = (())
        class_order      = CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION
        display_name     = 'assign-1'
        frill            = conjure_vwx_frill(empty_indentation, W__ASSIGN__W, LINE_MARKER)


        find_require_gem = find_require_gem__0
        scout_variables  = scout_variables__a_with_write__b


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION
        display_name = 'modify-statement'
        frill        = conjure_vwx_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           LINE_MARKER,
                       )

        scout_variables  = scout_variables__a_with_write__b
        find_require_gem = find_require_gem__0


    [
            conjure_assign_1, AssignStatement_1.conjure_plain, conjure_assign_1__with_frill,
    ] = produce_conjure_bookcase_dual_twig(
            'assign-1',
            AssignStatement_1,

            produce_conjure_plain = true,
        )

    [
            conjure_modify_statement, conjure_modify_statement__with_frill,
    ] = produce_conjure_bookcase_dual_twig('modify-statement', ModifyStatement)

    AssignStatement_1.add_comment = produce_add_comment('assign_statement_1', conjure_assign_1__with_frill)

    AssignStatement_1.transform = produce_transform__frill__ab_with_priority(
                                      'assign_statement_1',
                                      PRIORITY_TERNARY_LIST,
                                      PRIORITY_YIELD,
                                      conjure_assign_1__with_frill,
                                  )

    ModifyStatement.transform = produce_transform__frill__ab_with_priority(
                                    'modify_statement_1',
                                    PRIORITY_TERNARY_LIST,
                                    PRIORITY_YIELD,
                                    conjure_modify_statement__with_frill,
                                )


    share(
        'conjure_assign_1',             conjure_assign_1,
        'conjure_modify_statement',     conjure_modify_statement,
    )

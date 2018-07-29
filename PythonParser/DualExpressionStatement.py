#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.DualExpressionStatement')
def module():
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


    class AssignStatement_1(DualExpressionStatement):
        __slots__    = (())
        display_name = 'assign-1'
        frill        = conjure_vwx_frill(empty_indentation, W__ASSIGN__W, LINE_MARKER)


        find_require_module = find_require_module__0
        scout_variables     = scout_variables__a_with_write__b


    class ModifyStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'modify-statement'
        frill        = conjure_vwx_frill(
                           empty_indentation,
                           conjure_action_word('+=', ' += '),
                           LINE_MARKER,
                       )

        scout_variables     = scout_variables__a_with_write__b
        find_require_module = find_require_module__0


    [
            conjure_assign_1, AssignStatement_1.conjure_plain, conjure_assign_1__with_frill,
    ] = produce_dual_expression_statement(
            'assign-1',
            AssignStatement_1,

            produce_conjure_plain = true,
        )

    [
            conjure_modify_statement, conjure_modify_statement__with_frill,
    ] = produce_dual_expression_statement('modify-statement', ModifyStatement)

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

#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.PostfixExpression')
def module():
    class CallExpression(DualTwig):
        __slots__          = (())
        class_order        = CLASS_ORDER__DUAL_TWIG
        display_name       = 'call'
        is_call_expression = true

        scout_variables = scout_variables__ab


    class IndexExpression(DualTwig):
        __slots__    = (())
        class_order  = CLASS_ORDER__DUAL_TWIG
        display_name = 'index'

        scout_variables = scout_variables__ab


        def write_variables(t, art):
            t.a.scout_variables(art)
            t.b.scout_variables(art)


    class MethodCallExpression(DualTwig):
        __slots__    = (())
        class_order  = CLASS_ORDER__DUAL_TWIG
        display_name = 'method-call'

        scout_variables = scout_variables__ab


    conjure_call_expression        = produce_conjure_dual_twig('call',        CallExpression)
    conjure_index_expression       = produce_conjure_dual_twig('index',       IndexExpression)
    conjure_method_call_expression = produce_conjure_dual_twig('call-method', MethodCallExpression)


    CallExpression.mutate = produce__mutate__ab__priority(
                                'postfix-expression',
                                conjure_call_expression,
                                PRIORITY_POSTFIX,
                                PRIORITY_COMPREHENSION,
                            )

    IndexExpression.mutate = produce__mutate__ab__priority(
                                 'index-expression',
                                 conjure_index_expression,
                                 PRIORITY_POSTFIX,
                                 PRIORITY_SUBSCRIPT_LIST,
                             )

    MethodCallExpression.mutate = produce__mutate__ab__priority(
                                      'postfix-expression',
                                      conjure_method_call_expression,
                                      PRIORITY_POSTFIX,
                                      PRIORITY_COMPREHENSION,
                                  )

    share(
        'conjure_call_expression',          conjure_call_expression,
        'conjure_index_expression',         conjure_index_expression,
        'conjure_method_call_expression',   conjure_method_call_expression,
    )

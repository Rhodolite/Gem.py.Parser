#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.ClassOrder')
def gem():
    export(
        'CLASS_ORDER__ARGUMENT_0',                      30,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                    31,     #   Parameters_0 token

        'CLASS_ORDER__FRILL_MANY',                      41,     #   Frill_Many
        'CLASS_ORDER__BOOKCASE_MANY_FRILL',             42,     #   BookcaseManyFrill

        'CLASS_ORDER__BINARY_EXPRESSION',               50,     #   * expression
        'CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION',        51,     #   BookcaseDualExpression+
        'CLASS_ORDER__BOOKCASE_EXPRESSION',             52,     #   BookcaseExpression+
        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',        53,     #   BookcaseManyExpression+
        'CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION',      54,     #   BookcaseTripleExpression+
        'CLASS_ORDER__CALL_STATEMENT',                  55,     #   CallStatementBase+
        'CLASS_ORDER__DEFINITION_HEADER',               56,     #   DefinitionHeader+
        'CLASS_ORDER__DUAL_TWIG',                       57,     #   DualTwig
        'CLASS_ORDER__MANY_EXPRESSION',                 58,     #   + expression
        'CLASS_ORDER__MEMBER_EXPRESSION',               59,     #   Member expression
        'CLASS_ORDER__QUADRUPLE_TWIG',                  60,     #   Commented_VWX_Frill & VWXY_Frill
        'CLASS_ORDER__TRIPLE_EXPRESSION',               61,     #   ?: expression
        'CLASS_ORDER__TUPLE',                           62,     #   Tuple of expressions
        'CLASS_ORDER__UNARY_EXPRESSION',                63,     #   * expression
    )


    assert CLASS_ORDER__PYTHON_START == CLASS_ORDER__ARGUMENT_0
    assert CLASS_ORDER__UNARY_EXPRESSION < CLASS_ORDER__PYTHON_END


    del Shared.CLASS_ORDER__PYTHON_START
    del Shared.CLASS_ORDER__PYTHON_END

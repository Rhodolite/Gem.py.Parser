#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ClassOrder')
def module():
    export(
        'CLASS_ORDER__ARGUMENT_0',                              40,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                            41,     #   Parameters_0 token

        'CLASS_ORDER__FRILL_MANY',                              51,     #   Frill_Many
        'CLASS_ORDER__BOOKCASE_MANY_FRILL',                     52,     #   BookcaseManyFrill

        'CLASS_ORDER__BINARY_EXPRESSION',                       60,     #   * expression
        'CLASS_ORDER__BOOKCASE_EXPRESSION',                     61,     #   BookcaseExpression+
        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',                62,     #   BookcaseManyExpression+
        'CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION',              63,     #   BookcaseTripleExpression+
        'CLASS_ORDER__COLON__LINE_MARKER',                      64,     #   `:\n`
        'CLASS_ORDER__DEFINITION_HEADER',                       65,     #   DefinitionHeader+
        'CLASS_ORDER__DUAL_TWIG',                               66,     #   DualTwig
        'CLASS_ORDER__INDENTED__KEYWORD__COLON__LINE_MARKER',   67,     #   `    keyword:\n` (keyword like `else`)
        'CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER',          68,     #   `    keyword\n`  (keyword like `break`)
        'CLASS_ORDER__INDENTED_TOKEN',                          69,     #   Indented_Token
        'CLASS_ORDER__MANY_EXPRESSION',                         70,     #   + expression
        'CLASS_ORDER__MEMBER_EXPRESSION',                       71,     #   Member expression
        'CLASS_ORDER__QUADRUPLE_TWIG',                          72,     #   Commented_VWX_Frill & VWXY_Frill
        'CLASS_ORDER__TRIPLE_EXPRESSION',                       73,     #   ?: expression
        'CLASS_ORDER__TUPLE',                                   74,     #   Tuple of expressions
        'CLASS_ORDER__UNARY_EXPRESSION',                        75,     #   * expression
    )


    assert CLASS_ORDER__PYTHON_START == CLASS_ORDER__ARGUMENT_0
    assert CLASS_ORDER__UNARY_EXPRESSION < CLASS_ORDER__PYTHON_END


    del Shared.CLASS_ORDER__PYTHON_START
    del Shared.CLASS_ORDER__PYTHON_END

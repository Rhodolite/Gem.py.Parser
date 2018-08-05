#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ClassOrder')
def module():
    export(
        'CLASS_ORDER__ARGUMENT_0',                              40,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                            41,     #   Parameters_0 token

        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',                50,     #   BookcaseManyExpression+
        'CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION',              51,     #   BookcaseTripleExpression+
        'CLASS_ORDER__COLON__LINE_MARKER',                      52,     #   `:\n`
        'CLASS_ORDER__DEFINITION_HEADER',                       53,     #   DefinitionHeader+
        'CLASS_ORDER__DUAL_TWIG',                               54,     #   DualTwig
        'CLASS_ORDER__INDENTED__KEYWORD__COLON__LINE_MARKER',   55,     #   `    keyword:\n` (keyword like `else`)
        'CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER',          56,     #   `    keyword\n`  (keyword like `break`)
        'CLASS_ORDER__INDENTED_TOKEN',                          57,     #   Indented_Token
        'CLASS_ORDER__MEMBER_EXPRESSION',                       58,     #   Member expression
        'CLASS_ORDER__TRIPLE_EXPRESSION',                       59,     #   ?: expression
        'CLASS_ORDER__UNARY_EXPRESSION',                        60,     #   * expression
    )


    assert CLASS_ORDER__PYTHON_START == CLASS_ORDER__ARGUMENT_0
    assert CLASS_ORDER__UNARY_EXPRESSION < CLASS_ORDER__PYTHON_END


    del Shared.CLASS_ORDER__PYTHON_START
    del Shared.CLASS_ORDER__PYTHON_END

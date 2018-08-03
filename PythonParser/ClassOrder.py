#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ClassOrder')
def module():
    export(
        'CLASS_ORDER__ARGUMENT_0',                              40,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                            41,     #   Parameters_0 token

        'CLASS_ORDER__BOOKCASE_MANY_FRILL',                     50,     #   BookcaseManyFrill

        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',                60,     #   BookcaseManyExpression+
        'CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION',              61,     #   BookcaseTripleExpression+
        'CLASS_ORDER__COLON__LINE_MARKER',                      62,     #   `:\n`
        'CLASS_ORDER__DEFINITION_HEADER',                       63,     #   DefinitionHeader+
        'CLASS_ORDER__DUAL_TWIG',                               64,     #   DualTwig
        'CLASS_ORDER__INDENTED__KEYWORD__COLON__LINE_MARKER',   65,     #   `    keyword:\n` (keyword like `else`)
        'CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER',          66,     #   `    keyword\n`  (keyword like `break`)
        'CLASS_ORDER__INDENTED_TOKEN',                          67,     #   Indented_Token
        'CLASS_ORDER__MEMBER_EXPRESSION',                       68,     #   Member expression
        'CLASS_ORDER__TRIPLE_EXPRESSION',                       69,     #   ?: expression
        'CLASS_ORDER__UNARY_EXPRESSION',                        70,     #   * expression
    )


    assert CLASS_ORDER__PYTHON_START == CLASS_ORDER__ARGUMENT_0
    assert CLASS_ORDER__UNARY_EXPRESSION < CLASS_ORDER__PYTHON_END


    del Shared.CLASS_ORDER__PYTHON_START
    del Shared.CLASS_ORDER__PYTHON_END

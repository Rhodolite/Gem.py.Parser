#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.ClassOrder')
def gem():
    export(
        'CLASS_ORDER__ARGUMENT_0',                      10,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                    12,     #   Parameters_0 token
        'CLASS_ORDER__INDENTATION',                     13,     #   Indentation token
        'CLASS_ORDER__LINE_MARKER',                     14,     #   LineMarker token
        'CLASS_ORDER__EMPTY_LINE',                      15,     #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',                    16,     #   CommentLine token
        'CLASS_ORDER__COMMENT_LINE__STRING',            17,     #   CommentLine token, inherited from String

        'CLASS_ORDER__FRILL_2',                         20,     #   Commented_V_Frill & VW_Frill
        'CLASS_ORDER__FRILL_MANY',                      21,     #   Frill_Many
        'CLASS_ORDER__BOOKCASE_MANY_FRILL',             22,     #   BookcaseManyFrill

        'CLASS_ORDER__BINARY_EXPRESSION',               30,     #   * expression
        'CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION',        31,     #   BookcaseDualExpression+
        'CLASS_ORDER__BOOKCASE_EXPRESSION',             32,     #   BookcaseExpression+
        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',        33,     #   BookcaseManyExpression+
        'CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION',      34,     #   BookcaseTripleExpression+
        'CLASS_ORDER__CALL_STATEMENT',                  35,     #   CallStatementBase+
        'CLASS_ORDER__DEFINITION_HEADER',               36,     #   DefinitionHeader+
        'CLASS_ORDER__DUAL_TWIG',                       37,     #   DualTwig
        'CLASS_ORDER__MANY_EXPRESSION',                 38,     #   + expression
        'CLASS_ORDER__MEMBER_EXPRESSION',               39,     #   Member expression
        'CLASS_ORDER__QUADRUPLE_TWIG',                  40,     #   Commented_VWX_Frill & VWXY_Frill
        'CLASS_ORDER__TRIPLE_EXPRESSION',               41,     #   ?: expression
        'CLASS_ORDER__TRIPLE_TWIG',                     42,     #   Commented_VW_Frill & VWX_Frill
        'CLASS_ORDER__TUPLE',                           43,     #   Tuple of expressions
        'CLASS_ORDER__UNARY_EXPRESSION',                44,     #   * expression
    )


    assert CLASS_ORDER__PYTHON_START == CLASS_ORDER__ARGUMENT_0
    assert CLASS_ORDER__UNARY_EXPRESSION < CLASS_ORDER__PYTHON_END


    del Shared.CLASS_ORDER__PYTHON_START
    del Shared.CLASS_ORDER__PYTHON_END

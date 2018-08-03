#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.ClassOrder')
def module():
    export(
        'CLASS_ORDER__NORMAL_TOKEN',                     1,     #   Normal token

        'CLASS_ORDER__INDENTATION',                     10,     #   Indentation token
        'CLASS_ORDER__EMPTY_LINE',                      11,     #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',                    12,     #   CommentLine token
        'CLASS_ORDER__COMMENT_LINE__STRING',            13,     #   CommentLine token, inherited from String

        'CLASS_ORDER__FRILL_2',                         20,     #   Commented_V_Frill & VW_Frill
        'CLASS_ORDER__FRILL_3',                         21,     #   Commented_VW_Frill & VWX_Frill
        'CLASS_ORDER__FRILL_MANY',                      22,     #   Frill_Many
        'CLASS_ORDER__LINE_MARKER',                     23,     #   LineMarker token

        'CLASS_ORDER__BINARY_EXPRESSION',               30,     #   BinaryExpression+
        'CLASS_ORDER__BOOKCASE_COUPLE_TWIG',            31,     #   BookcaseCoupleTwig+
        'CLASS_ORDER__BOOKCASE_DUAL_TWIG',              32,     #   BookcaseDualExpression+
        'CLASS_ORDER__BOOKCASE_EXPRESSION',             33,     #   BookcaseExpression+
        'CLASS_ORDER__MANY_EXPRESSION',                 34,     #   ManyExpression+
        'CLASS_ORDER__QUADRUPLE_TWIG',                  35,     #   Commented_VWX_Frill & VWXY_Frill
        'CLASS_ORDER__TUPLE',                           36,     #   TokenTuple+

        'CLASS_ORDER__PYTHON_START',                    40,
        'CLASS_ORDER__PYTHON_END',                      80,
    )

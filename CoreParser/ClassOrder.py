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
        'CLASS_ORDER__LINE_MARKER',                     22,     #   LineMarker token

        'CLASS_ORDER__BOOKCASE_COUPLE_TWIG',            30,     #   BookcaseCoupleTwig+
        'CLASS_ORDER__BOOKCASE_DUAL_TWIG',              31,     #   BookcaseDualExpression+

        'CLASS_ORDER__PYTHON_START',                    40,
        'CLASS_ORDER__PYTHON_END',                      80,
    )

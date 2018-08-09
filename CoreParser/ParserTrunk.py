#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.ParserTrunk')
def module():
    require_module('CoreParser.Nub')


    @export
    class ParserTrunk(Object):
        __slots__     = (())
        herd_estimate = 0
        is_herd       = false

        if CRYSTAL_parser:
            is_CRYSTAL_identifier            = false
            is_empty_line                    = false
            is_end_of_data                   = false
            is_end_of_data__or__unknown_line = false
            is_right_parenthesis             = false

        if PYTHON_parser:
            is_class_decorator_or_function_header = false
            is_comment_line                       = false
            is_comment__or__empty_line            = false
            is_decorator_header                   = false
            is_right_brace                        = false
            is_right_square_bracket               = false
            is_statement                          = false
            is_vw_frill                           = false

        if TREMOLITE_parser:
            is_TREMOLITE__at_sign            = false
            is_TREMOLITE__set__right_brace   = false
            is_TREMOLITE__tilde__right_brace = false


        nub = static_conjure_nub

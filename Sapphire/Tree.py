#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Tree')
def gem():
    @share
    class SapphireTrunk(Object):
        __slots__ = (())


        herd_estimate                         = 0
        is_class_decorator_or_function_header = false
        is_comment_line                       = false
        is_comment__or__empty_line            = false
        is_decorator_header                   = false
        is_herd                               = false
        is_empty_line                         = false
        is_end_of_data                        = false
        is_end_of_data__or__unknown_line      = false
        is_herd                               = false
        is_right_brace                        = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false
        is_statement                          = false


        def display_full_token(t):
            return t.display_token()


        nub = static_conjure_nub

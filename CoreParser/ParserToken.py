#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.ParserToken')
def module():
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.Method')
    require_module('CoreParser.Nub')
    require_module('CoreParser.TokenCache')


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    if CRYSTAL_parser:
        def count_newlines__zero(t):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert (t.s is intern_string(t.s))

            return 0


    @export
    class ParserToken(Object):
        __slots__ = ((
            's',
        ))

        is_herd       = false
        herd_estimate = 0

        if CRYSTAL_parser:
            ends_in_newline                  = false
            is_CRYSTAL_comma                 = false
            is_CRYSTAL_identifier            = false
            is_empty_line                    = false
            is_end_of_data                   = false
            is_end_of_data__or__unknown_line = false
            is_right_parenthesis             = false
            line_marker                      = false
            newlines                         = 0

        if PYTHON_parser:
            is_comment_line            = false
            is_comment__or__empty_line = false
            is_indentation             = false
            is_keyword                 = false
            is_keyword_return          = false
            is_right_square_bracket    = false
            is_vw_frill                = false

        if TREMOLITE_parser:
            is_TREMOLITE_right_brace_set = false


        def __init__(t, s):
            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.s)


        if CRYSTAL_parser:
            count_newlines = count_newlines__zero


        dump_token    = dump_token__with_braces
        display_token = __repr__


        if PYTHON_parser:
            is_name = is_name__0


        nub   = static_conjure_nub
        order = order__s


        def write(t, w):
            w(t.s)

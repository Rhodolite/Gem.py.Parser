#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Whitespace')
def module():
    require_module('CoreParser.Method')


    class TokenWhitespace(ParserToken):
        __slots__    = (())
        display_name = 'whitespace'


        def __init__(t, s):
            assert '\n' not in s

            t.s = s


        if capital_global.python_parser:
            transform = transform__self


    [
            conjure_whitespace, conjure_whitespace__ends_in_newline,
    ] = produce_conjure_action_word('whitespace', TokenWhitespace, produce_ends_in_newline = true)


    export(
        'conjure_whitespace',                   conjure_whitespace,
        'conjure_whitespace__ends_in_newline',  conjure_whitespace__ends_in_newline,
    )

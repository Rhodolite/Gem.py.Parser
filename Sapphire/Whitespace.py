#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Whitespace')
def gem():
    require_gem('Sapphire.Indentation')
    require_gem('Sapphire.Method')


    if __debug__:
        cache_many = []


    empty_line_cache   = {}
    lookup_empty_line  = empty_line_cache.get
    provide_empty_line = empty_line_cache.setdefault


    class EmptyLine(String):
        __slots__                        = (())
        class_order                      = CLASS_ORDER__EMPTY_LINE
        ends_in_newline                  = true
        indentation                      = none
        impression                       = 0
        is_any_else                      = false
        is_any_except_or_finally         = false
        is_comment_line                  = false
        is_comment__or__empty_line       = true
        is_else_header_or_fragment       = false
        is_empty_line                    = true
        is_end_of_data                   = false
        is_end_of_data__or__unknown_line = false
        is_statement                     = false
        is_statement_header              = false
        line_marker                      = false
        newlines                         = 1


        def __repr__(t):
            return arrange('<EmptyLine %s>', portray_string(t))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.newlines is 1) and (t.line_marker is false)
            assert (t.count('\n') is 1) and (t[-1] == '\n')

            return 1


        def display_token(t):
            if t is empty_line:
                return '<empty-line>'

            return arrange('<empty-line %s>', portray_string(t))


        def dump_token(t, f, newline = true):
            assert newline is true

            f.line('<%s>', portray_string(t)[1:-1])


        find_require_gem = find_require_gem__0
        order            = order__string
        scout_variables  = scout_variables__0
        transform        = transform__remove_comments_0


        def write(t, w):
            w(t)


    class TokenWhitespace(PearlToken):
        display_name = 'whitespace'


        def __init__(t, s):
            assert '\n' not in s

            t.s = s


        transform = transform__self


    def conjure_empty_line(s):
        r = lookup_empty_line(s)

        if r is not none:
            return r

        r = EmptyLine(s)

        return provide_empty_line(r, r)


    empty_line = conjure_empty_line('\n')


    [
            conjure_whitespace, conjure_whitespace__ends_in_newline,
    ] = produce_conjure_action_word('whitespace', TokenWhitespace, produce_ends_in_newline = true)


    append_cache('empty-line', empty_line_cache)


    share(
        'conjure_empty_line',                   conjure_empty_line,
        'conjure_whitespace',                   conjure_whitespace,
        'conjure_whitespace__ends_in_newline',  conjure_whitespace__ends_in_newline,
    )

#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.DualToken')
def module():
    @export
    class DualToken(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
        ))


        def __init__(t, s, a, b):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s
            assert s == a.s + b.s

            t.s = s
            t.a = a
            t.b = b


        __repr__ = portray__ab


        if 0:                                                           #   Not currently used
            def display_full_token(t):
                display_name = t.display_name
                a_s          = t.a.s
                b_s          = t.b.s

                return arrange('<%s <%s> <%s>>',
                               display_name,
                               portray_string(a_s)   if '\n' in a_s else   a_s,
                               portray_string(b_s)   if '\n' in b_s else   b_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return arrange('<%s>', display_name)

            a_s = t.a.s
            b_s = t.b.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(a_s)   if '\n' in a_s else   a_s,
                           portray_string(b_s)   if '\n' in b_s else   b_s)


        order = order__s

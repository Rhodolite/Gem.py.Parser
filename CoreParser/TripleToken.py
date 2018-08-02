#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TripleToken')
def module():
    def construct_triple_token(t, s, a, b, c):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s + c.s
        assert '\n' not in s

        t.s = s
        t.a = a
        t.b = b
        t.c = c


    @export
    class TripleToken(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
            'c',                        #   Operator+
        ))


        __init__ = construct_triple_token
        __repr__ = portray__123


        if 0:                                                           #   Not currently used
            def display_full_token(t):
                display_name = t.display_name
                a_s          = t.a.s
                b_s          = t.b.s
                c_s          = t.c.s

                return arrange('<%s <%s> <%s> <%s>>',
                               display_name,
                               (portray_string(a_s)   if '\n' in a_s else   a_s),
                               (portray_string(b_s)   if '\n' in b_s else   b_s),
                               (portray_string(c_s)   if '\n' in c_s else   c_s))


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            a = t.a

            if a.is_indentation:
                return arrange('<%s %+d %s %s>',
                               display_name,
                               a.total,
                               t.b.display_short_token(),
                               t.c.display_short_token())


            return arrange('<%s %s %s %s>',
                           display_name,
                           a  .display_short_token(),
                           t.b.display_short_token(),
                           t.c.display_short_token())



    TripleToken.k1 = TripleToken.a
    TripleToken.k2 = TripleToken.b
    TripleToken.k3 = TripleToken.c


    @export
    class Whitespace_Atom_Whitespace(TripleToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'whitespace+atom+whitespace'


        if capital_global.python_parser:
            is__atom__or__special_operator = true
            is_atom                        = true
            is_special_operator            = false

        if capital_global.python_parser:
            scout_variables = scout_variables__0

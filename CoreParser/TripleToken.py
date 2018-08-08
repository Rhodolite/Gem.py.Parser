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


    def construct_triple_token__with_newlines(t, s, a, b, c, ends_in_newline, newlines):
        assert t.line_marker is false
        assert s == a.s + b.s + c.s
        assert ends_in_newline is (c.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.a               = a
        t.b               = b
        t.c               = c
        t.ends_in_newline = ends_in_newline
        t.newlines        = newlines


    @export
    def create_triple_token__line_marker(Meta, s, a, b, c):
        assert (s == a.s + b.s + c.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c)
                       if newlines is 1 else
                           conjure_ActionWord_LineMarker_Many(
                               Meta, construct_triple_token__line_marker__many,
                           )(s, a, b, c, newlines)
               )


    @export
    def create_triple_token__with_newlines(Meta, s, a, b, c):
        assert s == a.s + b.s + c.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c)
                       if newlines is 0 else
                           conjure_ActionWord_WithNewlines(
                               Meta, construct_triple_token__with_newlines,
                           )(s, a, b, c, s[-1] == '\n', newlines)
               )


    #
    #<produce_evoke_triple_token>
    #   produce_evoke_triple_token__ends_in_newline
    #   produce_evoke_triple_token__line_marker
    #       Two slightly different versions ...
    #
    @export
    def produce_evoke_triple_token__ends_in_newline(
            name, Meta, conjure_a, conjure_b, conjure_c, conjure_c__ends_in_newline,

            lookup  = lookup_normal_token,
            provide = provide_normal_token,
    ):
        @rename('evoke_%s', name)
        def evoke_triple_token(a_end, b_end, c_end):
            #
            #   For empty indentation: "qi() == a_end"
            #
            assert qi() <= a_end < b_end

            full = qs()[qi() : c_end]

            r = lookup(full)

            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            full = intern_string(full)
            s    = qs()

            return provide(
                       full,
                       create_triple_token__with_newlines(
                           Meta,
                           full,
                           conjure_a(s[qi()  : a_end]),
                           conjure_b(s[a_end : b_end]),
                           (conjure_c__ends_in_newline   if c_end is none else   conjure_c)(s[b_end : c_end]),
                       ),
                   )


        return evoke_triple_token


    @export
    def produce_evoke_triple_token__line_marker(name, Meta, conjure_a, conjure_b):
        @rename('evoke_%s', name)
        def evoke_triple_token(a_end, b_end):
            #
            #   For empty indentation: "qi() == a_end"
            #
            assert qi() <= a_end < b_end

            triple_s = qs()[qi() : ]

            r = lookup_line_marker(triple_s)

            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            s        = qs()
            triple_s = intern_string(triple_s)

            return provide_line_marker(
                       triple_s,
                       create_triple_token__line_marker(
                           Meta,
                           triple_s,
                           conjure_a          (s[qi()  : a_end]),
                           conjure_b          (s[a_end : b_end]),
                           conjure_line_marker(s[b_end :      ]),
                       ),
                   )

        return evoke_triple_token
    #</produce_evoke_triple_token>


    @export
    class TripleToken(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
            'c',                        #   Operator+
        ))


        __init__ = construct_triple_token
        __repr__ = portray__123


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            a = t.a

            if a.is_indentation:
                return arrange('<%s %+d %s %s>',
                               display_name,
                               a.total,
                               t.b.display_token(),
                               t.c.display_token())


            return arrange('<%s %s %s %s>',
                           display_name,
                           a  .display_token(),
                           t.b.display_token(),
                           t.c.display_token())



    TripleToken.k1 = TripleToken.a
    TripleToken.k2 = TripleToken.b
    TripleToken.k3 = TripleToken.c


    @export
    class Whitespace_Atom_Whitespace(TripleToken):
        __slots__    = (())
        display_name = 'whitespace+atom+whitespace'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_sign          = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false


        if PYTHON_parser:
            scout_variables = scout_variables__0


    @export
    class Whitespace_Name_Whitespace(TripleToken):
        __slots__    = (())
        display_name = 'whitespace+name+whitespace'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_identifier                            = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_sign          = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_PYTHON__identifier__or__star_parameter = true


        if PYTHON_parser:
            scout_variables = scout_variables__b


    #
    #   evoke
    #
    evoke_whitespace__double_quote__whitespace = produce_evoke_triple_token__ends_in_newline(
            'whitespace+double-quote+whitespace',
            Whitespace_Atom_Whitespace,
            conjure_whitespace,
            conjure_double_quote,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke_whitespace_name_whitespace = produce_evoke_triple_token__ends_in_newline(
            'whitespace+name+whitespace',
            Whitespace_Name_Whitespace,
            conjure_whitespace,
            conjure_name,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke_whitespace_number_whitespace = produce_evoke_triple_token__ends_in_newline(
            'whitespace+number+whitespace',
            Whitespace_Atom_Whitespace,
            conjure_whitespace,
            conjure_token_number,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke_whitespace__single_quote__whitespace = produce_evoke_triple_token__ends_in_newline(
            'whitespace+single-quote+whitespace',
            Whitespace_Atom_Whitespace,
            conjure_whitespace,
            conjure_single_quote,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )


    #
    #   find_evoke_crystal_whitespace_atom_whitespace
    #
    find_evoke_crystal_whitespace_atom_whitespace = {
            '"' : evoke_whitespace__double_quote__whitespace,
            "'" : evoke_whitespace__single_quote__whitespace,

            '.' : evoke_whitespace_number_whitespace,
            '0' : evoke_whitespace_number_whitespace, '1' : evoke_whitespace_number_whitespace,
            '2' : evoke_whitespace_number_whitespace, '3' : evoke_whitespace_number_whitespace,
            '4' : evoke_whitespace_number_whitespace, '5' : evoke_whitespace_number_whitespace,
            '6' : evoke_whitespace_number_whitespace, '7' : evoke_whitespace_number_whitespace,
            '8' : evoke_whitespace_number_whitespace, '9' : evoke_whitespace_number_whitespace,

            'A' : evoke_whitespace_name_whitespace, 'B' : evoke_whitespace_name_whitespace,
            'C' : evoke_whitespace_name_whitespace, 'D' : evoke_whitespace_name_whitespace,
            'E' : evoke_whitespace_name_whitespace, 'F' : evoke_whitespace_name_whitespace,
            'G' : evoke_whitespace_name_whitespace, 'H' : evoke_whitespace_name_whitespace,
            'I' : evoke_whitespace_name_whitespace, 'J' : evoke_whitespace_name_whitespace,
            'K' : evoke_whitespace_name_whitespace, 'L' : evoke_whitespace_name_whitespace,
            'M' : evoke_whitespace_name_whitespace, 'N' : evoke_whitespace_name_whitespace,
            'O' : evoke_whitespace_name_whitespace, 'P' : evoke_whitespace_name_whitespace,
            'Q' : evoke_whitespace_name_whitespace, 'R' : evoke_whitespace_name_whitespace,
            'S' : evoke_whitespace_name_whitespace, 'T' : evoke_whitespace_name_whitespace,
            'U' : evoke_whitespace_name_whitespace, 'V' : evoke_whitespace_name_whitespace,
            'W' : evoke_whitespace_name_whitespace, 'X' : evoke_whitespace_name_whitespace,
            'Y' : evoke_whitespace_name_whitespace, 'Z' : evoke_whitespace_name_whitespace,
            '_' : evoke_whitespace_name_whitespace,

            'a' : evoke_whitespace_name_whitespace, 'b' : evoke_whitespace_name_whitespace,
            'c' : evoke_whitespace_name_whitespace, 'd' : evoke_whitespace_name_whitespace,
            'e' : evoke_whitespace_name_whitespace, 'f' : evoke_whitespace_name_whitespace,
            'g' : evoke_whitespace_name_whitespace, 'h' : evoke_whitespace_name_whitespace,
            'i' : evoke_whitespace_name_whitespace, 'j' : evoke_whitespace_name_whitespace,
            'k' : evoke_whitespace_name_whitespace, 'l' : evoke_whitespace_name_whitespace,
            'm' : evoke_whitespace_name_whitespace, 'n' : evoke_whitespace_name_whitespace,
            'o' : evoke_whitespace_name_whitespace, 'p' : evoke_whitespace_name_whitespace,
            'q' : evoke_whitespace_name_whitespace, 'r' : evoke_whitespace_name_whitespace,
            's' : evoke_whitespace_name_whitespace, 't' : evoke_whitespace_name_whitespace,
            'u' : evoke_whitespace_name_whitespace, 'v' : evoke_whitespace_name_whitespace,
            'w' : evoke_whitespace_name_whitespace, 'x' : evoke_whitespace_name_whitespace,
            'y' : evoke_whitespace_name_whitespace, 'z' : evoke_whitespace_name_whitespace,
        }.__getitem__


    #
    #   export
    #
    export(
        'evoke_whitespace_name_whitespace',                 evoke_whitespace_name_whitespace,
        'find_evoke_crystal_whitespace_atom_whitespace',    find_evoke_crystal_whitespace_atom_whitespace,
    )

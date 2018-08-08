#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.DualToken')
def module():
    require_module('CoreParser.Atom')
    require_module('CoreParser.Whitespace')


    def construct_dual_token__line_marker__many(t, s, a, b, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines >= 1)
        assert s == a.s + b.s
        assert s.count('\n') == newlines
        assert b.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.newlines = newlines


    def construct_dual_token__with_newlines(t, s, a, b, ends_in_newline, newlines):
        assert t.line_marker is false
        assert s == a.s + b.s
        assert ends_in_newline is (b.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.a               = a
        t.b               = b
        t.ends_in_newline = ends_in_newline
        t.newlines        = newlines


    def create_dual_token__with_newlines(Meta, s, a, b):
        assert s == a.s + b.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 0 else
                           conjure_ActionWord_WithNewlines(
                                Meta, construct_dual_token__with_newlines,
                           )(s, a, b, s[-1] == '\n', newlines)
               )


    #
    #<create_dual_token>
    #   produce_create_dual_token__line_marker
    #   produce_create_dual_token__normal
    #       Two slightly different versions ...
    #
    def produce_conjure_dual_token__X__helper(name, Meta, create_dual_token, lookup, provide):
        @rename('conjure_%s', name)
        def conjure_dual_token(a, b):
            s = a.s + b.s

            r = lookup(s)

            if r is not none:
                assert (r.a is a) and (r.b is b)

                return r

            s = intern_string(s)

            return provide(s, create_dual_token(Meta, s, a, b))


        return conjure_dual_token


    def create_dual_token__line_marker(Meta, s, a, b):
        assert (s == a.s + b.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 1 else
                           conjure_ActionWord_LineMarker_Many(
                                Meta, construct_dual_token__line_marker__many
                           )(s, a, b, newlines)
               )


    @export
    def produce_conjure_dual_token__normal(
            name, Meta,

            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
    ):
        return produce_conjure_dual_token__X__helper(name, Meta, create_dual_token__with_newlines, lookup, provide)


    @export
    def produce_conjure_dual_token__line_marker(name, Meta):
        return produce_conjure_dual_token__X__helper(
                name, Meta, create_dual_token__line_marker, lookup_line_marker, provide_line_marker,
            )
    #</produce_conjure_dual_token>


    #
    #<produce_evoke_dual_token>
    #   produce_evoke_dual_token__ends_in_newline
    #   produce_evoke_dual_token__indentation
    #   produce_evoke_dual_token__line_marker
    #       Three slightly different versions ...
    #
    def produce_evoke_dual_token__X__indentation_or_whitespace(
            name, Meta, conjure_first, conjure_second, lookup, provide,
    ):
        @rename('evoke_%s', name)
        def evoke_dual_token__X__indentation_or_whitespace(middle, end):
            #
            #   Indentation tokens may have 0 length, hence 'qi() <= middle'
            #
            assert qi() <= middle < end

            full = qs()[qi() : end]

            r = lookup(full)

            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            full = intern_string(full)
            s    = qs()

            return provide(
                       full,
                       create_dual_token__with_newlines(
                           Meta,
                           full,
                           conjure_first (s[qi()   : middle]),
                           conjure_second(s[middle : end   ]),
                       ),
                   )


        return evoke_dual_token__X__indentation_or_whitespace


    @export
    def produce_evoke_dual_token__ends_in_newline(
            name, Meta, conjure_first, conjure_second, conjure_second__ends_in_newline,

            lookup  = lookup_normal_token,
            provide = provide_normal_token,
    ):
        @rename('evoke_%s', name)
        def evoke_dual_token__ends_in_newline(middle, end, second = 0):
            if end is none:
                assert qi() < middle
            else:
                assert qi() < middle < end

            full = qs()[qi() : end]

            r = lookup(full)

            if r is not none:
                #if not ( (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta)) ):
                #    my_line('r: %r', r)
                #    my_line('Meta: %r', Meta)
                #    my_line('adjusted: %r', lookup_adjusted_meta(Meta))

                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            full = intern_string(full)
            s    = qs()

            if second is not 0:
                assert second == s[middle : end]

            return provide(
                       full,
                       create_dual_token__with_newlines(
                           Meta,
                           full,
                           conjure_first(s[qi() : middle]),
                           (conjure_second__ends_in_newline   if end is none else   conjure_second)
                               ( (s[middle : end]   if second is 0 else   second) ),
                       ),
                   )


        return evoke_dual_token__ends_in_newline


    @export
    def produce_evoke_dual_token__indentation(name, Meta, conjure_first, conjure_second):
        return produce_evoke_dual_token__X__indentation_or_whitespace(
                name, Meta, conjure_first, conjure_second, lookup_indentation, provide_indentation,
            )


    @export
    def produce_evoke_dual_token__line_marker(name, Meta, conjure_first):
        @rename('evoke_%s', name)
        def evoke_dual_token__line_marker(a_end):
            assert qi() < a_end

            full_s = qs()[qi() : ]

            r = lookup_line_marker(full_s)

            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            s      = qs()
            full_s = intern_string(full_s)

            return provide_line_marker(
                       full_s,
                       create_dual_token__line_marker(
                           Meta,
                           full_s,
                           conjure_first      (s[qi()  : a_end]),
                           conjure_line_marker(s[a_end :      ]),
                       ),
                   )


        return evoke_dual_token__line_marker


    @export
    def produce_evoke_dual_token__whitespace(name, Meta, conjure_first, conjure_second):
        return produce_evoke_dual_token__X__indentation_or_whitespace(
                name, Meta, conjure_first, conjure_second, lookup_normal_token, provide_normal_token,
            )
    #</produce_evoke_dual_token>


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


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return arrange('<%s>', display_name)

            return arrange('<%s %s %s>', display_name, t.a.display_token(), t.b.display_token())


        order = order__s


    @export
    class Atom_Whitespace(DualToken):
        __slots__    = (())
        display_name = 'atom+whitespace'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false


        if PYTHON_parser:
            scout_variables = scout_variables__0


    @export
    class Name_Whitespace(DualToken):
        __slots__    = (())
        display_name = 'name+whitespace'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_identifier                            = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_PYTHON__identifier__or__star_parameter = true


        if PYTHON_parser:
            scout_variables = scout_variables__a
            write_variables = write_variables__a


    @export
    class Whitespace_Atom(DualToken):
        __slots__    = (())
        display_name = 'whitespace+atom'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false


        if PYTHON_parser:
            def find_atom(t):
                return t.b


        if PYTHON_parser:
            scout_variables = scout_variables__0


    @export
    class Whitespace_Name(DualToken):
        __slots__    = (())
        display_name = 'whitespace+name'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_identifier                            = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_PYTHON__identifier__or__star_parameter = true


        if PYTHON_parser:
            add_parameters = add_parameters__b


        if PYTHON_parser:
            def mutate(t, vary, priority):
                if vary.remove_comments:
                    return t.b

                return t


        if PYTHON_parser:
            scout_default_values = scout_default_values__b
            scout_variables      = scout_variables__b


        if PYTHON_parser:
            def transform(t, vary):
                if vary.remove_comments:
                    return t.b

                return t


        if PYTHON_parser:
            write_variables = write_variables__b


    #
    #   conjure
    #
    conjure_atom_whitespace = produce_conjure_dual_token__normal('atom_whitespace', Atom_Whitespace)
    conjure_name_whitespace = produce_conjure_dual_token__normal('name_whitespace', Name_Whitespace)
    conjure_whitespace_atom = produce_conjure_dual_token__normal('whitespace_atom', Whitespace_Atom)
    conjure_whitespace_name = produce_conjure_dual_token__normal('whitespace_name', Whitespace_Name)



    #
    #   evoke
    #
    evoke__double_quote__whitespace = produce_evoke_dual_token__ends_in_newline(
            'double-quote+whitespace',
            Atom_Whitespace,
            conjure_double_quote,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke_name_whitespace = produce_evoke_dual_token__ends_in_newline(
            'name+whitespace',
            Name_Whitespace,
            conjure_name,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke_number_whitespace = produce_evoke_dual_token__ends_in_newline(
            'number+whitespace',
            Atom_Whitespace,
            conjure_token_number,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke__single_quote__whitespace = produce_evoke_dual_token__ends_in_newline(
            'single-quote+whitespace',
            Atom_Whitespace,
            conjure_single_quote,
            conjure_whitespace,
            conjure_whitespace__ends_in_newline,
        )

    evoke_whitespace__double_quote = produce_evoke_dual_token__whitespace(
            'whitespace+double-quote',
            Whitespace_Atom,
            conjure_whitespace,
            conjure_double_quote,
        )

    evoke_whitespace_name = produce_evoke_dual_token__whitespace(
            'whitespace+name',
            Whitespace_Name,
            conjure_whitespace,
            conjure_name,
        )

    evoke_whitespace_number = produce_evoke_dual_token__whitespace(
            'whitespace+number',
            Whitespace_Atom,
            conjure_whitespace,
            conjure_token_number,
        )

    evoke_whitespace__single_quote = produce_evoke_dual_token__whitespace(
            'whitespace+single-quote',
            Whitespace_Atom,
            conjure_whitespace,
            conjure_single_quote,
        )


    #
    #   find_evoke_crystal_atom_whitespace
    #
    find_evoke_crystal_atom_whitespace = {
            '"' : evoke__double_quote__whitespace,
            "'" : evoke__single_quote__whitespace,

            '.' : evoke_number_whitespace,
            '0' : evoke_number_whitespace, '1' : evoke_number_whitespace, '2' : evoke_number_whitespace,
            '3' : evoke_number_whitespace, '4' : evoke_number_whitespace, '5' : evoke_number_whitespace,
            '6' : evoke_number_whitespace, '7' : evoke_number_whitespace, '8' : evoke_number_whitespace,
            '9' : evoke_number_whitespace,

            'A' : evoke_name_whitespace, 'B' : evoke_name_whitespace, 'C' : evoke_name_whitespace,
            'D' : evoke_name_whitespace, 'E' : evoke_name_whitespace, 'F' : evoke_name_whitespace,
            'G' : evoke_name_whitespace, 'H' : evoke_name_whitespace, 'I' : evoke_name_whitespace,
            'J' : evoke_name_whitespace, 'K' : evoke_name_whitespace, 'L' : evoke_name_whitespace,
            'M' : evoke_name_whitespace, 'N' : evoke_name_whitespace, 'O' : evoke_name_whitespace,
            'P' : evoke_name_whitespace, 'Q' : evoke_name_whitespace, 'R' : evoke_name_whitespace,
            'S' : evoke_name_whitespace, 'T' : evoke_name_whitespace, 'U' : evoke_name_whitespace,
            'V' : evoke_name_whitespace, 'W' : evoke_name_whitespace, 'X' : evoke_name_whitespace,
            'Y' : evoke_name_whitespace, 'Z' : evoke_name_whitespace, '_' : evoke_name_whitespace,

            'a' : evoke_name_whitespace, 'b' : evoke_name_whitespace, 'c' : evoke_name_whitespace,
            'd' : evoke_name_whitespace, 'e' : evoke_name_whitespace, 'f' : evoke_name_whitespace,
            'g' : evoke_name_whitespace, 'h' : evoke_name_whitespace, 'i' : evoke_name_whitespace,
            'j' : evoke_name_whitespace, 'k' : evoke_name_whitespace, 'l' : evoke_name_whitespace,
            'm' : evoke_name_whitespace, 'n' : evoke_name_whitespace, 'o' : evoke_name_whitespace,
            'p' : evoke_name_whitespace, 'q' : evoke_name_whitespace, 'r' : evoke_name_whitespace,
            's' : evoke_name_whitespace, 't' : evoke_name_whitespace, 'u' : evoke_name_whitespace,
            'v' : evoke_name_whitespace, 'w' : evoke_name_whitespace, 'x' : evoke_name_whitespace,
            'y' : evoke_name_whitespace, 'z' : evoke_name_whitespace,
        }.__getitem__


    #
    #   find_evoke_crystal_whitespace_atom
    #
    find_evoke_crystal_whitespace_atom = {
            '"' : evoke_whitespace__double_quote,
            "'" : evoke_whitespace__single_quote,

            '.' : evoke_whitespace_number,
            '0' : evoke_whitespace_number, '1' : evoke_whitespace_number, '2' : evoke_whitespace_number,
            '3' : evoke_whitespace_number, '4' : evoke_whitespace_number, '5' : evoke_whitespace_number,
            '6' : evoke_whitespace_number, '7' : evoke_whitespace_number, '8' : evoke_whitespace_number,
            '9' : evoke_whitespace_number,

            'A' : evoke_whitespace_name, 'B' : evoke_whitespace_name, 'C' : evoke_whitespace_name,
            'D' : evoke_whitespace_name, 'E' : evoke_whitespace_name, 'F' : evoke_whitespace_name,
            'G' : evoke_whitespace_name, 'H' : evoke_whitespace_name, 'I' : evoke_whitespace_name,
            'J' : evoke_whitespace_name, 'K' : evoke_whitespace_name, 'L' : evoke_whitespace_name,
            'M' : evoke_whitespace_name, 'N' : evoke_whitespace_name, 'O' : evoke_whitespace_name,
            'P' : evoke_whitespace_name, 'Q' : evoke_whitespace_name, 'R' : evoke_whitespace_name,
            'S' : evoke_whitespace_name, 'T' : evoke_whitespace_name, 'U' : evoke_whitespace_name,
            'V' : evoke_whitespace_name, 'W' : evoke_whitespace_name, 'X' : evoke_whitespace_name,
            'Y' : evoke_whitespace_name, 'Z' : evoke_whitespace_name, '_' : evoke_whitespace_name,

            'a' : evoke_whitespace_name, 'b' : evoke_whitespace_name, 'c' : evoke_whitespace_name,
            'd' : evoke_whitespace_name, 'e' : evoke_whitespace_name, 'f' : evoke_whitespace_name,
            'g' : evoke_whitespace_name, 'h' : evoke_whitespace_name, 'i' : evoke_whitespace_name,
            'j' : evoke_whitespace_name, 'k' : evoke_whitespace_name, 'l' : evoke_whitespace_name,
            'm' : evoke_whitespace_name, 'n' : evoke_whitespace_name, 'o' : evoke_whitespace_name,
            'p' : evoke_whitespace_name, 'q' : evoke_whitespace_name, 'r' : evoke_whitespace_name,
            's' : evoke_whitespace_name, 't' : evoke_whitespace_name, 'u' : evoke_whitespace_name,
            'v' : evoke_whitespace_name, 'w' : evoke_whitespace_name, 'x' : evoke_whitespace_name,
            'y' : evoke_whitespace_name, 'z' : evoke_whitespace_name,
        }.__getitem__


    #
    #   export
    #
    export(
        'find_evoke_crystal_whitespace_atom',   find_evoke_crystal_whitespace_atom,
        'find_evoke_crystal_atom_whitespace',   find_evoke_crystal_atom_whitespace,
        'evoke_name_whitespace',                evoke_name_whitespace,
        'evoke_whitespace_name',                evoke_whitespace_name,
        'conjure_atom_whitespace',              conjure_atom_whitespace,
        'conjure_name_whitespace',              conjure_name_whitespace,
        'conjure_whitespace_atom',              conjure_whitespace_atom,
        'conjure_whitespace_name',              conjure_whitespace_name,
    )

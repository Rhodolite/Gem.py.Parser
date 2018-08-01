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
        def evoke_dual_token__ends_in_newline(middle, end):
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

            return provide(
                       full,
                       create_dual_token__with_newlines(
                           Meta,
                           full,
                           conjure_first(s[qi() : middle]),
                           (conjure_second__ends_in_newline   if end is none else   conjure_second)(s[middle : end]),
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


    @export
    class Whitespace_Atom(DualToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'whitespace+atom'


        if capital_global.python_parser:
            is__atom__or__special_operator = true
            is_atom                        = true
            is_special_operator            = false


        if capital_global.python_parser:
            def find_atom(t):
                return t.b


        if capital_global.python_parser:
            scout_variables = scout_variables__0


    @export
    class Whitespace_Name(DualToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'whitespace+name'


        if capital_global.python_parser:
            is__atom__or__special_operator = true
            is_atom                        = true
            is_identifier                  = true
            is_special_operator            = false


        if capital_global.python_parser:
            add_parameters = add_parameters__b


        if capital_global.python_parser:
            def mutate(t, vary, priority):
                if vary.remove_comments:
                    return t.b

                return t


        if capital_global.python_parser:
            scout_default_values = scout_default_values__b
            scout_variables      = scout_variables__b


        if capital_global.python_parser:
            def transform(t, vary):
                if vary.remove_comments:
                    return t.b

                return t


        if capital_global.python_parser:
            write_variables = write_variables__b


    #
    #   evoke
    #
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
    #   find_crystal_evoke_whitespace_atom
    #
    find_crystal_evoke_whitespace_atom = {
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
        'evoke_whitespace_name',                evoke_whitespace_name,
        'find_crystal_evoke_whitespace_atom',   find_crystal_evoke_whitespace_atom,
    )

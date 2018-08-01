#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.DualToken')
def module():
    require_module('PythonParser.ClassOrder')
    require_module('PythonParser.CreateMeta')
    require_module('PythonParser.Elemental')
    require_module('PythonParser.TokenCache')
    require_module('PythonParser.Whitespace')


    def construct_dual_token(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s
        assert '\n' not in s

        t.s = s
        t.a = a
        t.b = b


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


    def construct_dual_token__line_marker_1(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s
        assert s.count('\n') is 1
        assert b.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b


    def construct_dual_token__line_marker__many(t, s, a, b, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines >= 1)
        assert s == a.s + b.s
        assert s.count('\n') == newlines
        assert b.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.newlines = newlines




    def produce_mutate_atom_whitespace(name, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            a    = t.a
            a__2 = a.mutate(vary, priority)

            if vary.remove_comments:
                return a__2

            b    = t.b
            b__2 = b.transform(vary)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        return mutate


    def produce_transform_atom_whitespace(name, conjure):
        @rename('transform_%s', name)
        def transform(t, vary):
            a    = t.a
            a__2 = a.transform(vary)

            if vary.remove_comments:
                return a__2

            b    = t.b
            b__2 = b.transform(vary)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        return transform



    def produce_mutate_whitespace_atom(name, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            b    = t.b
            b__2 = b.mutate(vary, priority)

            if vary.remove_comments:
                return b__2

            a    = t.a
            a__2 = a.transform(vary)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        return mutate


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


    def produce_conjure_dual_token(
            name, Meta,

            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false
    ):
        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_dual_token = create_dual_token__line_marker
            lookup            = lookup_line_marker
            provide           = provide_line_marker
        else:
            create_dual_token = create_dual_token__with_newlines


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

    def produce_evoke_dual_token__indentation_or_whitespace(
            name, Meta, conjure_first, conjure_second, lookup, provide,
    ):
        @rename('evoke_%s', name)
        def evoke_dual_token__indentation_or_whitespace(middle, end):
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


        return evoke_dual_token__indentation_or_whitespace


    def produce_evoke_dual_token__indentation(name, Meta, conjure_first, conjure_second):
        return produce_evoke_dual_token__indentation_or_whitespace(
                name, Meta, conjure_first, conjure_second, lookup_indentation, provide_indentation,
            )


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


    def produce_evoke_dual_token__whitespace(name, Meta, conjure_first, conjure_second):
        return produce_evoke_dual_token__indentation_or_whitespace(
                name, Meta, conjure_first, conjure_second, lookup_normal_token, provide_normal_token,
            )


    class Arguments_0(DualToken):
        __slots__                             = (())
        class_order                           = CLASS_ORDER__ARGUMENT_0
        display_name                          = 'arguments-(0)'
        is__arguments_0__or__left_parenthesis = true
        is_arguments_0                        = true
        is_postfix_operator                   = true

        scout_variables = scout_variables__0


    class Atom_Whitespace(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'atom+whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true

        scout_variables = scout_variables__0


    class Colon_LineMarker_1(DualToken):
        __slots__                               = (())
        class_order                             = CLASS_ORDER__COLON__LINE_MARKER
        display_name                            = r':\n'
        ends_in_newline                         = true
        is_colon__line_marker                   = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_comprehension_expression      = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_multiply_expression           = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_python_arithmetic_expression  = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
        line_marker                             = true
        newlines                                = 1

        __init__       = construct_dual_token__line_marker_1
        count_newlines = count_newlines__line_marker


    class Colon_RightSquareBracket(DualToken):
        __slots__                               = (())
        class_order                             = CLASS_ORDER__NORMAL_TOKEN
        #   [
        display_name                            = ':]'
        is_colon__right_square_bracket          = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_comprehension_expression      = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_multiply_expression           = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_python_arithmetic_expression  = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true


    class Comma_RightBrace(DualToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        #   {
        display_name = ',}'


    class Comma_RightParenthesis(DualToken):
        __slots__                             = (())
        class_order                           = CLASS_ORDER__NORMAL_TOKEN
        #   (
        display_name                          = ',)'
        is_comma__right_parenthesis           = true
        is_end_of_boolean_and_expression      = true
        is_end_of_boolean_or_expression       = true
        is_end_of_compare_expression          = true
        is_end_of_comprehension_expression    = true
        is_end_of_logical_and_expression      = true
        is_end_of_logical_or_expression       = true
        is_end_of_multiply_expression         = true
        is_end_of_normal_expression           = true
        is_end_of_python_arithmetic_expression= true
        is_end_of_ternary_expression          = true
        is_end_of_unary_expression            = true
        is__optional_comma__right_parenthesis = true


    class Comma_RightSquareBracket(DualToken):
        __slots__                                = (())
        class_order                              = CLASS_ORDER__NORMAL_TOKEN
        #   [
        display_name                             = ',]'
        is_end_of_boolean_and_expression         = true
        is_end_of_boolean_or_expression          = true
        is_end_of_compare_expression             = true
        is_end_of_comprehension_expression       = true
        is_end_of_logical_and_expression         = true
        is_end_of_logical_or_expression          = true
        is_end_of_multiply_expression            = true
        is_end_of_normal_expression              = true
        is_end_of_python_arithmetic_expression   = true
        is_end_of_ternary_expression             = true
        is_end_of_unary_expression               = true
        is__optional_comma__right_square_bracket = true


    class Dot_Name(DualToken):
        __slots__           = (())
        #   [
        class_order         = CLASS_ORDER__NORMAL_TOKEN
        display_name        = '.name'
        is_postfix_operator = true


        def mutate(t, vary, priority):
            a = t.a
            b = t.b

            a__2 = a.transform(vary)
            b__2 = b.transform(vary)

            if (a is a__2) and (b is b__2):
                return t

            return conjure_dot_name(a__2, b__2)


    class DotNamePair(DualToken):
        __slots__           = (())
        class_order         = CLASS_ORDER__NORMAL_TOKEN
        #   [
        display_name        = '.name-pair'
        is_postfix_operator = true


    class EmptyList(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = '[,]'
        is__atom__or__special_operator = true
        is_atom                        = true

        scout_variables = scout_variables__0


    class EmptyMap(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = '{:}'
        is__atom__or__special_operator = true
        is_atom                        = true

        scout_variables = scout_variables__0


    class EmptyTuple(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = '{,}'
        is__atom__or__special_operator = true
        is_atom                        = true

        scout_variables = scout_variables__0


    class Indented_Token(DualToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__INDENTED_TOKEN
        display_name = 'indented-token'


        indentation = DualToken.a
        token       = DualToken.b


        def display_token(t):
            return arrange('<+%d {%s}>', t.indentation.total, portray_string(t.token.s)[1:-1])


    @share
    class Is_Not(DualToken):
        __slots__                               = (())
        class_order                             = CLASS_ORDER__NORMAL_TOKEN
        display_name                            = 'is-not'
        is_compare_operator                     = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_python_arithmetic_expression  = true
        is_end_of_unary_expression              = true


    class LeftSquareBracket_Colon(DualToken):
        __slots__           = (())
        class_order         = CLASS_ORDER__NORMAL_TOKEN
        display_name        = '[:'                             #   ]
        is_postfix_operator = true
        is_tail_index       = true


    class Name_Whitespace(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'name+whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true

        scout_variables = scout_variables__a
        write_variables = write_variables__a


    @share
    class Not_In(DualToken):
        __slots__                              = (())
        class_order                            = CLASS_ORDER__NORMAL_TOKEN
        display_name                           = 'not-in'
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_python_arithmetic_expression = true
        is_end_of_unary_expression             = true


    class Parameters_0(DualToken):
        __slots__       = (())
        class_order     = CLASS_ORDER__PARAMETERS_0
        display_name    = 'parameters-(0)'
        is_parameters_0 = true


        add_parameters     = add_parameters__0
        parameters_1_named = parameters_1_named__false
        scout_variables    = scout_variables__0


    class Whitespace_Atom(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'whitespace+atom'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_special_operator            = false


        def find_atom(t):
            return t.b


        scout_variables = scout_variables__0


    class Whitespace_Name(DualToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'whitespace+name'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true
        is_special_operator            = false


        add_parameters = add_parameters__b


        def mutate(t, vary, priority):
            if vary.remove_comments:
                return t.b

            return t


        scout_default_values = scout_default_values__b
        scout_variables      = scout_variables__b


        def transform(t, vary):
            if vary.remove_comments:
                return t.b

            return t


        write_variables = write_variables__b


    conjure_atom_whitespace = produce_conjure_dual_token('atom_whitespace', Atom_Whitespace)

    conjure_arguments_0 = produce_conjure_dual_token(
                              'arguments_0',
                              Arguments_0,

                              lookup  = lookup_arguments_0_token,
                              provide = provide_arguments_0_token,
                          )

    conjure_colon__line_marker = produce_conjure_dual_token(
                                     'colon__line_marker__1',
                                     Colon_LineMarker_1,

                                     line_marker = true,
                                 )

    conjure_colon__right_square_bracket = produce_conjure_dual_token(
                                              'colon__right_square_bracket',
                                              Colon_RightSquareBracket,
                                          )

    conjure__comma__right_brace      = produce_conjure_dual_token('comma__right_brace',       Comma_RightBrace)
    conjure_comma__right_parenthesis = produce_conjure_dual_token('comma__right_parenthesis', Comma_RightParenthesis)

    conjure_comma__right_square_bracket = produce_conjure_dual_token(
                                              'comma__right_square_bracket',
                                              Comma_RightSquareBracket,
                                          )

    conjure_dot_name      = produce_conjure_dual_token('.name',       Dot_Name)
    conjure_dot_name_pair = produce_conjure_dual_token('.name-pair',  DotNamePair)
    conjure_empty_list    = produce_conjure_dual_token('[]',          EmptyList)
    conjure_empty_map     = produce_conjure_dual_token('{}',          EmptyMap)
    conjure_empty_tuple   = produce_conjure_dual_token('empty-tuple', EmptyTuple)

    conjure_indented_token = produce_conjure_dual_token(
                                 'indented-token',
                                 Indented_Token,

                                 lookup  = lookup_indentation,
                                 provide = provide_indentation,
                             )

    conjure_is_not = produce_conjure_dual_token('is-not', Is_Not)

    conjure_left_square_bracket__colon = produce_conjure_dual_token(
                                             '[:',                           #   ]
                                             LeftSquareBracket_Colon,
                                         )

    conjure_name_whitespace = produce_conjure_dual_token('name_whitespace', Name_Whitespace)

    conjure_not_in = produce_conjure_dual_token('not-in', Not_In)

    conjure_parameters_0 = produce_conjure_dual_token(
                               'parameters_0',
                               Parameters_0,

                               lookup  = lookup_parameters_0_token,
                               provide = provide_parameters_0_token,
                          )

    conjure_whitespace_atom = produce_conjure_dual_token('whitespace_atom', Whitespace_Atom)
    conjure_whitespace_name = produce_conjure_dual_token('whitespace_name', Whitespace_Name)

    evoke_arguments_0 = produce_evoke_dual_token__ends_in_newline(
                            'arguments_0',
                            Arguments_0,
                            conjure_left_parenthesis,
                            conjure_right_parenthesis,
                            conjure_right_parenthesis__ends_in_newline,

                            lookup  = lookup_arguments_0_token,
                            provide = provide_arguments_0_token,
                        )

    evoke_colon__line_marker = produce_evoke_dual_token__line_marker(
                                   'colon__line_marker',
                                   Colon_LineMarker_1,
                                   conjure_colon,
                               )

    evoke__colon__right_square_bracket = produce_evoke_dual_token__ends_in_newline(
                                             'colon__right_square_bracket',
                                             Colon_RightSquareBracket,
                                             conjure_colon,
                                             conjure_right_square_bracket,
                                             conjure_right_square_bracket__ends_in_newline,
                                         )

    evoke__comma__right_brace = produce_evoke_dual_token__ends_in_newline(
                                    'comma__right_brace',
                                    Comma_RightBrace,
                                    conjure_comma,
                                    conjure_right_brace,
                                    conjure_right_brace__ends_in_newline,
                                )

    evoke_comma__right_parenthesis = produce_evoke_dual_token__ends_in_newline(
                                         'comma__right_parenthesis',
                                         Comma_RightParenthesis,
                                         conjure_comma,
                                         conjure_right_parenthesis,
                                         conjure_right_parenthesis__ends_in_newline,
                                     )

    evoke__comma__right_square_bracket = produce_evoke_dual_token__ends_in_newline(
                                             'comma__right_square_bracket',
                                             Comma_RightSquareBracket,
                                             conjure_comma,
                                             conjure_right_square_bracket,
                                             conjure_right_square_bracket__ends_in_newline,
                                         )

    evoke__double_quote__whitespace = produce_evoke_dual_token__ends_in_newline(
                                          'double-quote+whitespace',
                                          Atom_Whitespace,
                                          conjure_double_quote,
                                          conjure_whitespace,
                                          conjure_whitespace__ends_in_newline,
                                      )

    evoke_empty_list = produce_evoke_dual_token__ends_in_newline(
                           '[]',
                           EmptyList,
                           conjure_left_square_bracket,
                           conjure_right_square_bracket,
                           conjure_right_square_bracket__ends_in_newline,
                       )

    evoke_empty_map = produce_evoke_dual_token__ends_in_newline(
                          '{}',
                          EmptyMap,
                          conjure_left_brace,
                          conjure_right_brace,
                          conjure_right_brace__ends_in_newline,
                      )

    evoke_empty_tuple = produce_evoke_dual_token__ends_in_newline(
                            '()',
                            EmptyTuple,
                            conjure_left_parenthesis,
                            conjure_right_parenthesis,
                            conjure_right_parenthesis__ends_in_newline,
                        )

    evoke_indented_assert = produce_evoke_dual_token__indentation(
                                'indented-assert',
                                Indented_Token,
                                conjure_indentation,
                                conjure_keyword_assert,
                            )

    evoke_indented__at_sign = produce_evoke_dual_token__indentation(
                                  'indented-at-sign',
                                  Indented_Token,
                                  conjure_indentation,
                                  conjure_at_sign,
                              )

    evoke_indented_class = produce_evoke_dual_token__indentation(
                               'indented-class',
                               Indented_Token,
                               conjure_indentation,
                               conjure_keyword_class,
                           )

    evoke_indented_delete = produce_evoke_dual_token__indentation(
                                'indented-delete',
                                Indented_Token,
                                conjure_indentation,
                                conjure_keyword_delete,
                            )

    evoke_indented_else_if = produce_evoke_dual_token__indentation(
                                 'indented-else-if',
                                 Indented_Token,
                                 conjure_indentation,
                                 conjure_keyword_else_if,
                             )

    evoke_indented_except = produce_evoke_dual_token__indentation(
                                'indented-except',
                                Indented_Token,
                                conjure_indentation,
                                conjure_keyword_from,
                            )

    evoke_indented_from = produce_evoke_dual_token__indentation(
                              'indented-from',
                              Indented_Token,
                              conjure_indentation,
                              conjure_keyword_from,
                          )

    evoke_indented_for = produce_evoke_dual_token__indentation(
                             'indented-for',
                             Indented_Token,
                             conjure_indentation,
                             conjure_keyword_for,
                         )

    evoke_indented_function = produce_evoke_dual_token__indentation(
                                  'indented-function',
                                  Indented_Token,
                                  conjure_indentation,
                                  conjure_keyword_function,
                              )

    evoke_indented_if = produce_evoke_dual_token__indentation(
                            'indented-if',
                            Indented_Token,
                            conjure_indentation,
                            conjure_keyword_if,
                        )

    evoke_indented_import = produce_evoke_dual_token__indentation(
                                'indented-import',
                                Indented_Token,
                                conjure_indentation,
                                conjure_keyword_import,
                            )

    evoke_indented_raise = produce_evoke_dual_token__indentation(
                               'indented-raise',
                               Indented_Token,
                               conjure_indentation,
                               conjure_keyword_raise,
                           )

    evoke_indented_return = produce_evoke_dual_token__indentation(
                                'indented-return',
                                Indented_Token,
                                conjure_indentation,
                                conjure_keyword_return,
                            )

    evoke_indented_while = produce_evoke_dual_token__indentation(
                               'indented-while',
                               Indented_Token,
                               conjure_indentation,
                               conjure_keyword_while,
                           )

    evoke_indented_with = produce_evoke_dual_token__indentation(
                              'indented-with',
                              Indented_Token,
                              conjure_indentation,
                              conjure_keyword_with,
                          )

    evoke_indented_yield = produce_evoke_dual_token__indentation(
                               'indented-yield',
                               Indented_Token,
                               conjure_indentation,
                               conjure_keyword_yield,
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
                                  conjure_number,
                                  conjure_whitespace,
                                  conjure_whitespace__ends_in_newline,
                              )

    evoke_is_not = produce_evoke_dual_token__ends_in_newline(
                       'is_not',
                       Is_Not,
                       conjure_keyword_is,
                       conjure_keyword_not,
                       conjure_keyword_not__ends_in_newline,
                   )

    evoke__left_square_bracket__colon = produce_evoke_dual_token__ends_in_newline(
                                            '[:',                           #   ]
                                            LeftSquareBracket_Colon,
                                            conjure_left_square_bracket,
                                            conjure_colon,
                                            conjure_colon__ends_in_newline,
                                        )

    evoke_not_in = produce_evoke_dual_token__ends_in_newline(
                       'not_in',
                       Not_In,
                       conjure_keyword_not,
                       conjure_keyword_in,
                       conjure_keyword_in__ends_in_newline,
                   )

    evoke_parameters_0 = produce_evoke_dual_token__ends_in_newline(
                             'parameters_0',
                             Parameters_0,
                             conjure_left_parenthesis,
                             conjure_right_parenthesis,
                             conjure_right_parenthesis__ends_in_newline,

                             lookup  = lookup_parameters_0_token,
                             provide = provide_parameters_0_token,
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
                                  conjure_number,
                              )

    evoke_whitespace__single_quote = produce_evoke_dual_token__whitespace(
                                         'whitespace+single-quote',
                                         Whitespace_Atom,
                                         conjure_whitespace,
                                         conjure_single_quote,
                                     )

    #
    #   Constants
    #
    ARGUMENTS_0         = conjure_arguments_0                (LP,         RP)
    COLON__LINE_MARKER  = conjure_colon__line_marker         (COLON,      LINE_MARKER)
    COLON_RSB           = conjure_colon__right_square_bracket(COLON,      RSB)
    COMMA_RSB           = conjure_comma__right_square_bracket(COMMA,      RSB)
    COMMA_RP            = conjure_comma__right_parenthesis   (COMMA,      RP)
    EMPTY_LIST          = conjure_empty_list                 (LSB,        RSB)
    EMPTY_MAP           = conjure_empty_map                  (LEFT_BRACE, RIGHT_BRACE)
    EMPTY_TUPLE         = conjure_empty_tuple                (LP,         RP)
    LSB_COLON           = conjure_left_square_bracket__colon (LSB,        COLON)
    PARAMETERS_0        = conjure_parameters_0               (LP,         RP)
    W__IS_NOT__W        = conjure_is_not                     (W__IS__W,   NOT__W)
    W__NOT_IN__W        = conjure_not_in                     (W__NOT__W,  IN__W)


    #
    #   .mutate
    #
    #   NOTE:
    #       Comma_RightParentheiss.mutate    leaves  the , (called on parenthesized tuple expression)
    #       Comma_RightParenthesis.transform removes the , (called in other situations where the , is not needed)
    #
    Arguments_0           .mutate = produce_mutate__uncommented   ('arguments_0',              ARGUMENTS_0)
    Atom_Whitespace       .mutate = produce_mutate_atom_whitespace('atom_whitespace',          conjure_atom_whitespace)
    Comma_RightParenthesis.mutate = produce_mutate__uncommented   ('comma__right_parenthesis', COMMA_RP)
    DotNamePair           .mutate = produce_mutate__ab            ('dot-name-pair',            conjure_dot_name_pair)
    EmptyList             .mutate = produce_mutate__uncommented   ('empty_list',               EMPTY_LIST)
    EmptyMap              .mutate = produce_mutate__uncommented   ('empty_map',                EMPTY_MAP)
    EmptyTuple            .mutate = produce_mutate__uncommented   ('empty_tuple',              EMPTY_TUPLE)
    Name_Whitespace       .mutate = produce_mutate_atom_whitespace('name_whitespace',          conjure_name_whitespace)
    Whitespace_Atom       .mutate = produce_mutate_whitespace_atom('whitespace_atom',          conjure_whitespace_atom)
    Whitespace_Name       .mutate = produce_mutate_whitespace_atom('whitespace_name',          conjure_whitespace_name)


    #
    #   .transform
    #
    Colon_LineMarker_1.transform = produce_transform__ab('colon__line_marker_1', conjure_colon__line_marker)

    Comma_RightBrace        .transform = produce_transform__uncommented('comma__right_brace',          RIGHT_BRACE)
    Colon_RightSquareBracket.transform = produce_transform__uncommented('colon__right_square_bracket', COLON_RSB)

    Comma_RightParenthesis.transform = produce_transform__uncommented(
                                           'comma__right_parenthesis',
                                           RP,                          #   See comment above on why not 'COMMA_RP'
                                       )

    Comma_RightSquareBracket.transform = produce_transform__uncommented('comma__right_square_bracket', COMMA_RSB)

    Indented_Token.transform = produce_transform__ab         ('indented_token', conjure_indented_token)
    Is_Not        .transform = produce_transform__uncommented('is_not',         W__IS_NOT__W)

    LeftSquareBracket_Colon.transform = produce_transform__uncommented('left_square_bracket__colon', LSB_COLON)

    Name_Whitespace.transform = produce_transform_atom_whitespace('name_whitespace', conjure_name_whitespace)
    Not_In         .transform = produce_transform__uncommented   ('not_in',          W__NOT_IN__W)
    Parameters_0   .transform = produce_transform__uncommented   ('parameters_0',    PARAMETERS_0)


    #
    #   find_*
    #
    find_evoke_comma_something = {
                                     #   (
                                     ')' : evoke_comma__right_parenthesis,

                                     #   [
                                     ']' : evoke__comma__right_square_bracket,
                                 }.__getitem__

    find_evoke_atom_whitespace = {
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

    find_evoke_whitespace_atom = {
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


    share(
        'COLON__LINE_MARKER',                       COLON__LINE_MARKER,
        'COLON_RSB',                                COLON_RSB,
        'COMMA_RP',                                 COMMA_RP,
        'conjure_arguments_0',                      conjure_arguments_0,
        'conjure_atom_whitespace',                  conjure_atom_whitespace,
        'conjure_colon__line_marker',               conjure_colon__line_marker,
        'conjure__comma__right_brace',              conjure__comma__right_brace,
        'conjure_comma__right_parenthesis',         conjure_comma__right_parenthesis,
        'conjure_comma__right_square_bracket',      conjure_comma__right_square_bracket,
        'conjure_dot_name',                         conjure_dot_name,
        'conjure_dot_name_pair',                    conjure_dot_name_pair,
        'conjure_empty_list',                       conjure_empty_list,
        'conjure_empty_map',                        conjure_empty_map,
        'conjure_empty_tuple',                      conjure_empty_tuple,
        'conjure_indented_token',                   conjure_indented_token,
        'conjure_is_not',                           conjure_is_not,
        'conjure_not_in',                           conjure_not_in,
        'conjure_parameters_0',                     conjure_parameters_0,
        'evoke_arguments_0',                        evoke_arguments_0,
        'evoke_colon__line_marker',                 evoke_colon__line_marker,
        'evoke__colon__right_square_bracket',       evoke__colon__right_square_bracket,
        'evoke__comma__right_brace',                evoke__comma__right_brace,
        'evoke_comma__right_parenthesis',           evoke_comma__right_parenthesis,
        'evoke_empty_list',                         evoke_empty_list,
        'evoke_empty_map',                          evoke_empty_map,
        'evoke_empty_tuple',                        evoke_empty_tuple,
        'evoke_indented_assert',                    evoke_indented_assert,
        'evoke_indented__at_sign',                  evoke_indented__at_sign,
        'evoke_indented_class',                     evoke_indented_class,
        'evoke_indented_delete',                    evoke_indented_delete,
        'evoke_indented_else_if',                   evoke_indented_else_if,
        'evoke_indented_except',                    evoke_indented_except,
        'evoke_indented_for',                       evoke_indented_for,
        'evoke_indented_from',                      evoke_indented_from,
        'evoke_indented_function',                  evoke_indented_function,
        'evoke_indented_if',                        evoke_indented_if,
        'evoke_indented_import',                    evoke_indented_import,
        'evoke_indented_raise',                     evoke_indented_raise,
        'evoke_indented_return',                    evoke_indented_return,
        'evoke_indented_while',                     evoke_indented_while,
        'evoke_indented_with',                      evoke_indented_with,
        'evoke_indented_yield',                     evoke_indented_yield,
        'evoke_is_not',                             evoke_is_not,
        'evoke__left_square_bracket__colon',        evoke__left_square_bracket__colon,
        'evoke_name_whitespace',                    evoke_name_whitespace,
        'evoke_not_in',                             evoke_not_in,
        'evoke_parameters_0',                       evoke_parameters_0,
        'evoke_whitespace_name',                    evoke_whitespace_name,
        'find_evoke_atom_whitespace',               find_evoke_atom_whitespace,
        'find_evoke_comma_something',               find_evoke_comma_something,
        'find_evoke_whitespace_atom',               find_evoke_whitespace_atom,
        'LSB_COLON',                                LSB_COLON,
    )

#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.DualToken')
def module():
    require_module('PythonParser.ClassOrder')
    require_module('PythonParser.CreateMeta')
    require_module('PythonParser.Elemental')
    require_module('PythonParser.TokenCache')


    def construct_dual_token__line_marker_1(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s
        assert s.count('\n') is 1
        assert b.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b


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


    class Arguments_0(DualToken):
        __slots__                             = (())
        class_order                           = CLASS_ORDER__ARGUMENT_0
        display_name                          = 'arguments-(0)'
        is__arguments_0__or__left_parenthesis = true
        is_arguments_0                        = true
        is_postfix_operator                   = true

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
        is_end_of_PYTHON_arithmetic_expression  = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true
        line_marker                             = true
        newlines                                = 1

        __init__       = construct_dual_token__line_marker_1
        count_newlines = count_newlines__line_marker


    class Colon_RightSquareBracket(DualToken):
        __slots__ = (())

        #   [
        display_name = ':]'

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
        is_end_of_PYTHON_arithmetic_expression  = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true


    class Comma_RightBrace(DualToken):
        __slots__ = (())

        #   {
        display_name = ',}'

        is_end_of_boolean_and_expression       = true
        is_end_of_boolean_or_expression        = true
        is_end_of_compare_expression           = true
        is_end_of_comprehension_expression     = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_ternary_expression           = true
        is_end_of_unary_expression             = true
        is__optional_comma__right_brace        = true


    class Comma_RightParenthesis(DualToken):
        __slots__  = (())

        #   (
        display_name = ',)'

        is_comma__right_parenthesis           = true
        is_end_of_boolean_and_expression      = true
        is_end_of_boolean_or_expression       = true
        is_end_of_compare_expression          = true
        is_end_of_comprehension_expression    = true
        is_end_of_logical_and_expression      = true
        is_end_of_logical_or_expression       = true
        is_end_of_multiply_expression         = true
        is_end_of_normal_expression           = true
        is_end_of_PYTHON_arithmetic_expression= true
        is_end_of_ternary_expression          = true
        is_end_of_unary_expression            = true
        is__optional_comma__right_parenthesis = true


    class Comma_RightSquareBracket(DualToken):
        __slots__ = (())

        #   [
        display_name = ',]'

        is_end_of_boolean_and_expression         = true
        is_end_of_boolean_or_expression          = true
        is_end_of_compare_expression             = true
        is_end_of_comprehension_expression       = true
        is_end_of_logical_and_expression         = true
        is_end_of_logical_or_expression          = true
        is_end_of_multiply_expression            = true
        is_end_of_normal_expression              = true
        is_end_of_PYTHON_arithmetic_expression   = true
        is_end_of_ternary_expression             = true
        is_end_of_unary_expression               = true
        is__optional_comma__right_square_bracket = true


    class Dot_Name(DualToken):
        __slots__           = (())
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
        display_name        = '.name-pair'
        is_postfix_operator = true


    class EmptyList(DualToken):
        __slots__    = (())
        display_name = '[,]'

        is_CRYSTAL_atom                                  = true
        is_CRYSTAL_simple_atom__or__colon                = true
        is_CRYSTAL_simple_atom__or__right_brace          = true
        is_CRYSTAL_simple_atom__or__right_parenthesis    = true
        is_CRYSTAL_simple_atom__or__right_square_bracket = true

        is_CRYSTAL_right_parenthesis = false


        scout_variables = scout_variables__0


    class EmptyMap(DualToken):
        __slots__    = (())
        display_name = '{:}'

        is_CRYSTAL_atom                                  = true
        is_CRYSTAL_simple_atom__or__colon                = true
        is_CRYSTAL_simple_atom__or__right_brace          = true
        is_CRYSTAL_simple_atom__or__right_parenthesis    = true
        is_CRYSTAL_simple_atom__or__right_square_bracket = true

        is_CRYSTAL_right_parenthesis = false


        scout_variables = scout_variables__0


    class EmptyTuple(DualToken):
        __slots__    = (())
        display_name = '{,}'

        is_CRYSTAL_atom                                  = true
        is_CRYSTAL_simple_atom__or__colon                = true
        is_CRYSTAL_simple_atom__or__right_brace          = true
        is_CRYSTAL_simple_atom__or__right_parenthesis    = true
        is_CRYSTAL_simple_atom__or__right_square_bracket = true

        is_CRYSTAL_right_parenthesis = false


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
        display_name                            = 'is-not'
        is_compare_operator                     = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_PYTHON_arithmetic_expression  = true
        is_end_of_unary_expression              = true


    class LeftSquareBracket_Colon(DualToken):
        __slots__           = (())
        display_name        = '[:'                             #   ]
        is_postfix_operator = true
        is_tail_index       = true


    @share
    class Not_In(DualToken):
        __slots__                              = (())
        display_name                           = 'not-in'
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


    class Parameters_0(DualToken):
        __slots__       = (())
        class_order     = CLASS_ORDER__PARAMETERS_0
        display_name    = 'parameters-(0)'
        is_parameters_0 = true


        add_parameters     = add_parameters__0
        parameters_1_named = parameters_1_named__false
        scout_variables    = scout_variables__0


    #
    #   conjure
    #
    conjure_arguments_0 = produce_conjure_dual_token__normal(
            'arguments_0',
            Arguments_0,

            lookup  = lookup_arguments_0_token,
            provide = provide_arguments_0_token,
        )

    conjure_colon__line_marker = produce_conjure_dual_token__line_marker('colon__line_marker__1', Colon_LineMarker_1)

    conjure_colon__right_square_bracket = produce_conjure_dual_token__normal(
            'colon__right_square_bracket',
            Colon_RightSquareBracket,
        )

    conjure__comma__right_brace = produce_conjure_dual_token__normal('comma__right_brace', Comma_RightBrace)

    conjure_comma__right_parenthesis = produce_conjure_dual_token__normal(
            'comma__right_parenthesis',
            Comma_RightParenthesis,
        )

    conjure_comma__right_square_bracket = produce_conjure_dual_token__normal(
            'comma__right_square_bracket',
            Comma_RightSquareBracket,
        )

    conjure_dot_name      = produce_conjure_dual_token__normal('.name',       Dot_Name)
    conjure_dot_name_pair = produce_conjure_dual_token__normal('.name-pair',  DotNamePair)
    conjure_empty_list    = produce_conjure_dual_token__normal('[]',          EmptyList)
    conjure_empty_map     = produce_conjure_dual_token__normal('{}',          EmptyMap)
    conjure_empty_tuple   = produce_conjure_dual_token__normal('empty-tuple', EmptyTuple)

    conjure_indented_token = produce_conjure_dual_token__normal(
            'indented-token',
            Indented_Token,

            lookup  = lookup_indentation,
            provide = provide_indentation,
        )

    conjure_is_not = produce_conjure_dual_token__normal('is-not', Is_Not)

    conjure_left_square_bracket__colon = produce_conjure_dual_token__normal(
            '[:',                           #   ]
            LeftSquareBracket_Colon,
        )

    conjure_not_in = produce_conjure_dual_token__normal('not-in', Not_In)

    conjure_parameters_0 = produce_conjure_dual_token__normal(
            'parameters_0',
            Parameters_0,

            lookup  = lookup_parameters_0_token,
            provide = provide_parameters_0_token,
        )


    #
    #   evoke
    #
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
                                    conjure_CRYSTAL_comma,
                                    conjure_right_brace,
                                    conjure_right_brace__ends_in_newline,
                                )

    evoke_comma__right_parenthesis = produce_evoke_dual_token__ends_in_newline(
                                         'comma__right_parenthesis',
                                         Comma_RightParenthesis,
                                         conjure_CRYSTAL_comma,
                                         conjure_right_parenthesis,
                                         conjure_right_parenthesis__ends_in_newline,
                                     )

    evoke__comma__right_square_bracket = produce_evoke_dual_token__ends_in_newline(
                                             'comma__right_square_bracket',
                                             Comma_RightSquareBracket,
                                             conjure_CRYSTAL_comma,
                                             conjure_right_square_bracket,
                                             conjure_right_square_bracket__ends_in_newline,
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


    #
    #   Constants
    #
    ARGUMENTS_0         = conjure_arguments_0                (LEFT_PARENTHESIS, RIGHT_PARENTHESIS)
    COLON__LINE_MARKER  = conjure_colon__line_marker         (COLON,            LINE_MARKER)
    COLON_RSB           = conjure_colon__right_square_bracket(COLON,            RSB)
    COMMA_RSB           = conjure_comma__right_square_bracket(COMMA,            RSB)
    COMMA_RP            = conjure_comma__right_parenthesis   (COMMA,            RIGHT_PARENTHESIS)
    EMPTY_LIST          = conjure_empty_list                 (LSB,              RSB)
    EMPTY_MAP           = conjure_empty_map                  (LEFT_BRACE,       RIGHT_BRACE)
    EMPTY_TUPLE         = conjure_empty_tuple                (LEFT_PARENTHESIS, RIGHT_PARENTHESIS)
    LSB_COLON           = conjure_left_square_bracket__colon (LSB,              COLON)
    PARAMETERS_0        = conjure_parameters_0               (LEFT_PARENTHESIS, RIGHT_PARENTHESIS)
    W__IS_NOT__W        = conjure_is_not                     (W__IS__W,         NOT__W)
    W__NOT_IN__W        = conjure_not_in                     (W__NOT__W,        IN__W)


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
                                           RIGHT_PARENTHESIS,           #   See comment above on why not 'COMMA_RP'
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
    find_evoke_PYTHON__comma_something = {
            #   (
            ')' : evoke_comma__right_parenthesis,

            #   [
            ']' : evoke__comma__right_square_bracket,

            #   {
            '}' : evoke__comma__right_brace,
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
        'evoke_not_in',                             evoke_not_in,
        'evoke_parameters_0',                       evoke_parameters_0,
        'find_evoke_PYTHON__comma_something',       find_evoke_PYTHON__comma_something,
        'LSB_COLON',                                LSB_COLON,
    )

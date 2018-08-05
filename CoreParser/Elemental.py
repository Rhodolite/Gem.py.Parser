#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Elemental')
def module():
    require_module('CoreParser.ActionWord')
    require_module('CoreParser.Atom')
    require_module('CoreParser.ClassOrder')


    @export
    class KeywordAndOperatorBase(ParserToken):
        __slots__ = (())

        class_order = CLASS_ORDER__NORMAL_TOKEN


        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = false
            is_CRYSTAL_left_parenthesis                      = false
            is_CRYSTAL_right_parenthesis                     = false
            is_CRYSTAL_simple_atom__or__colon                = false
            is_CRYSTAL_simple_atom__or__right_brace          = false
            is_CRYSTAL_simple_atom__or__right_parenthesis    = false
            is_CRYSTAL_simple_atom__or__right_square_bracket = false

        if CRYSTAL_parser:
            is_CRYSTAL_comma = false


        if PYTHON_parser:
            is_all_index                             = false
            is_arguments_0                           = false
            is__arguments_0__or__left_parenthesis    = false
            is_colon                                 = false
            is_colon__line_marker                    = false
            is_colon__right_square_bracket           = false
            is__comma__or__right_parenthesis         = false
            is_comma__right_parenthesis              = false
            is_comma__right_square_bracket           = false
            is_compare_operator                      = false
            is_dot                                   = false
            is_end_of_boolean_and_expression         = false
            is_end_of_boolean_or_expression          = false
            is_end_of_compare_expression             = false
            is_end_of_comprehension_expression       = false
            is_end_of_comprehension_expression_list  = false
            is_end_of_logical_and_expression         = false
            is_end_of_logical_or_expression          = false
            is_end_of_multiply_expression            = false
            is_end_of_normal_expression              = false
            is_end_of_normal_expression_list         = false
            is_end_of_PYTHON_arithmetic_expression   = false
            is_end_of_ternary_expression             = false
            is_end_of_ternary_expression_list        = false
            is_end_of_unary_expression               = false
            is_equal_sign                            = false
            is_keyword_and                           = false
            is_keyword_as                            = false
            is_keyword_else                          = false
            is_keyword_for                           = false
            is_keyword_if                            = false
            is_keyword_in                            = false
            is_keyword_not                           = false
            is_keyword_or                            = false
            is_keyword_return                        = false
            is_left_brace                            = false
            is_left_square_bracket                   = false
            is_logical_and_operator                  = false
            is_logical_or_operator                   = false
            is_minus_sign                            = false
            is_modify_operator                       = false
            is_multiply_operator                     = false
            is__optional_comma__right_parenthesis    = false
            is__optional_comma__right_square_bracket = false
            is_parameters_0                          = false
            is_postfix_operator                      = false
            is_power_operator                        = false
            is_PYTHON_arithmetic_operator            = false
            is_right_brace                           = false
            is_right_square_bracket                  = false
            is_star_sign                             = false
            is_tail_index                            = false
            is_tilde_sign                            = false


        if TREMOLITE_parser:
            is_end_of_TREMOLITE_arithmetic_expression     = false
            is_end_of_TREMOLITE_or_expression             = false
            is_end_of_TREMOLITE_range_expression          = false
            is_end_of_TREMOLITE_unary_expression          = false
            is_TREMOLITE_arithmetic_operator              = false
            is_TREMOLITE_left_brace_set                   = false
            is_TREMOLITE__optional_comma__right_brace_set = false
            is_TREMOLITE_range_operator                   = false
            is_TREMOLITE_right_brace_set                  = false


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, portray_string(t.s))


        def display_short_token(t):
            return arrange('{%s}', portray_string(t.s)[1:-1])


        display_token = display_short_token


    if JAVA_parser or PYTHON_parser:
        @export
        class KeywordImport(KeywordAndOperatorBase):
            __slots__    = (())
            display_name = 'import'


        if JAVA_parser:
            [
                    conjure_keyword_import, conjure_keyword_import__ends_in_newline,
            ] = produce_conjure_action_word__ends_in_newline('keyword_import', KeywordImport)
        else:
            conjure_keyword_import = produce_conjure_action_word__normal('keyword_import', KeywordImport)


        export(
            'conjure_keyword_import',   conjure_keyword_import,
        )


        if JAVA_parser:
            export(
                'conjure_keyword_import__ends_in_newline',  conjure_keyword_import__ends_in_newline,
            )


    if TREMOLITE_parser:
        #
        #   Tremolite Parser
        #
        @export
        class KeywordLanguage(KeywordAndOperatorBase):
            __slots__    = (())
            display_name = 'language'


        conjure_keyword_language = produce_conjure_action_word__normal('keyword_language', KeywordLanguage)

        export(
            'conjure_keyword_language',     conjure_keyword_language,
        )


    if PYTHON_parser or TREMOLITE_parser:
        @export
        class OperatorComma(KeywordAndOperatorBase):
            __slots__      = (())
            display_name   = ','
            frill_estimate = 1

            if CRYSTAL_parser:
                is_CRYSTAL_comma = true

            if PYTHON_parser:
                is__comma__or__right_parenthesis       = true
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

            if TREMOLITE_parser:
                is_end_of_TREMOLITE_arithmetic_expression = true
                is_end_of_TREMOLITE_or_expression         = true
                is_end_of_TREMOLITE_range_expression      = true
                is_end_of_TREMOLITE_unary_expression      = true

        [
                conjure_CRYSTAL_comma, conjure_CRYSTAL_comma__ends_in_newline,
        ] = produce_conjure_action_word__ends_in_newline('comma', OperatorComma)


        export(
            'conjure_CRYSTAL_comma',                    conjure_CRYSTAL_comma,
            'conjure_CRYSTAL_comma__ends_in_newline',   conjure_CRYSTAL_comma__ends_in_newline,
        )


    if PYTHON_parser or TREMOLITE_parser:
        @export
        class OperatorLeftParenthesis(KeywordAndOperatorBase):
            __slots__    = (())
            display_name = '('                                          #   )


            if CRYSTAL_parser:
                #
                #   Not strictly needed here; for optimization, so does not have to look in base classes
                #
                is_CRYSTAL_atom = false

            if CRYSTAL_parser:
                is_CRYSTAL_left_parenthesis = true

            if PYTHON_parser:
                is__arguments_0__or__left_parenthesis = true
                is_postfix_operator                   = true


        [
            conjure_left_parenthesis, conjure_left_parenthesis__ends_in_newline,
        ] = produce_conjure_action_word__ends_in_newline('left_parenthesis', OperatorLeftParenthesis)


        LEFT_PARENTHESIS = conjure_left_parenthesis('(')

        export(
            'conjure_left_parenthesis',                     conjure_left_parenthesis,
            'conjure_left_parenthesis__ends_in_newline',    conjure_left_parenthesis__ends_in_newline,
            'LEFT_PARENTHESIS',                             LEFT_PARENTHESIS,
        )


    if PYTHON_parser or TREMOLITE_parser:
        @export
        class OperatorPlusSign(KeywordAndOperatorBase):
            __slots__    = (())
            display_name = '+'


            if PYTHON_parser:
                is_end_of_multiply_expression = true
                is_end_of_unary_expression    = true
                is_PYTHON_arithmetic_operator = true


            if TREMOLITE_parser:
                is_end_of_TREMOLITE_range_expression = true
                is_end_of_TREMOLITE_unary_expression = true
                is_TREMOLITE_arithmetic_operator     = true


    if PYTHON_parser or TREMOLITE_parser:
        @export
        class OperatorRightParenthesis(KeywordAndOperatorBase):
            __slots__ = (())

            #  (
            display_name                     = ')'

            if CRYSTAL_parser:
                is_CRYSTAL_simple_atom__or__right_parenthesis = true

            if CRYSTAL_parser:
                is_CRYSTAL_right_parenthesis = true

            if PYTHON_parser:
                is__comma__or__right_parenthesis        = true
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
                is__optional_comma__right_parenthesis   = true

            if TREMOLITE_parser:
                is_end_of_TREMOLITE_arithmetic_expression = true
                is_end_of_TREMOLITE_or_expression         = true
                is_end_of_TREMOLITE_range_expression      = true
                is_end_of_TREMOLITE_unary_expression      = true


        [
            conjure_right_parenthesis, conjure_right_parenthesis__ends_in_newline,
        ] = produce_conjure_action_word__ends_in_newline('right_parenthesis', OperatorRightParenthesis)


        RIGHT_PARENTHESIS = conjure_right_parenthesis(')')


        export(
            'conjure_right_parenthesis',                    conjure_right_parenthesis,
            'conjure_right_parenthesis__ends_in_newline',   conjure_right_parenthesis__ends_in_newline,
            'RIGHT_PARENTHESIS',                            RIGHT_PARENTHESIS,
        )


    if PYTHON_parser or TREMOLITE_parser:
        initialize_action_word__Meta(
            ((
                 ((     '(',        OperatorLeftParenthesis     )),
                 ((     ')',        OperatorRightParenthesis    )),
                 ((     '+',        OperatorPlusSign            )),
            )),
        )


    #
    #   is_CRYSTAL_close_or_open_operator
    #
    if CRYSTAL_parser:
        if PYTHON_parser:
            is_CRYSTAL_close_or_open_operator = {
                    #   {[(
                    ')' : 7,
                    ']' : 7,
                    '}' : 7,
                }.get
        
        if TREMOLITE_parser:
            is_CRYSTAL_close_or_open_operator = {
                    '(' : 3,
                    ')' : 7,
                    '{|' : 3,
                    '|}' : 7,
                }.get


        export(
            'is_CRYSTAL_close_or_open_operator',    is_CRYSTAL_close_or_open_operator,
        )

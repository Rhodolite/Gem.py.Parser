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


        if capital_global.crystal_parser:
            is__atom__or__special_operator = false


        if capital_global.python_parser:
            is_all_index                               = false
            is_arguments_0                             = false
            is__arguments_0__or__left_parenthesis      = false
            is_atom                                    = false
            is_colon                                   = false
            is_colon__line_marker                      = false
            is_colon__right_square_bracket             = false
            is_comma                                   = false
            is__comma__or__right_parenthesis           = false
            is_comma__right_parenthesis                = false
            is_comma__right_square_bracket             = false
            is_compare_operator                        = false
            is_dot                                     = false
            is_end_of_boolean_and_expression           = false
            is_end_of_boolean_or_expression            = false
            is_end_of_compare_expression               = false
            is_end_of_comprehension_expression         = false
            is_end_of_comprehension_expression_list    = false
            is_end_of_logical_and_expression           = false
            is_end_of_logical_or_expression            = false
            is_end_of_multiply_expression              = false
            is_end_of_normal_expression                = false
            is_end_of_normal_expression_list           = false
            is_end_of_python_arithmetic_expression     = false
            is_end_of_ternary_expression               = false
            is_end_of_ternary_expression_list          = false
            is_end_of_unary_expression                 = false
            is_equal_sign                              = false
            is_keyword_and                             = false
            is_keyword_as                              = false
            is_keyword_else                            = false
            is_keyword_for                             = false
            is_keyword_if                              = false
            is_keyword_in                              = false
            is_keyword_not                             = false
            is_keyword_or                              = false
            is_keyword_return                          = false
            is_left_brace                              = false
            is_left_parenthesis                        = false
            is_left_square_bracket                     = false
            is_logical_and_operator                    = false
            is_logical_or_operator                     = false
            is_minus_sign                              = false
            is_modify_operator                         = false
            is_multiply_operator                       = false
            is__optional_comma__right_parenthesis      = false
            is__optional_comma__right_square_bracket   = false
            is_parameters_0                            = false
            is_postfix_operator                        = false
            is_power_operator                          = false
            is_python_arithmetic_operator              = false
            is_right_brace                             = false
            is_right_parenthesis                       = false
            is_right_square_bracket                    = false
            is_special_operator                        = false
            is_star_sign                               = false
            is_tail_index                              = false
            is_tilde_sign                              = false


        if capital_global.tremolite_parser:
            is_end_of_tremolite_arithmetic_expression = false
            is_end_of_tremolite_range_expression      = false
            is_end_of_tremolite_unary_expression      = false
            is_tremolite_arithmetic_operator          = false
            is_tremolite_range_operator               = false


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, portray_string(t.s))


        def display_short_token(t):
            return arrange('{%s}', portray_string(t.s)[1:-1])


        display_token = display_short_token


    if (capital_global.java_parser) or (capital_global.python_parser):
        @export
        class KeywordImport(KeywordAndOperatorBase):
            __slots__    = (())
            class_order  = CLASS_ORDER__NORMAL_TOKEN
            display_name = 'import'
            keyword      = 'import'


        if capital_global.java_parser:
            [
                    conjure_keyword_import, conjure_keyword_import__ends_in_newline,
            ] = produce_conjure_action_word('keyword_import', KeywordImport, produce_ends_in_newline = true)
        else:
            conjure_keyword_import = produce_conjure_action_word('keyword_import', KeywordImport)


        export(
            'conjure_keyword_import',   conjure_keyword_import,
        )


        if capital_global.java_parser:
            export(
                'conjure_keyword_import__ends_in_newline',  conjure_keyword_import__ends_in_newline,
            )


    if capital_global.tremolite_parser:
        #
        #   Tremolite Parser
        #
        @export
        class KeywordLanguage(KeywordAndOperatorBase):
            __slots__    = (())
            class_order  = CLASS_ORDER__NORMAL_TOKEN
            display_name = 'language'
            keyword      = 'language'


        conjure_keyword_language = produce_conjure_action_word('keyword_language', KeywordLanguage)

        export(
            'conjure_keyword_language',     conjure_keyword_language,
        )


    if (capital_global.python_parser) or (capital_global.tremolite_parser):
        @export
        class OperatorPlusSign(KeywordAndOperatorBase):
            __slots__                     = (())
            class_order                   = CLASS_ORDER__NORMAL_TOKEN
            display_name                  = '+'
            keyword                       = '+'


            if capital_global.python_parser:
                is_end_of_multiply_expression = true
                is_end_of_unary_expression    = true
                is_python_arithmetic_operator = true


            if capital_global.tremolite_parser:
                is_end_of_tremolite_range_expression = true
                is_end_of_tremolite_unary_expression = true
                is_tremolite_arithmetic_operator     = true


        initialize_action_word__Meta(
            ((
                 ((     '+',        OperatorPlusSign            )),
            )),
        )


    if capital_global.crystal_parser:
        #   {[((
        is_close_operator = { ')' : 7, ']' : 7, '}' : 7 }.get


        export(
            'is_close_operator',    is_close_operator,
        )

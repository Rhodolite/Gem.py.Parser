#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Elemental')
def module():
    def construct_action_word__line_marker_1(t, s):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert (s.count('\n') is 1) and (s[-1] == '\n')

        t.s = s


    class KeywordAnd(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'and'
        is_end_of_compare_expression           = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_keyword_and                         = true


    class KeywordAs(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = 'as'
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
        is_keyword_as                           = true


    class KeywordAssert(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'assert'


    class KeywordBreak(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'break'


    class KeywordClass(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'class'


    class KeywordContinue(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'continue'


    class KeywordDelete(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'delete'


    class KeywordElse(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'else'
        is_end_of_boolean_and_expression       = true
        is_end_of_boolean_or_expression        = true
        is_end_of_compare_expression           = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_keyword_else                        = true


    class KeywordElseColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'else:'


    class KeywordElseIf(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'else-if'


    class KeywordExcept(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'except'


    class KeywordExceptColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'except:'


    class KeywordFinally(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'finally'


    class KeywordFinallyColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'finally:'


    class KeywordFor(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'for'
        is_end_of_boolean_and_expression       = true
        is_end_of_boolean_or_expression        = true
        is_end_of_compare_expression           = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_ternary_expression_list      = true        #   Not really, but for consistency
        is_end_of_ternary_expression           = true
        is_end_of_unary_expression             = true
        is_keyword_for                         = true


    class KeywordFrom(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'from'


    class KeywordFunction(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'function'


    class KeywordIf(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'if'
        is_end_of_boolean_and_expression       = true
        is_end_of_boolean_or_expression        = true
        is_end_of_compare_expression           = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_keyword_if                          = true


    @share
    class KeywordIn(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'in'
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_keyword_in                          = true


    @share
    class KeywordIs(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'is'
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


    class KeywordNot(KeywordAndOperatorBase):
        __slots__      = (())
        display_name   = 'not'
        is_keyword_not = true


        #
        #   NOTE:
        #       The following are actually being set for the 'not in' keyword, which the 'not' keyword is a
        #       sub-part of.
        #
        #       This means than when [partially] parsing the 'not in' keyword by just parsing the first keyword,
        #       it will still be treated properly in expression parsing (which has not yet parsed the following
        #       'in' keyword).
        #
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


    class KeywordOr(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = 'or'
        is_end_of_boolean_and_expression       = true
        is_end_of_compare_expression           = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_keyword_or                          = true


    class KeywordPass(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'pass'


    class KeywordRaise(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'raise'


    class KeywordReturn(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'return'

        is_keyword_return = true


    class KeywordTry(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'try'


    class KeywordWhile(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'while'


    @share
    class KeywordWith(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'with'


    @share
    class KeywordYield(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'yield'


    class OperatorAddModify(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '+='
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
        is_modify_operator                      = true


    class OperatorAtSign(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '@'


    @share
    class OperatorCompareEqual(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '=='
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


        def display_token(t):
            if t.s == ' == ':
                return '=='

            return arrange('<%s %s>', t.display_name, portray_string(t.s))


    @share
    class OperatorCompareNotEqual(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '!='
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


    @share
    class OperatorDivide(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '/'
        is_multiply_operator       = true
        is_end_of_unary_expression = true


    class OperatorDot(KeywordAndOperatorBase):
        __slots__           = (())
        display_name        = '.'
        is_dot              = true
        is_postfix_operator = true


    class OperatorEqualSign(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '='
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
        is_equal_sign                           = true


    @share
    class OperatorGreaterThan(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '>'
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' > ':
                return '{>}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorGreaterThanOrEqual(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '>='
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' > ':
                return '{>}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorIntegerDivide(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '//'
        is_multiply_operator       = true
        is_end_of_unary_expression = true


    class OperatorLeftBrace(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '{'                                              #   }

        is_left_brace = true


        display_token = display_token__with_angle_signs
        dump_token    = dump_token__with_angle_signs


    @export
    class OperatorLeftSquareBracket(KeywordAndOperatorBase):
        __slots__                = (())
        display_name             = '['                                    #   ]
        is_left_square_bracket   = true
        is_postfix_operator      = true


    @share
    class OperatorLessThan(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '<'
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' < ':
                return '{<}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorLessThanOrEqual(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '<='
        is_compare_operator                    = true
        is_end_of_logical_and_expression       = true
        is_end_of_logical_or_expression        = true
        is_end_of_multiply_expression          = true
        is_end_of_normal_expression_list       = true
        is_end_of_normal_expression            = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true


        def __repr__(t):
            if '\n' in t.s:
                return arrange('{%s}', portray_string(t.s))

            return arrange('{%s}', t.s)


        def display_token(t):
            if t.s == ' <= ':
                return '{<=}'

            return arrange('{%s %s}', t.display_name, portray_string(t.s))


    @share
    class OperatorLogicalAndSign(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '&'
        is_end_of_multiply_expression          = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_logical_and_operator                = true


    @share
    class OperatorLogicalOrSign(KeywordAndOperatorBase):
        __slots__                              = (())
        display_name                           = '|'
        is_end_of_logical_and_expression       = true
        is_end_of_multiply_expression          = true
        is_end_of_PYTHON_arithmetic_expression = true
        is_end_of_unary_expression             = true
        is_logical_or_operator                 = true


    class OperatorLogicalOrModify(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '|='
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
        is_modify_operator                      = true


    @share
    class OperatorMinusSign(KeywordAndOperatorBase):
        __slots__                     = (())
        display_name                  = '-'
        is_end_of_multiply_expression = true
        is_end_of_unary_expression    = true
        is_minus_sign                 = true
        is_PYTHON_arithmetic_operator = true


    @share
    class OperatorPercentSign(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '%'
        is_multiply_operator       = true
        is_end_of_unary_expression = true


    @share
    class OperatorPower(KeywordAndOperatorBase):
        __slots__         = (())
        display_name      = '**'
        is_power_operator = true


    class OperatorRightBrace(KeywordAndOperatorBase):
        __slots__ = (())

        #  {
        display_name = '}'

        is_CRYSTAL_simple_atom__or__right_brace = true

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
        is__optional_comma__right_brace         = true
        is_right_brace                          = true


        display_token = display_token__with_angle_signs
        dump_token    = dump_token__with_angle_signs


    @export
    class OperatorRightSquareBracket(KeywordAndOperatorBase):
        __slots__ = (())

        #   [
        display_name = ']'

        is_CRYSTAL_simple_atom__or__right_square_bracket = true

        is_end_of_boolean_and_expression         = true
        is_end_of_boolean_or_expression          = true
        is_end_of_compare_expression             = true
        is_end_of_comprehension_expression_list  = true
        is_end_of_comprehension_expression       = true
        is_end_of_logical_and_expression         = true
        is_end_of_logical_or_expression          = true
        is_end_of_multiply_expression            = true
        is_end_of_normal_expression_list         = true
        is_end_of_normal_expression              = true
        is_end_of_PYTHON_arithmetic_expression   = true
        is_end_of_ternary_expression_list        = true
        is_end_of_ternary_expression             = true
        is_end_of_unary_expression               = true
        is__optional_comma__right_square_bracket = true
        is_right_square_bracket                  = true


    @share
    class OperatorStarSign(KeywordAndOperatorBase):
        __slots__                  = (())
        display_name               = '*'
        is_end_of_unary_expression = true
        is_multiply_operator       = true
        is_star_sign               = true


    class OperatorSubtractModify(KeywordAndOperatorBase):
        __slots__                               = (())
        display_name                            = '-='
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
        is_modify_operator                      = true


    @share
    class OperatorTildeSign(KeywordAndOperatorBase):
        __slots__     = (())
        display_name  = '~'
        is_tilde_sign = true


    initialize_action_word__Meta(
        ((
             ((     '!=',       OperatorCompareNotEqual     )),
             ((     '&',        OperatorLogicalAndSign      )),
             ((     '%',        OperatorPercentSign         )),
             ((     '*',        OperatorStarSign            )),
             ((     '**',       OperatorPower               )),
             ((     '+=',       OperatorAddModify           )),
             ((     ',',        OperatorComma               )),
             ((     '-',        OperatorMinusSign           )),
             ((     '-=',       OperatorSubtractModify      )),
             ((     '.',        OperatorDot                 )),
             ((     '/',        OperatorDivide              )),
             ((     '//',       OperatorIntegerDivide       )),
             ((     '<',        OperatorLessThan            )),
             ((     '<=',       OperatorLessThanOrEqual     )),
             ((     '=',        OperatorEqualSign           )),
             ((     '==',       OperatorCompareEqual        )),
             ((     '>',        OperatorGreaterThan         )),
             ((     '>=',       OperatorGreaterThanOrEqual  )),
             ((     'and',      KeywordAnd                  )),
             ((     'as',       KeywordAs                   )),
             ((     'else',     KeywordElse                 )),
             ((     'for',      KeywordFor                  )),
             ((     'if',       KeywordIf                   )),
             ((     'in',       KeywordIn                   )),
             ((     'is',       KeywordIs                   )),
             ((     'not',      KeywordNot                  )),
             ((     'or',       KeywordOr                   )),
             ((     '[',        OperatorLeftSquareBracket   )),
             ((     ']',        OperatorRightSquareBracket  )),
             ((     '{',        OperatorLeftBrace           )),
             ((     '|',        OperatorLogicalOrSign       )),
             ((     '|=',       OperatorLogicalOrModify     )),
             ((     '}',        OperatorRightBrace          )),
             ((     '~',        OperatorTildeSign           )),
        )),
    )


    del Shared.initialize_action_word__Meta


    conjure_at_sign          = produce_conjure_action_word__normal('at_sign',          OperatorAtSign)
    conjure_dot              = produce_conjure_action_word__normal('dot',              OperatorDot)
    conjure_equal_sign       = produce_conjure_action_word__normal('equal_sign',       OperatorEqualSign)
    conjure_keyword_as       = produce_conjure_action_word__normal('keyword_as',       KeywordAs)
    conjure_keyword_break    = produce_conjure_action_word__normal('keyword_break',    KeywordBreak)
    conjure_keyword_class    = produce_conjure_action_word__normal('keyword_class',    KeywordClass)
    conjure_keyword_continue = produce_conjure_action_word__normal('keyword_continue', KeywordContinue)
    conjure_keyword_finally  = produce_conjure_action_word__normal('keyword_finally',  KeywordFinally)
    conjure_keyword_for      = produce_conjure_action_word__normal('keyword_for',      KeywordFor)
    conjure_keyword_from     = produce_conjure_action_word__normal('keyword_from',     KeywordFrom)
    conjure_keyword_if       = produce_conjure_action_word__normal('keyword_if',       KeywordIf)
    conjure_keyword_is       = produce_conjure_action_word__normal('keyword_is',       KeywordIs)
    conjure_star_sign        = produce_conjure_action_word__normal('star_sign',        OperatorStarSign)

    [
            conjure_keyword_in, conjure_keyword_in__ends_in_newline,
    ] = produce_conjure_action_word__ends_in_newline('keyword_in', KeywordIn)

    [
            conjure_keyword_not, conjure_keyword_not__ends_in_newline,
    ] = produce_conjure_action_word__ends_in_newline('keyword_not', KeywordNot)

    [
        conjure_left_brace, conjure_left_brace__ends_in_newline,
    ] = produce_conjure_action_word__ends_in_newline('left_brace', OperatorLeftBrace)

    [
        conjure_left_square_bracket, conjure_left_square_bracket__ends_in_newline,
    ] = produce_conjure_action_word__ends_in_newline('left_square_bracket', OperatorLeftSquareBracket)

    [
        conjure_right_brace, conjure_right_brace__ends_in_newline,
    ] = produce_conjure_action_word__ends_in_newline('right_brace', OperatorRightBrace)

    [
        conjure_right_square_bracket, conjure_right_square_bracket__ends_in_newline,
    ] = produce_conjure_action_word__ends_in_newline('right_square_bracket', OperatorRightSquareBracket)


    #
    #   Fix these to have 'WithPythonNewline' version
    #
    conjure_else_colon       = produce_conjure_action_word__normal('keyword-else-colon',    KeywordElseColon)
    conjure_except_colon     = produce_conjure_action_word__normal('keyword-except-colon',  KeywordExceptColon)
    conjure_finally_colon    = produce_conjure_action_word__normal('keyword-finally-colon', KeywordFinallyColon)
    conjure_keyword_assert   = produce_conjure_action_word__normal('keyword-assert',        KeywordAssert)
    conjure_keyword_delete   = produce_conjure_action_word__normal('keyword-delete',        KeywordDelete)
    conjure_keyword_else     = produce_conjure_action_word__normal('keyword-else',          KeywordElse)
    conjure_keyword_else_if  = produce_conjure_action_word__normal('keyword-else-if',       KeywordElseIf)
    conjure_keyword_except   = produce_conjure_action_word__normal('keyword-except',        KeywordExcept)
    conjure_keyword_function = produce_conjure_action_word__normal('keyword-function',      KeywordFunction)
    conjure_keyword_pass     = produce_conjure_action_word__normal('keyword-pass',          KeywordPass)
    conjure_keyword_raise    = produce_conjure_action_word__normal('keyword-raise',         KeywordRaise)
    conjure_keyword_return   = produce_conjure_action_word__normal('keyword-return',        KeywordReturn)
    conjure_keyword_try      = produce_conjure_action_word__normal('keyword-try',           KeywordTry)
    conjure_keyword_while    = produce_conjure_action_word__normal('keyword-while',         KeywordWhile)
    conjure_keyword_with     = produce_conjure_action_word__normal('keyword-with',          KeywordWith)
    conjure_keyword_yield    = produce_conjure_action_word__normal('keyword-yield',         KeywordYield)


    ASSERT__W                   = conjure_keyword_assert      ('assert ')
    AT_SIGN                     = conjure_at_sign             ('@')
    BREAK                       = conjure_keyword_break       ('break')
    CLASS__W                    = conjure_keyword_class       ('class ')
    COMMA                       = conjure_CRYSTAL_comma       (',')
    CONTINUE                    = conjure_keyword_continue    ('continue')
    DELETE__W                   = conjure_keyword_delete      ('del ')
    DOT                         = conjure_dot                 ('.')
    ELSE                        = conjure_keyword_else        ('else')
    ELSE_IF__W                  = conjure_keyword_else_if     ('elif ')
    EXCEPT                      = conjure_keyword_except      ('except')
    EXCEPT__W                   = conjure_keyword_except      ('except ')
    FINALLY                     = conjure_keyword_finally     ('finally')
    FOR__W                      = conjure_keyword_for         ('for ')
    FROM__W                     = conjure_keyword_from        ('from ')
    FUNCTION__W                 = conjure_keyword_function    ('def ')
    IF__W                       = conjure_keyword_if          ('if ')
    IMPORT__W                   = conjure_keyword_import      ('import ')
    IN__W                       = conjure_keyword_in          ('in ')
    LEFT_BRACE                  = conjure_left_brace          ('{')
    LSB                         = conjure_left_square_bracket ('[')
    MINUS_SIGN                  = conjure_action_word         ('-', '-')
    NOT__W                      = conjure_keyword_not         ('not ')
    PASS                        = conjure_keyword_pass        ('pass')
    PLUS_SIGN                   = conjure_action_word         ('+', '+')
    RAISE                       = conjure_keyword_raise       ('raise')
    RAISE__W                    = conjure_keyword_raise       ('raise ')
    RETURN                      = conjure_keyword_return      ('return')
    RETURN__W                   = conjure_keyword_return      ('return ')
    RIGHT_BRACE                 = conjure_right_brace         ('}')
    RSB                         = conjure_right_square_bracket(']')
    STAR_SIGN                   = conjure_star_sign           ('*')
    TILDE_SIGN                  = conjure_action_word         ('~', '~')
    TRY                         = conjure_keyword_try         ('try')
    W__ADD_MODIFY__W            = conjure_action_word         ('+=', ' += ')
    W__AND_SIGN__W              = conjure_action_word         ('&', ' & ')
    W__AND__W                   = conjure_action_word         ('and', ' and ')
    W__ASSIGN__W                = conjure_equal_sign          (' = ')
    W__AS__W                    = conjure_keyword_as          (' as ')
    W__COLON__W                 = conjure_colon               (' : ')
    W__COMPARE_EQUAL__W         = conjure_action_word         ('==', ' == ')
    W__COMPARE_NOT_EQUAL__W     = conjure_action_word         ('!=', ' != ')
    W__DIVIDE__W                = conjure_action_word         ('/', ' / ')
    W__ELSE__W                  = conjure_keyword_else        (' else ')
    W__FOR__W                   = conjure_keyword_for         (' for ')
    W__GREATER_THAN_OR_EQUAL__W = conjure_action_word         ('>=',  ' >= ')
    W__GREATER_THAN__W          = conjure_action_word         ('>',  ' > ')
    WHILE__W                    = conjure_keyword_while       ('while ')
    W__IF__W                    = conjure_keyword_if          (' if ')
    W__IMPORT__W                = conjure_keyword_import      (' import ')
    W__INTEGER_DIVIDE__W        = conjure_action_word         ('//', ' // ')
    W__IN__W                    = conjure_keyword_in          (' in ')
    W__IS__W                    = conjure_keyword_is          (' is ')
    WITH__W                     = conjure_keyword_with        ('with ')
    W__LESS_THAN_OR_EQUAL__W    = conjure_action_word         ('<=', ' <= ')
    W__LESS_THAN__W             = conjure_action_word         ('<',  ' < ')
    W__NOT__W                   = conjure_keyword_not         (' not ')
    W__OR_MODIFY__W             = conjure_action_word         ('|=', ' |= ')
    W__OR_SIGN__W               = conjure_action_word         ('|', ' | ')
    W__OR__W                    = conjure_action_word         ('or', ' or ')
    W__PERCENT_SIGN__W          = conjure_action_word         ('%', ' % ')
    W__POWER__W                 = conjure_action_word         ('**', ' ** ')
    W__STAR_SIGN__W             = conjure_star_sign           (' * ')
    W__SUBTRACT_MODIFY__W       = conjure_action_word         ('-=', ' -= ')
    YIELD                       = conjure_keyword_yield       ('yield')
    YIELD__W                    = conjure_keyword_yield       ('yield ')


    #
    #   NOTE:
    #       .mutate functions when called are generally called on expressions, thus the result
    #       (when removing comments) needs to have leading space.
    #
    #       .transform functions when called are generally called on statement, thus the result
    #       (when removing comments) needs to NOT have leading space.
    #
    #       Example:
    #           KeywordIf.mutate:       Returns ' if ' (with    a leading space, when removing comments)
    #           KeywordIf.transform:    Returns 'if '  (without a leading space, when removing comments)
    #
    #       Thus given the following input:
    #
    #           if  ((a)if  b else c):
    #
    #       The first 'if  ' is transformed to 'if ', while the second 'if  ' is mutated to ' if '.
    #
    #   NOTE:
    #       For KeywordNot, the .mutate is called for a unary not-expressio; hence the result is ' not '.
    #
    #       When used in an expression like '1 is not 2' then the Is_Not handles this & internally
    #       converts this to ' in ' & 'not ' (i.e.: no leading space on the 'not ').
    #
    #       Hence KeywordNot.mutate always returns 'not ' since it is only called in the context
    #       of a unary-expression.
    #
    KeywordElse  .mutate = produce_mutate__uncommented('keyword_else',   W__ELSE__W)
    KeywordFor   .mutate = produce_mutate__uncommented('keyword_for',    W__FOR__W)
    KeywordIf    .mutate = produce_mutate__uncommented('keyword_if',     W__IF__W)
    KeywordIn    .mutate = produce_mutate__uncommented('keyword_in',     W__IN__W)
    KeywordImport.mutate = produce_mutate__uncommented('keyword_import', W__IMPORT__W)
    KeywordNot   .mutate = produce_mutate__uncommented('keyword_not',    NOT__W)
    OperatorColon.mutate = produce_mutate__uncommented('operator_colon', W__COLON__W)
#   OperatorLeftParenthesis.mutate = produce_mutate__uncommented('left_parenthesis', LEFT_PARENTHESIS)


    #
    #   NOTE:
    #       See note in KeywordFor   .mutate on the difference from KeywordFor   .transform
    #       See note in KeywordImport.mutate on the difference from KeywordImport.transform
    #
    KeywordAnd             .transform = produce_transform__uncommented('keyword_and',         W__AND__W)
    KeywordAs              .transform = produce_transform__uncommented('keyword_as',          W__AS__W)
    KeywordAssert          .transform = produce_transform__uncommented('keyword_assert',      ASSERT__W)
    KeywordClass           .transform = produce_transform__uncommented('keyword_class',       CLASS__W)
    KeywordDelete          .transform = produce_transform__uncommented('keyword_delete',      DELETE__W)
    KeywordElseIf          .transform = produce_transform__uncommented('keyword_else_if',     ELSE_IF__W)
    KeywordExcept          .transform = produce_transform__uncommented('keyword_except',      EXCEPT__W)
    KeywordFor             .transform = produce_transform__uncommented('keyword_for',         FOR__W)
    KeywordFrom            .transform = produce_transform__uncommented('keyword_from',        FROM__W)
    KeywordFunction        .transform = produce_transform__uncommented('keyword_function',    FUNCTION__W)
    KeywordIf              .transform = produce_transform__uncommented('keyword_if',          IF__W)
    KeywordIn              .transform = produce_transform__uncommented('keyword_in',          W__IN__W)
    KeywordIs              .transform = produce_transform__uncommented('keyword_is',          W__IS__W)
    KeywordImport          .transform = produce_transform__uncommented('keyword_import',      IMPORT__W)
    KeywordOr              .transform = produce_transform__uncommented('keyword_or',          W__OR__W)
    KeywordRaise           .transform = produce_transform__uncommented('keyword_raise',       RAISE__W)
    KeywordReturn          .transform = produce_transform__uncommented('keyword_return',      RETURN__W)
    KeywordWhile           .transform = produce_transform__uncommented('keyword_while',       WHILE__W)
    KeywordWith            .transform = produce_transform__uncommented('keyword_with',        WITH__W)
    KeywordYield           .transform = produce_transform__uncommented('keyword_yield',       YIELD__W)
    OperatorAddModify      .transform = produce_transform__uncommented('operator_add_modify', W__ADD_MODIFY__W)
    OperatorAtSign         .transform = produce_transform__uncommented('at_sign',             AT_SIGN)
    OperatorColon          .transform = produce_transform__uncommented('colon',               COLON)
    OperatorComma          .transform = produce_transform__uncommented('comma',               COMMA__W)
    OperatorCompareEqual   .transform = produce_transform__uncommented('compare_equal',       W__COMPARE_EQUAL__W)
    OperatorCompareNotEqual.transform = produce_transform__uncommented('compare_not_equal',   W__COMPARE_NOT_EQUAL__W)
    OperatorDot            .transform = produce_transform__uncommented('operator_dot',        DOT)
    OperatorDivide         .transform = produce_transform__uncommented('operator_divide',     W__DIVIDE__W)
    OperatorEqualSign      .transform = produce_transform__uncommented('equal_sign',          W__ASSIGN__W)

    OperatorIntegerDivide.transform = produce_transform__uncommented(
                                          'operator_integer_divide',
                                          W__INTEGER_DIVIDE__W,
                                      )

    OperatorGreaterThan.transform = produce_transform__uncommented('greater_than', W__GREATER_THAN__W)

    OperatorGreaterThanOrEqual.transform = produce_transform__uncommented(
                                               'greater_than_or_equal',
                                               W__GREATER_THAN_OR_EQUAL__W,
                                           )

    OperatorLeftBrace        .transform = produce_transform__uncommented('left_brace',          LEFT_BRACE)
    OperatorLeftParenthesis  .transform = produce_transform__uncommented('left_parenthesis',    LEFT_PARENTHESIS)
    OperatorLeftSquareBracket.transform = produce_transform__uncommented('left_square_bracket', LSB)
    OperatorLessThan         .transform = produce_transform__uncommented('less_than',           W__LESS_THAN__W)

    OperatorLessThanOrEqual.transform = produce_transform__uncommented('less_than_or_equal', W__LESS_THAN_OR_EQUAL__W)

    OperatorLogicalAndSign    .transform = produce_transform__uncommented('logical_and_sign',      W__AND_SIGN__W)
    OperatorLogicalOrSign     .transform = produce_transform__uncommented('logical_or_sign',       W__OR_SIGN__W)
    OperatorLogicalOrModify   .transform = produce_transform__uncommented('logical_or_modify',     W__OR_MODIFY__W)
    OperatorMinusSign         .transform = produce_transform__uncommented('operator_minus_sign',   MINUS_SIGN)
    OperatorPercentSign       .transform = produce_transform__uncommented('operator_percent_sign', W__PERCENT_SIGN__W)
    OperatorPlusSign          .transform = produce_transform__uncommented('operator_plus_sign',    PLUS_SIGN)
    OperatorPower             .transform = produce_transform__uncommented('operator_power',        W__POWER__W)
    OperatorRightBrace        .transform = produce_transform__uncommented('right_brace',           RIGHT_BRACE)
    OperatorRightParenthesis  .transform = produce_transform__uncommented('right_parenthesis',     RIGHT_PARENTHESIS)
    OperatorRightSquareBracket.transform = produce_transform__uncommented('right_square_bracket',  RSB)
    OperatorStarSign          .transform = produce_transform__uncommented('operator_star_sign',    STAR_SIGN)

    OperatorSubtractModify.transform = produce_transform__uncommented(
                                           'operator_subtract_modify',
                                           W__SUBTRACT_MODIFY__W,
                                       )

    OperatorTildeSign.transform = produce_transform__uncommented('operator_tilde_sign', TILDE_SIGN)


    find_PYTHON_atom_type = {
            '"' : conjure_double_quote,
            "'" : conjure_single_quote,

            #   (
            ')' : conjure_right_parenthesis,
            '.' : conjure_token_number,

            '0' : conjure_token_number, '1' : conjure_token_number, '2' : conjure_token_number,
            '3' : conjure_token_number, '4' : conjure_token_number, '5' : conjure_token_number,
            '6' : conjure_token_number, '7' : conjure_token_number, '8' : conjure_token_number,
            '9' : conjure_token_number,

            'A' : conjure_name, 'B' : conjure_name, 'C' : conjure_name, 'D' : conjure_name, 'E' : conjure_name,
            'F' : conjure_name, 'G' : conjure_name, 'H' : conjure_name, 'I' : conjure_name, 'J' : conjure_name,
            'K' : conjure_name, 'L' : conjure_name, 'M' : conjure_name, 'N' : conjure_name, 'O' : conjure_name,
            'P' : conjure_name, 'Q' : conjure_name, 'R' : conjure_name, 'S' : conjure_name, 'T' : conjure_name,
            'U' : conjure_name, 'V' : conjure_name, 'W' : conjure_name, 'X' : conjure_name, 'Y' : conjure_name,
            'Z' : conjure_name, '_' : conjure_name,

            #  [
            ']' : conjure_right_square_bracket,

            'a' : conjure_name, 'b' : conjure_name, 'c' : conjure_name, 'd' : conjure_name, 'e' : conjure_name,
            'f' : conjure_name, 'g' : conjure_name, 'h' : conjure_name, 'i' : conjure_name, 'j' : conjure_name,
            'k' : conjure_name, 'l' : conjure_name, 'm' : conjure_name, 'n' : conjure_name, 'o' : conjure_name,
            'p' : conjure_name, 'q' : conjure_name, 'r' : conjure_name, 's' : conjure_name, 't' : conjure_name,
            'u' : conjure_name, 'v' : conjure_name, 'w' : conjure_name, 'x' : conjure_name, 'y' : conjure_name,
            'z' : conjure_name,
        }.__getitem__


    lookup_PYTHON_keyword_conjure_function = {
            'not'    : conjure_keyword_not,
            'return' : conjure_keyword_return,
        }.get


    share(
        'conjure_at_sign',                                  conjure_at_sign,
        'conjure_colon',                                    conjure_colon,
        'conjure_colon__ends_in_newline',                   conjure_colon__ends_in_newline,
        'conjure_dot',                                      conjure_dot,
        'conjure_else_colon',                               conjure_else_colon,
        'conjure_equal_sign',                               conjure_equal_sign,
        'conjure_except_colon',                             conjure_except_colon,
        'conjure_finally_colon',                            conjure_finally_colon,
        'conjure_keyword_as',                               conjure_keyword_as,
        'conjure_keyword_assert',                           conjure_keyword_assert,
        'conjure_keyword_break',                            conjure_keyword_break,
        'conjure_keyword_class',                            conjure_keyword_class,
        'conjure_keyword_continue',                         conjure_keyword_continue,
        'conjure_keyword_delete',                           conjure_keyword_delete,
        'conjure_keyword_else',                             conjure_keyword_else,
        'conjure_keyword_else_if',                          conjure_keyword_else_if,
        'conjure_keyword_except',                           conjure_keyword_except,
        'conjure_keyword_finally',                          conjure_keyword_finally,
        'conjure_keyword_for',                              conjure_keyword_for,
        'conjure_keyword_from',                             conjure_keyword_from,
        'conjure_keyword_function',                         conjure_keyword_function,
        'conjure_keyword_if',                               conjure_keyword_if,
        'conjure_keyword_in',                               conjure_keyword_in,
        'conjure_keyword_in__ends_in_newline',              conjure_keyword_in__ends_in_newline,
        'conjure_keyword_is',                               conjure_keyword_is,
        'conjure_keyword_not',                              conjure_keyword_not,
        'conjure_keyword_not__ends_in_newline',             conjure_keyword_not__ends_in_newline,
        'conjure_keyword_pass',                             conjure_keyword_pass,
        'conjure_keyword_raise',                            conjure_keyword_raise,
        'conjure_keyword_return',                           conjure_keyword_return,
        'conjure_keyword_try',                              conjure_keyword_try,
        'conjure_keyword_while',                            conjure_keyword_while,
        'conjure_keyword_with',                             conjure_keyword_with,
        'conjure_keyword_yield',                            conjure_keyword_yield,
        'conjure_left_brace',                               conjure_left_brace,
        'conjure_left_brace__ends_in_newline',              conjure_left_brace__ends_in_newline,
        'conjure_left_square_bracket',                      conjure_left_square_bracket,
        'conjure_left_square_bracket__ends_in_newline',     conjure_left_square_bracket__ends_in_newline,
        'conjure_right_brace',                              conjure_right_brace,
        'conjure_right_brace__ends_in_newline',             conjure_right_brace__ends_in_newline,
        'conjure_right_parenthesis',                        conjure_right_parenthesis,
        'conjure_right_parenthesis__ends_in_newline',       conjure_right_parenthesis__ends_in_newline,
        'conjure_right_square_bracket',                     conjure_right_square_bracket,
        'conjure_right_square_bracket__ends_in_newline',    conjure_right_square_bracket__ends_in_newline,
        'conjure_star_sign',                                conjure_star_sign,
        'find_PYTHON_atom_type',                            find_PYTHON_atom_type,
        'AT_SIGN',                                          AT_SIGN,
        'BREAK',                                            BREAK,
        'CONTINUE',                                         CONTINUE,
        'COLON',                                            COLON,
        'COMMA',                                            COMMA,
        'COMMA__W',                                         COMMA__W,
        'ELSE',                                             ELSE,
        'EXCEPT',                                           EXCEPT,
        'FINALLY',                                          FINALLY,
        'FOR__W',                                           FOR__W,
        'FUNCTION__W',                                      FUNCTION__W,
        'IF__W',                                            IF__W,
        'IN__W',                                            IN__W,
        'LEFT_BRACE',                                       LEFT_BRACE,
        'lookup_PYTHON_keyword_conjure_function',           lookup_PYTHON_keyword_conjure_function,
        'LSB',                                              LSB,
        'NOT__W',                                           NOT__W,
        'PASS',                                             PASS,
        'RAISE',                                            RAISE,
        'RAISE__W',                                         RAISE__W,
        'RETURN',                                           RETURN,
        'RETURN__W',                                        RETURN__W,
        'RIGHT_BRACE',                                      RIGHT_BRACE,
        'RSB',                                              RSB,
        'TRY',                                              TRY,
        'W__ASSIGN__W',                                     W__ASSIGN__W,
        'W__AS__W',                                         W__AS__W,
        'W__COLON__W',                                      W__COLON__W,
        'W__ELSE__W',                                       W__ELSE__W,
        'W__FOR__W',                                        W__FOR__W,
        'WHILE__W',                                         WHILE__W,
        'W__IF__W',                                         W__IF__W,
        'W__IN__W',                                         W__IN__W,
        'W__IS__W',                                         W__IS__W,
        'WITH__W',                                          WITH__W,
        'W__NOT__W',                                        W__NOT__W,
        'W__PERCENT_SIGN__W',                               W__PERCENT_SIGN__W,
        'W__STAR_SIGN__W',                                  W__STAR_SIGN__W,
        'YIELD',                                            YIELD,
        'YIELD__W',                                         YIELD__W,
    )

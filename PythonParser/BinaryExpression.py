#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BinaryExpression')
def module():
    require_module('PythonParser.DualToken')
    require_module('PythonParser.Elemental')
    require_module('PythonParser.Priority')


    class AndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'and-1'
        frill        = conjure_action_word('and', ' and ')


    class AsFragment(BinaryExpression):
        __slots__    = (())
        display_name = 'as-fragment'
        frill        = conjure_action_word('as', ' as ')


        def scout_variables(t, art):
            raise_runtime_error('AsFragment.scout_variables: programming error')


        def write_variables(t, art):
            #
            #   t.a: not relevant yet, relevant in future when tracking what is in each module
            #
            t.b.write_variables(art)


    class CommaExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = ','
        frill        = COMMA__W


        write_variables = write_variables__ab


    class ComprehensionIfExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'comprehension-if'
        frill        = conjure_keyword_if(' if ')


    class CompareContainsExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'in'
        frill        = conjure_keyword_in(' in ')


    class CompareEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '=='
        frill        = conjure_action_word('==', ' == ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareDifferentExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is-not'
        frill        = conjure_is_not(W__IS__W, NOT__W)


    del Shared.conjure_is_not


    class CompareExcludeExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'not-in'
        frill        = conjure_not_in(W__NOT__W, conjure_keyword_in('in '))


    del Shared.conjure_not_in


    class CompareGreaterThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>'
        frill        = conjure_action_word('>', ' > ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareGreaterThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '>='
        frill        = conjure_action_word('>=', ' >= ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareIdentityExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'is'
        frill        = conjure_keyword_is(' is ')


    class CompareLessThanExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<'
        frill        = conjure_action_word('<', ' < ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareLessThanOrEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '<='
        frill        = conjure_action_word('<=', ' <= ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class CompareNotEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '!='
        frill        = conjure_action_word('!=', ' != ')

        __repr__      = portray_with_braces
        display_token = display_token__with_braces


    class DivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '/'
        frill        = conjure_action_word('/', ' / ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class IntegerDivideExpression(BinaryExpression):
        __slots__    = (())
        display_name = '//'
        frill        = conjure_action_word('//', ' // ')

        __repr__ = portray_with_braces

        display_token = display_token__with_braces


    class KeywordArgument(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-argument'
        frill        = W__ASSIGN__W


        def scout_variables(t, art):
            #
            #   t.a: nothing to do yet -- later when matching function keyword parameters have something to do
            #
            t.b.scout_variables(art)


    class KeywordParameter(BinaryExpression):
        __slots__    = (())
        display_name = 'keyword-parameter'
        frill        = W__ASSIGN__W


        add_parameters = add_parameters__a


        def scout_default_values(t, art):
            t.b.scout_variables(art)


        def scout_variables(t, art):
            assert 0, 'incomplete'


    class LogicalAndExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '&'
        frill        = conjure_action_word('&', ' & ')


    class LogicalOrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '|'
        frill        = conjure_action_word('|', ' | ')


    class MapElement(BinaryExpression):
        __slots__    = (())
        display_name = ':'
        frill        = W__COLON__W


    class ModulusExpression(BinaryExpression):
        __slots__    = (())
        display_name = '%'
        frill        = W__PERCENT_SIGN__W


    class MultiplyExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = '*'
        frill        = W__STAR_SIGN__W


    class OrExpression_1(BinaryExpression):
        __slots__    = (())
        display_name = 'or'
        frill        = conjure_action_word('or', ' or ')


    class PowerExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'power'
        frill        = conjure_action_word('**', ' ** ')


    class SubtractExpression(BinaryExpression):
        __slots__    = (())
        display_name = '-'
        frill        = conjure_action_word('-', ' - ')


    conjure_and_expression_1   = produce_conjure_binary_expression('and-1',             AndExpression_1)
    conjure_as_fragment        = produce_conjure_binary_expression('as-fragment',       AsFragment)
    conjure_comma_expression_1 = produce_conjure_binary_expression('comma-1',           CommaExpression_1)
    conjure_compare_contains   = produce_conjure_binary_expression('compare-contains',  CompareContainsExpression)
    conjure_compare_different  = produce_conjure_binary_expression('compare-different', CompareDifferentExpression)
    conjure_compare_equal      = produce_conjure_binary_expression('compare-equal',     CompareEqualExpression)
    conjure_compare_exclude    = produce_conjure_binary_expression('compare-exclude',   CompareExcludeExpression)

    conjure_compare_greater_than_or_equal = produce_conjure_binary_expression(
            'compare-greater-than-or-equal',
            CompareGreaterThanOrEqualExpression,
        )

    conjure_compare_greater_than = produce_conjure_binary_expression(
            'compare-greater-than',
            CompareGreaterThanExpression,
        )

    conjure_compare_identity = produce_conjure_binary_expression('compare-identity', CompareIdentityExpression)

    conjure_compare_less_than_or_equal = produce_conjure_binary_expression(
            'compare-less-than-or-equal',
            CompareLessThanOrEqualExpression,
        )

    conjure_compare_less_than = produce_conjure_binary_expression('compare-less-than', CompareLessThanExpression)
    conjure_compare_not_equal = produce_conjure_binary_expression('compare-not-equal', CompareNotEqualExpression)
    conjure_comprehension_if  = produce_conjure_binary_expression('comprehension-if',  ComprehensionIfExpression)
    conjure_divide_expression = produce_conjure_binary_expression('divide',            DivideExpression)

    conjure_integer_divide_expression = produce_conjure_binary_expression('integer-divide',    IntegerDivideExpression)
    conjure_keyword_argument          = produce_conjure_binary_expression('keyword-argument',  KeywordArgument)
    conjure_keyword_parameter         = produce_conjure_binary_expression('keyword-parameter', KeywordParameter)
    conjure_logical_and_expression    = produce_conjure_binary_expression('logical-and-1',     LogicalAndExpression_1)
    conjure_logical_or_expression     = produce_conjure_binary_expression('logical-or-1',      LogicalOrExpression_1)
    conjure_map_element               = produce_conjure_binary_expression('map-element',       MapElement)
    conjure_modulus_expression        = produce_conjure_binary_expression('modulus',           ModulusExpression)
    conjure_multiple_expression_1     = produce_conjure_binary_expression('multiply-1',        MultiplyExpression_1)
    conjure_or_expression_1           = produce_conjure_binary_expression('or-1',              OrExpression_1)
    conjure_power_expression          = produce_conjure_binary_expression('power',             PowerExpression)
    conjure_subtract_expression       = produce_conjure_binary_expression('subtract',          SubtractExpression)


    #
    #   .mutate
    #
    AddExpression.mutate = produce_mutate__binary_expression(
                               'add-expression',
                               PRIORITY_ARITHMETIC,
                               PRIORITY_MULTIPLY,
                               conjure_add_expression,
                           )

    AndExpression_1.mutate = produce_mutate__binary_expression(
                                 'and-expression-1',
                                 PRIORITY_BOOLEAN_AND,
                                 PRIORITY_NOT,
                                 conjure_and_expression_1,
                             )

    AsFragment.mutate = produce_mutate__binary_expression(
                            'as_fragment',
                            PRIORITY_TERNARY,
                            PRIORITY_NORMAL,
                            conjure_as_fragment,
                        )


    CommaExpression_1.mutate = produce_mutate__binary_expression(
                                   'comma_expression_1',
                                   PRIORITY_TERNARY,
                                   PRIORITY_TERNARY,
                                   conjure_comma_expression_1,
                               )

    CompareContainsExpression.mutate = produce_mutate__binary_expression(
                                           'compare_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_contains,
                                       )

    CompareEqualExpression.mutate = produce_mutate__binary_expression(
                                        'compare_equal_expression',
                                        PRIORITY_COMPARE,
                                        PRIORITY_NORMAL,
                                        conjure_compare_equal,
                                    )

    CompareDifferentExpression.mutate = produce_mutate__binary_expression(
                                            'compare_different_expression',
                                            PRIORITY_COMPARE,
                                            PRIORITY_NORMAL,
                                            conjure_compare_different,
                                        )

    CompareExcludeExpression.mutate = produce_mutate__binary_expression(
                                          'compare_exclude_expression',
                                          PRIORITY_COMPARE,
                                          PRIORITY_NORMAL,
                                          conjure_compare_exclude,
                                      )

    CompareGreaterThanExpression.mutate = produce_mutate__binary_expression(
                                              'compare_greater_than_expression',
                                              PRIORITY_COMPARE,
                                              PRIORITY_NORMAL,
                                              conjure_compare_greater_than,
                                          )

    CompareGreaterThanOrEqualExpression.mutate = produce_mutate__binary_expression(
                                                     'compare_greater_than_or_equal_expression',
                                                     PRIORITY_COMPARE,
                                                     PRIORITY_NORMAL,
                                                     conjure_compare_greater_than_or_equal,
                                                 )

    CompareIdentityExpression.mutate = produce_mutate__binary_expression(
                                           'compare_identity_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_identity,
                                       )

    CompareLessThanExpression.mutate = produce_mutate__binary_expression(
                                           'compare_less_than_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_less_than,
                                       )

    CompareLessThanOrEqualExpression.mutate = produce_mutate__binary_expression(
                                                  'compare_less_than_or_equal_expression',
                                                  PRIORITY_COMPARE,
                                                  PRIORITY_NORMAL,
                                                  conjure_compare_less_than_or_equal,
                                              )

    CompareNotEqualExpression.mutate = produce_mutate__binary_expression(
                                           'compare_not_equal_expression',
                                           PRIORITY_COMPARE,
                                           PRIORITY_NORMAL,
                                           conjure_compare_not_equal,
                                       )

    ComprehensionIfExpression.mutate = produce_mutate__binary_expression(
                                           'comprehension_if_expression',
                                           PRIORITY_TERNARY,
                                           PRIORITY_LAMBDA,
                                           conjure_comprehension_if,
                                       )

    DivideExpression.mutate = produce_mutate__binary_expression(
                              'divide_expression',
                                  PRIORITY_MULTIPLY,
                                  PRIORITY_UNARY,
                                  conjure_divide_expression,
                              )

    IntegerDivideExpression.mutate = produce_mutate__binary_expression(
                                         'integer_divide_expression',
                                         PRIORITY_MULTIPLY,
                                         PRIORITY_UNARY,
                                         conjure_integer_divide_expression,
                                     )


    KeywordArgument.mutate = produce_mutate__binary_expression(
                                 'keyword-argument',
                                 PRIORITY_POSTFIX,
                                 PRIORITY_TERNARY,
                                 conjure_keyword_argument,
                             )

    LogicalAndExpression_1.mutate = produce_mutate__binary_expression(
                                        'logical_and_expression_1',
                                        PRIORITY_LOGICAL_AND,
                                        PRIORITY_SHIFT,
                                        conjure_logical_and_expression,
                                    )

    LogicalOrExpression_1.mutate = produce_mutate__binary_expression(
                                       'logical_or_expression_1',
                                       PRIORITY_NORMAL,
                                       PRIORITY_LOGICAL_EXCLUSIVE_OR,
                                       conjure_logical_or_expression,
                                   )

    MapElement.mutate = produce_mutate__map_element(
                            'map_element',
                            PRIORITY_MAP_ELEMENT,
                            PRIORITY_TERNARY,
                            PRIORITY_TERNARY,
                            conjure_map_element,
                        )

    ModulusExpression.mutate = produce_mutate__binary_expression(
                                        'modulus_expression',
                                        PRIORITY_MULTIPLY,
                                        PRIORITY_UNARY,
                                        conjure_modulus_expression,
                                    )

    MultiplyExpression_1.mutate = produce_mutate__binary_expression(
                                      'multiply_expression_1',
                                      PRIORITY_MULTIPLY,
                                      PRIORITY_UNARY,
                                      conjure_multiple_expression_1,
                                  )

    OrExpression_1.mutate = produce_mutate__binary_expression(
                                'or_expression_1',
                                PRIORITY_BOOLEAN_OR,
                                PRIORITY_BOOLEAN_AND,
                                conjure_or_expression_1,
                            )

    PowerExpression.mutate = produce_mutate__binary_expression(
                                 'power_expression',
                                 PRIORITY_POWER,
                                 PRIORITY_UNARY,                        #   SIC: Unary on purpose
                                 conjure_power_expression,
                             )

    SubtractExpression.mutate = produce_mutate__binary_expression(
                                    'subtract_expression',
                                    PRIORITY_ARITHMETIC,
                                    PRIORITY_MULTIPLY,
                                    conjure_subtract_expression,
                                )

    #
    #   .transform
    #
    KeywordParameter.transform = produce_transform__binary_expression(
                                     'keyword_parameter',
                                     PRIORITY_ATOM,
                                     PRIORITY_TERNARY,
                                     conjure_keyword_parameter,
                                 )


    #
    #   .expression_meta
    #
    Is_Not                    .expression_meta = static_method(conjure_compare_different)
    KeywordIn                 .expression_meta = static_method(conjure_compare_contains)
    KeywordIs                 .expression_meta = static_method(conjure_compare_identity)
    Not_In                    .expression_meta = static_method(conjure_compare_exclude)
    OperatorCompareEqual      .expression_meta = static_method(conjure_compare_equal)
    OperatorCompareNotEqual   .expression_meta = static_method(conjure_compare_not_equal)
    OperatorDivide            .expression_meta = static_method(conjure_divide_expression)
    OperatorGreaterThan       .expression_meta = static_method(conjure_compare_greater_than)
    OperatorGreaterThanOrEqual.expression_meta = static_method(conjure_compare_greater_than_or_equal)
    OperatorIntegerDivide     .expression_meta = static_method(conjure_integer_divide_expression)
    OperatorLessThan          .expression_meta = static_method(conjure_compare_less_than)
    OperatorLessThanOrEqual   .expression_meta = static_method(conjure_compare_less_than_or_equal)
    OperatorMinusSign         .expression_meta = static_method(conjure_subtract_expression)
    OperatorPercentSign       .expression_meta = static_method(conjure_modulus_expression)
    OperatorStarSign          .expression_meta = static_method(conjure_multiple_expression_1)


    share(
        'conjure_and_expression_1',         conjure_and_expression_1,
        'conjure_comma_expression_1',       conjure_comma_expression_1,
        'conjure_comprehension_if',         conjure_comprehension_if,
        'conjure_keyword_argument',         conjure_keyword_argument,
        'conjure_keyword_parameter',        conjure_keyword_parameter,
        'conjure_logical_and_expression',   conjure_logical_and_expression,
        'conjure_logical_or_expression',    conjure_logical_or_expression,
        'conjure_map_element',              conjure_map_element,
        'conjure_as_fragment',              conjure_as_fragment,
        'conjure_modulus_expression',       conjure_modulus_expression,
        'conjure_or_expression_1',          conjure_or_expression_1,
        'conjure_power_expression',         conjure_power_expression,
    )

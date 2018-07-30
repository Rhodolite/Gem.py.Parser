#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ManyExpression')
def module():
    class AndExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'and-*'

        scout_variables = scout_variables__many


    class CommaExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = ',-*'

        scout_variables = scout_variables__many
        write_variables = write_variables__many


    class CompareExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'compare-*'

        scout_variables = scout_variables__many


    class LogicalOrExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = '|-*'

        order           = order__frill_many
        scout_variables = scout_variables__many


    class MultiplyExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'multiply-*'

        scout_variables = scout_variables__many


    class OrExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'or-*'

        scout_variables = scout_variables__many


    [
        conjure_and_expression_many, conjure_and_expression_many__with_frill,
    ] = produce_conjure_many_expression('and-*', AndExpression_Many)

    [
        conjure_comma_expression_many, conjure_comma_expression_many__with_frill,
    ] = produce_conjure_many_expression('comma-*', CommaExpression_Many) 

    [
        conjure_compare_expression_many, conjure_compare_expression_many__with_frill,
    ] = produce_conjure_many_expression('compare-*', CompareExpression_Many) 

    [
        conjure_logical_or_expression_many, conjure_logical_or_expression_many__with_frill,
    ] = produce_conjure_many_expression('logical-or-*', LogicalOrExpression_Many)

    [
        conjure_multiply_expression_many, conjure_multiply_expression_many__with_frill,
    ] = produce_conjure_many_expression('multiply-*', MultiplyExpression_Many)

    [
        conjure_or_expression_many, conjure_or_expression_many__with_frill,
    ] = produce_conjure_many_expression('or-*', OrExpression_Many)


    #
    #   .mutate
    #
    AndExpression_Many.mutate = produce_mutate__frill__many(
            'and_expression_many',
            PRIORITY_BOOLEAN_AND,
            PRIORITY_NOT,
            PRIORITY_NOT,
            conjure_and_expression_many__with_frill,
        )

    ArithmeticExpression_Many.mutate = produce_mutate__frill__many(
            'arithmetic_expression_many',
            PRIORITY_ARITHMETIC,
            PRIORITY_MULTIPLY,
            PRIORITY_MULTIPLY,
            conjure_arithmetic_expression_many__with_frill,
        )

    CommaExpression_Many.mutate = produce_mutate__frill__many(
            'comma_expression_many',
            PRIORITY_TERNARY,
            PRIORITY_TERNARY,
            PRIORITY_TERNARY,
            conjure_comma_expression_many__with_frill,
        )

    CompareExpression_Many.mutate = produce_mutate__frill__many(
            'compare_expression_many',
            PRIORITY_COMPARE,
            PRIORITY_NORMAL,
            PRIORITY_NORMAL,
            conjure_compare_expression_many__with_frill,
        )

    LogicalOrExpression_Many.mutate = produce_mutate__frill__many(
            'logical_or_expression_many',
            PRIORITY_NORMAL,
            PRIORITY_LOGICAL_EXCLUSIVE_OR,
            PRIORITY_LOGICAL_EXCLUSIVE_OR,
            conjure_logical_or_expression_many__with_frill,
        )

    MultiplyExpression_Many.mutate = produce_mutate__frill__many(
            'multiply_expression_many',
            PRIORITY_MULTIPLY,
            PRIORITY_UNARY,
            PRIORITY_UNARY,
            conjure_multiply_expression_many__with_frill,
        )

    OrExpression_Many.mutate = produce_mutate__frill__many(
            'or_expression_many',
            PRIORITY_BOOLEAN_OR,
            PRIORITY_BOOLEAN_AND,
            PRIORITY_BOOLEAN_AND,
            conjure_or_expression_many__with_frill,
        )

    share(
        'conjure_and_expression_many',          conjure_and_expression_many,
        'conjure_arithmetic_expression_many',   conjure_arithmetic_expression_many,
        'conjure_comma_expression_many',        conjure_comma_expression_many,
        'conjure_compare_expression_many',      conjure_compare_expression_many,
        'conjure_logical_or_expression_many',   conjure_logical_or_expression_many,
        'conjure_multiply_expression_many',     conjure_multiply_expression_many,
        'conjure_or_expression_many',           conjure_or_expression_many,
    )

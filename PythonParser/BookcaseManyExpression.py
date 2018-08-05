#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseManyExpression')
def module():
    class Arguments_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = 'arguments-*'


        def first_argument(t):
            return t.many[0]


        scout_variables = scout_variables__many


    class ListExpression_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = '[*]'
        
        is_CRYSTAL_atom = true

        is_CRYSTAL_right_parenthesis = false


        scout_variables = scout_variables__many
        write_variables = write_variables__many


    class MapExpression_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = '{:*:}'
       
        is_CRYSTAL_atom = true

        is_CRYSTAL_right_parenthesis = false


        scout_variables = scout_variables__many


    class Parameters_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = 'parameter-(*)'


        def add_parameters(t, art):
            for v in t.many:
                v.add_parameters(art)


        def parameter_1_named(t, name):
            return 0


        def scout_variables(t, many):
            for v in t.many:
                v.scout_default_values(many)


    class TupleExpression_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = '{,*,}'

        is_CRYSTAL_atom = true

        is_CRYSTAL_right_parenthesis = false


        scout_variables = scout_variables__many


    [
        conjure_arguments_many, conjure_arguments_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'arguments-*',
            Arguments_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_list_expression_many, conjure_list_expression_many__with_frill
    ] = produce_conjure_bookcase_many_expression(
            'list-expression-*',
            ListExpression_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_map_expression_many, conjure_map_expression_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'map-expression-*',
            MapExpression_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_parameters_many, conjure_parameters_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'parameter-*',
            Parameters_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_tuple_expression_many, conjure_tuple_expression_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'tuple-expression-*',
            TupleExpression_Many,

            produce_conjure_with_frill = 1,
        )


    #
    #   .mutate
    #
    Arguments_Many.mutate = produce_mutate__frill__many(
                                'arguments_many',
                                PRIORITY_ASSIGN,
                                PRIORITY_ASSIGN,
                                PRIORITY_ASSIGN,
                                conjure_arguments_many__with_frill,
                            )

    ListExpression_Many.mutate = produce_mutate__frill__many(
                                     'list_expression_many',
                                     PRIORITY_COMPREHENSION,
                                     PRIORITY_TERNARY,
                                     PRIORITY_TERNARY,
                                     conjure_list_expression_many__with_frill,
                                 )

    MapExpression_Many.mutate = produce_mutate__frill__many(
                                    'list_expression_many',
                                    PRIORITY_COMPREHENSION,
                                    PRIORITY_MAP_ELEMENT,
                                    PRIORITY_MAP_ELEMENT,
                                    conjure_map_expression_many__with_frill,
                                )

    TupleExpression_Many.mutate = produce_mutate__frill__many(
                                    'tuple_expression_many',
                                    PRIORITY_TERNARY,
                                    PRIORITY_TERNARY,
                                    PRIORITY_TERNARY,
                                    conjure_tuple_expression_many__with_frill,
                                )

    #
    #   .mutate
    #
    Parameters_Many.transform = produce_transform__frill__many(
                                    'parameters_many',
                                    PRIORITY_ASSIGN,
                                    conjure_parameters_many__with_frill,
                                )


    share(
        'conjure_arguments_many',           conjure_arguments_many,
        'conjure_list_expression_many',     conjure_list_expression_many,
        'conjure_map_expression_many',      conjure_map_expression_many,
        'conjure_parameters_many',          conjure_parameters_many,
        'conjure_tuple_expression_many',    conjure_tuple_expression_many,
    )

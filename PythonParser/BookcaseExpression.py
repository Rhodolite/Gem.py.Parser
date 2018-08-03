#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseExpression')
def module():
    require_module('PythonParser.Elemental')
    require_module('PythonParser.Priority')
    require_module('PythonParser.TripleToken')


    LSB_RSB = conjure_vw_frill(LSB, RSB)


    class Arguments_1(BookcaseExpression):
        __slots__      = (())
        display_name   = 'arguments-(1)'
        frill          = LEFT_PARENTHESIS__RIGHT_PARENTHESIS
        is_arguments_1 = true

        scout_variables = scout_variables__a


    class HeadIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'head-index'
        frill        = conjure_vw_frill(LSB, COLON_RSB)

        scout_variables = scout_variables__a


    class ListExpression_1(BookcaseExpression):
        __slots__    = (())
        display_name = '[1]'
        frill        = LSB_RSB
        
        is_CRYSTAL_atom = true


        scout_variables = scout_variables__a
        write_variables = write_variables__a


    class MapExpression_1(BookcaseExpression):
        __slots__    = (())
        display_name = '{:1:}'
        frill        = conjure_vw_frill(conjure_left_brace ('{'), conjure_right_brace('}'))

        is_CRYSTAL_atom = true


        scout_variables = scout_variables__a


    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'normal-index'
        frill        = LSB_RSB

        scout_variables = scout_variables__a


    class Parameters_1(BookcaseExpression):
        __slots__       = (())
        display_name    = 'parameters-(1)'
        frill           = LEFT_PARENTHESIS__RIGHT_PARENTHESIS
        is_parameters_1 =  true


        def add_parameters(t, art):
            t.a.add_parameters(art)


        def parameter_1_named(t, name):
            return t.a.s == name


        def scout_variables(t, art):
            t.a.scout_default_values(art)


    class ParenthesizedTupleExpression_1(BookcaseExpression):
        __slots__    = (())
        display_name = '{,}'
        frill        = conjure_vw_frill(LEFT_PARENTHESIS, COMMA_RP)

        is_CRYSTAL_atom = true


        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a

            frill__2 = frill.morph (vary, 0, PRIORITY_TERNARY)
            a__2     = a    .mutate(vary, PRIORITY_TERNARY)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_parenthesized_tuple_expression_1__with_frill(frill__2, a__2)


        scout_variables = scout_variables__a


    class TailIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'tail-index'
        frill        = conjure_vw_frill(LSB_COLON, RSB)

        scout_variables = scout_variables__a


    [
        conjure_arguments_1, conjure_arguments_1_with_frill,
    ] = produce_conjure_bookcase_expression('arguments-1', Arguments_1)

    [
        conjure_head_index, conjure_head_index__with_frill,
    ] = produce_conjure_bookcase_expression('head-index', HeadIndex)

    [
        conjure_list_expression_1, conjure_list_expression_1__with_frill,
    ] = produce_conjure_bookcase_expression('list-expression-1', ListExpression_1)

    [
        conjure_map_expression_1, conjure_map_expression_1__with_frill,
    ] = produce_conjure_bookcase_expression('map-expression-1', MapExpression_1)

    [
        conjure_normal_index, conjure_normal_index__with_frill,
    ] = produce_conjure_bookcase_expression('normal-index', NormalIndex)

    [
        conjure_parameters_1, conjure_parameters_1__with_frill,
    ] = produce_conjure_bookcase_expression('parameters-1', Parameters_1)

    [
        conjure_tail_index, conjure_tail_index__with_frill,
    ] = produce_conjure_bookcase_expression('tail-index', TailIndex)

    [
        conjure_parenthesized_tuple_expression_1, conjure_parenthesized_tuple_expression_1__with_frill,
    ] = produce_conjure_bookcase_expression('parenthesized-tuple-expression-1', ParenthesizedTupleExpression_1)


    #
    #   .mutate
    #
    Arguments_1.mutate = produce_mutate__frill__a_with_priority(
                             'arguments_1',
                             PRIORITY_COMPREHENSION,
                             conjure_arguments_1_with_frill,
                         )

    HeadIndex.mutate = produce_mutate__frill__a_with_priority(
                           'head_index',
                           PRIORITY_TERNARY,
                           conjure_head_index__with_frill,
                       )


    ListExpression_1.mutate = produce_mutate__frill__a_with_priority(
                                  'list_expression_1',
                                  PRIORITY_COMPREHENSION,
                                  conjure_list_expression_1__with_frill,
                              )

    MapExpression_1.mutate = produce_mutate__frill__a_with_priority(
                                 'map_expression_1',
                                 PRIORITY_MAP_ELEMENT,
                                 conjure_map_expression_1__with_frill,
                             )

    NormalIndex.mutate = produce_mutate__frill__a_with_priority(
                             'normal_index',
                             PRIORITY_TERNARY,
                             conjure_normal_index__with_frill,
                         )

    ParenthesizedExpression.mutate = produce_mutate__frill__a_with_priority(
                                         'parenthesized_expression',
                                         PRIORITY_COMPREHENSION,
                                         conjure_parenthesized_expression__with_frill,
                                     )


    TailIndex.mutate = produce_mutate__frill__a_with_priority(
                           'tail_index',
                           PRIORITY_TERNARY,
                           conjure_tail_index__with_frill,
                       )


    #
    #   .transform
    #
    Parameters_1.transform = produce_transform__frill_a('parameters_1', conjure_parameters_1__with_frill)


    share(
        'conjure_arguments_1',                          conjure_arguments_1,
        'conjure_head_index',                           conjure_head_index,
        'conjure_list_expression_1',                    conjure_list_expression_1,
        'conjure_map_expression_1',                     conjure_map_expression_1,
        'conjure_normal_index',                         conjure_normal_index,
        'conjure_parameters_1',                         conjure_parameters_1,
        'conjure_parenthesized_expression',             conjure_parenthesized_expression,
        'conjure_parenthesized_tuple_expression_1',     conjure_parenthesized_tuple_expression_1,
        'conjure_tail_index',                           conjure_tail_index,
    )

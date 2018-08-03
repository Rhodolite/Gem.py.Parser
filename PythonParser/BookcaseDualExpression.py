#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseDualExpression')
def module():
    require_module('PythonParser.Elemental')


    class Arguments_2(BookcaseDualTwig):
        __slots__    = (())
        display_name = '(2)'
        frill        = conjure_vwx_frill(LP, COMMA__W, RP)


        def first_argument(t):
            return t.a


        scout_variables = scout_variables__ab


    class ListExpression_2(BookcaseDualTwig):
        __slots__    = (())
        display_name = '[2]'
        frill        = conjure_vwx_frill(LSB, COMMA__W, RSB)

        is_CRYSTAL_atom                       = true
        is_PYTHON__atom__or__special_operator = true
        is_PYTHON_special_operator            = false


        scout_variables = scout_variables__ab
        write_variables = write_variables__ab


    class RangeIndex(BookcaseDualTwig):
        __slots__    = (())
        display_name = 'range-index'
        frill        = conjure_vwx_frill(LSB, conjure_colon(' : '), RSB)

        scout_variables = scout_variables__ab


    class TupleExpression_2(BookcaseDualTwig):
        __slots__    = (())
        display_name = '{,2}'
        frill        = conjure_vwx_frill(LP, COMMA__W, RP)

        is_CRYSTAL_atom                       = true
        is_PYTHON__atom__or__special_operator = true
        is_PYTHON_special_operator            = false


        def mutate(t, vary, priority):
            if priority is PRIORITY_COMPREHENSION:
                element_priority = PRIORITY_TERNARY
            elif priority is PRIORITY_TERNARY:
                pass
            else:
                #my_line('priority: %d', priority)
                raise_unknown_line()

            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate(vary, priority)
            b__2     = b    .mutate(vary, priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_tuple_expression_2__with_frill(frill__2, a__2, b__2)


        scout_variables = scout_variables__ab


    [
        conjure_arguments_2, Arguments_2.conjure_plain, conjure_arguments_2__with_frill,
    ] = produce_conjure_bookcase_dual_twig(
            'arguments-2',
            Arguments_2,

            produce_conjure_plain = true,
        )

    [
        conjure_list_expression_2, conjure_list_expression_2__with_frill,
    ] = produce_conjure_bookcase_dual_twig('list-expression-2', ListExpression_2)

    [
        conjure_range_index, conjure_range_index__with_frill,
    ] = produce_conjure_bookcase_dual_twig('range-index', RangeIndex)

    [
        conjure_tuple_expression_2, conjure_tuple_expression_2__with_frill,
    ] = produce_conjure_bookcase_dual_twig('tuple-expression-2', TupleExpression_2)


    #
    #   .mutate
    #
    Arguments_2.mutate = produce_mutate__frill__ab_with_priority(
                             'arguments_2',
                             PRIORITY_ASSIGN,
                             PRIORITY_ASSIGN,
                             conjure_arguments_2__with_frill,
                         )

    ListExpression_2.mutate = produce_mutate__frill__ab_with_priority(
                                  'list_expression_2',
                                  PRIORITY_COMPREHENSION,
                                  PRIORITY_TERNARY,
                                  conjure_list_expression_2__with_frill,
                              )

    RangeIndex.mutate = produce_mutate__frill__ab_with_priority(
                            'range_index',
                            PRIORITY_SUBSCRIPT,
                            PRIORITY_SUBSCRIPT,
                            conjure_range_index__with_frill,
                        )


    share(
        'conjure_arguments_2',          conjure_arguments_2,
        'conjure_list_expression_2',    conjure_list_expression_2,
        'conjure_range_index',          conjure_range_index,
        'conjure_tuple_expression_2',   conjure_tuple_expression_2,
    )

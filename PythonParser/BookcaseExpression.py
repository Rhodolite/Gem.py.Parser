#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseExpression')
def module():
    require_module('PythonParser.DualToken')
    require_module('PythonParser.Elemental')
    require_module('PythonParser.Priority')
    require_module('PythonParser.TripleToken')


    LP_RP   = conjure_vw_frill(LP,  RP)
    LSB_RSB = conjure_vw_frill(LSB, RSB)


    @share
    class BookcaseExpression(ParserTrunk):
        __slots__ = ((
            'a',                        #   Expression+
        ))


        def __init__(t, a):
            t.a = a


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.a)


        def count_newlines(t):
            return t.a.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.a.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            r = frill.w.dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_a


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)


    BookcaseExpression.k1 = BookcaseExpression.a


    @share
    def produce_conjure_bookcase_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        def conjure_BookcaseExpression_WithFrill(a, frill):
            BookcaseExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseExpression_WithFrill is none:
                class BookcaseExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   DualFrill
                    ))


                    def __init__(t, a, frill):
                        t.a     = a
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.frill)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            return arrange('<%s+frill %s %s %s>',
                                           t.display_name,
                                           frill.v.display_token(),
                                           t.a    .display_token(),
                                           frill.w.display_token())


                write = attribute(Meta, 'write__frill', none)

                if write is not none:
                    BookcaseExpression_WithFrill.write = write


                #BookcaseExpression_WithFrill.k2 = BookcaseExpression_WithFrill.frill


                if python_debug_mode:
                    BookcaseExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseExpression_WithFrill)

            return BookcaseExpression_WithFrill(a, frill)


        conjure_dual__with_frill = produce_conjure_dual__21(
                                       name + '__X2',
                                       conjure_BookcaseExpression_WithFrill,
                                       cache,
                                       lookup,
                                       store,
                                   )

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w


        @rename('conjure_%s', name)
        def conjure_bookcase_expression(frill_v, a, frill_w):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w):
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__with_frill(a, conjure_vw_frill(frill_v, frill_w))


        @rename('conjure_%s__with_frill', name)
        def conjure_with_frill(frill, a):
            if frill is meta_frill:
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__with_frill(a, frill)


        if python_debug_mode:
            append_cache(name, cache)


        return ((
                   conjure_bookcase_expression,
                   conjure_with_frill,
               ))


    class Arguments_1(BookcaseExpression):
        __slots__      = (())
        class_order    = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name   = 'arguments-(1)'
        frill          = LP_RP
        is_arguments_1 = true

        scout_variables = scout_variables__a


    class HeadIndex(BookcaseExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'head-index'
        frill        = conjure_vw_frill(LSB, COLON_RSB)

        scout_variables = scout_variables__a


    class ListExpression_1(BookcaseExpression):
        __slots__                              = (())
        class_order                            = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name                           = '[1]'
        frill                                  = LSB_RSB
        is_CRYSTAL__atom__or__special_operator = true
        is_CRYSTAL_atom                        = true
        is_CRYSTAL_special_operator            = false

        scout_variables = scout_variables__a
        write_variables = write_variables__a


    class MapExpression_1(BookcaseExpression):
        __slots__                              = (())
        class_order                            = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name                           = '{:1:}'
        frill                                  = conjure_vw_frill(conjure_left_brace ('{'), conjure_right_brace('}'))
        is_CRYSTAL__atom__or__special_operator = true
        is_CRYSTAL_atom                        = true
        is_CRYSTAL_special_operator            = false

        scout_variables = scout_variables__a


    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name = 'normal-index'
        frill        = LSB_RSB

        scout_variables = scout_variables__a


    class Parameters_1(BookcaseExpression):
        __slots__       = (())
        class_order     = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name    = 'parameters-(1)'
        frill           = LP_RP
        is_parameters_1 =  true


        def add_parameters(t, art):
            t.a.add_parameters(art)


        def parameter_1_named(t, name):
            return t.a.s == name


        def scout_variables(t, art):
            t.a.scout_default_values(art)


    class ParenthesizedExpression(BookcaseExpression):
        __slots__                              = (())
        class_order                            = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name                           = '()'
        frill                                  = LP_RP
        is_CRYSTAL__atom__or__special_operator = true
        is_CRYSTAL_atom                        = true
        is_CRYSTAL_special_operator            = false

        scout_variables = scout_variables__a


    class ParenthesizedTupleExpression_1(BookcaseExpression):
        __slots__                              = (())
        class_order                            = CLASS_ORDER__BOOKCASE_EXPRESSION
        display_name                           = '{,}'
        frill                                  = conjure_vw_frill(LP, COMMA_RP)
        is_CRYSTAL__atom__or__special_operator = true
        is_CRYSTAL_atom                        = true
        is_CRYSTAL_special_operator            = false


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
        class_order  = CLASS_ORDER__BOOKCASE_EXPRESSION
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
        conjure_parenthesized_expression, conjure_parenthesized_expression__with_frill,
    ] = produce_conjure_bookcase_expression('parenthesized-expression', ParenthesizedExpression)

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

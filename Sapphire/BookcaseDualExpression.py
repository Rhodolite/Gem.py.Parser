#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.BookcaseDualExpression')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.TripleFrill')


    bookcase_dual_expression_with_frill_cache  = create_cache('bookcase-dual-expression-with-frill', conjure_nub)
    lookup_bookcase_dual_expression_with_frill = bookcase_dual_expression_with_frill_cache.lookup
    store_bookcase_dual_expression_with_frill  = bookcase_dual_expression_with_frill_cache.store


    @share
    class BookcaseDualExpression(DualTwig):
        k3 = none


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines() + t.frill.count_newlines()


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            frill    .w.dump_token(f)
            t        .b.dump_token(f)
            r = frill.x.dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_ab


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)


    BookcaseDualExpression.k1 = BookcaseDualExpression.a
    BookcaseDualExpression.k2 = BookcaseDualExpression.b


    @share
    def produce_conjure_bookcase_dual_expression(
            name,
            Meta,

            produce_conjure_plain      = false,
            produce_conjure_with_frill = false,
    ):
        assert type(produce_conjure_plain)      is Boolean
        assert (type(produce_conjure_with_frill) is Boolean) or (produce_conjure_with_frill is 1)

        cache = create_cache(name, conjure_nub)


        def conjure_Meta_WithFrill(frill, a, b):
            BookcaseDualExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseDualExpression_WithFrill is none:
                class BookcaseDualExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   TripleFrill
                    ))


                    def __init__(t, frill, a, b):
                        t.frill = frill
                        t.a     = a
                        t.b     = b


                    def __repr__(t):
                        return arrange('<%s %r %r %r>', t.__class__.__name__, t.frill, t.a, t.b)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            return arrange('<%s+frill %s %s %s %s %s>',
                                           t.display_name,
                                           frill.v.display_token(),
                                           t.a    .display_token(),
                                           frill.w.display_token(),
                                           t.b    .display_token(),
                                           frill.x.display_token())


                BookcaseDualExpression_WithFrill.k1 = BookcaseDualExpression_WithFrill.frill
                BookcaseDualExpression_WithFrill.k2 = BookcaseDualExpression_WithFrill.a
                BookcaseDualExpression_WithFrill.k3 = BookcaseDualExpression_WithFrill.b


                write = attribute(Meta, 'write__frill', none)


                if write is not none:
                    BookcaseDualExpression_WithFrill.write = write


                if __debug__:
                    BookcaseDualExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseDualExpression_WithFrill)

            return BookcaseDualExpression_WithFrill(frill, a, b)


        conjure_dual = produce_conjure_unique_dual(name, Meta, cache)

        conjure_triple_with_frill = produce_conjure_unique_triple(
                                        name,
                                        conjure_Meta_WithFrill,
                                        bookcase_dual_expression_with_frill_cache,
                                        lookup_bookcase_dual_expression_with_frill,
                                        store_bookcase_dual_expression_with_frill,
                                    )

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w
        meta_frill_x = meta_frill.x


        @rename('conjure_%s', name)
        def conjure_bookcase_dual_expression(frill_v, a, frill_w, b, frill_x):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w) and (frill_x is meta_frill_x):
                return conjure_dual(a, b)

            return conjure_triple_with_frill(conjure_vwx_frill(frill_v, frill_w, frill_x), a, b)


        if produce_conjure_with_frill:
            @rename('conjure_%s__with_frill', name)
            def conjure_with_frill(frill, a, b):
                if frill is meta_frill:
                    return conjure_dual(a, b)

                return conjure_triple_with_frill(frill, a, b)


            if produce_conjure_plain:
                return ((
                           conjure_bookcase_dual_expression,
                           static_method(conjure_dual),
                           (conjure_with_frill   if produce_conjure_with_frill is 1 else   static_method(conjure_with_frill)),
                       ))

            return ((
                       conjure_bookcase_dual_expression,
                       (conjure_with_frill   if produce_conjure_with_frill is 1 else   static_method(conjure_with_frill)),
                   ))

        if produce_conjure_plain:
            return ((
                       conjure_bookcase_dual_expression,
                       static_method(conjure_dual),
                   ))

        return conjure_bookcase_dual_expression


    class Arguments_2(BookcaseDualExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION
        display_name = '(2)'
        frill        = conjure_vwx_frill(LP, COMMA__W, RP)

        scout_variables = scout_variables__ab


    class ListExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION
        display_name                   = '[2]'
        frill                          = conjure_vwx_frill(LSB, COMMA__W, RSB)
        is__atom__or__special_operator = true
        is_atom                        = true
        is_special_operator            = false

        scout_variables = scout_variables__ab
        write_variables = write_variables__ab


    class RangeIndex(BookcaseDualExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION
        display_name = 'range-index'
        frill        = conjure_vwx_frill(LSB, conjure_colon(' : '), RSB)

        scout_variables = scout_variables__ab


    class TupleExpression_2(BookcaseDualExpression):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION
        display_name                   = '{,2}'
        frill                          = conjure_vwx_frill(LP, COMMA__W, RP)
        is__atom__or__special_operator = true
        is_atom                        = true
        is_special_operator            = false


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
    ] = produce_conjure_bookcase_dual_expression(
            'arguments-2',
            Arguments_2,

            produce_conjure_plain      = true,
            produce_conjure_with_frill = 1,
        )

    [
        conjure_list_expression_2, conjure_list_expression_2__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'list-expression-2',
            ListExpression_2,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_range_index, conjure_range_index__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'range-index',
            RangeIndex,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_tuple_expression_2, conjure_tuple_expression_2__with_frill,
    ] = produce_conjure_bookcase_dual_expression(
            'tuple-expression-2',
            TupleExpression_2,

            produce_conjure_with_frill = 1,
        )


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

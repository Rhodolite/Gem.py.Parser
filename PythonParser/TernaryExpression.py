#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TernaryExpression')
def module():
    triple_expression_with_frill_cache  = create_cache('triple-expression-with-frill')
    lookup_triple_expression_with_frill = triple_expression_with_frill_cache.lookup
    store_triple_expression_with_frill  = triple_expression_with_frill_cache.store



    class TripleExpression(TripleTwig):
        __slots__ = (())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            frill.v.dump_token(f)
            t    .b.dump_token(f)
            frill.w.dump_token(f)
            r = t.c.dump_token(f, false)

            return f.token_result(r, newline)


        order           = order__frill_abc
        scout_variables = scout_variables__abc


        def write(t, w):
            frill = t.frill

            t.a.write(w)
            w(frill.v.s)
            t.b.write(w)
            w(frill.w.s)
            t.c.write(w)


    def produce_conjure_triple_expression(
            name, Meta,

            produce_conjure_with_frill = false,
    ):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_Meta_WithFrill(a, b, c, frill):
            TripleExpression_WithFrill = lookup_adjusted_meta(Meta)

            if TripleExpression_WithFrill is none:
                class TripleExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   DualFrill
                    ))


                    def __init__(t, a, b, c, frill):
                        t.a     = a
                        t.b     = b
                        t.c     = c
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.frill)


                    def count_newlines(t):
                        return (
                                     t.a    .count_newlines()
                                   + t.b    .count_newlines()
                                   + t.c    .count_newlines()
                                   + t.frill.count_newlines()
                               )


                    def display_token(t):
                        frill = t.frill

                        return arrange('<%s+frill %s %s %s %s %s>',
                                       t.display_name,
                                       t.a    .display_token(),
                                       frill.v.display_token(),
                                       t.b    .display_token(),
                                       frill.w.display_token(),
                                       t.c    .display_token())


                TripleExpression_WithFrill.k4 = TripleExpression_WithFrill.frill

                if __debug__:
                    TripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, TripleExpression_WithFrill)

            return TripleExpression_WithFrill(a, b, c, frill)


        conjure_triple = produce_conjure_triple(name + '__X3', Meta, cache, lookup, store)

        conjure_quadruple = produce_conjure_quadruple__4123(
                                name,
                                conjure_Meta_WithFrill,
                                triple_expression_with_frill_cache,
                                lookup_triple_expression_with_frill,
                                store_triple_expression_with_frill,
                            )

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w


        @rename('conjure_%s', name)
        def conjure_triple_expression(a, frill_v, b, frill_w, c):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w):
                return conjure_triple(a, b, c)

            return conjure_quadruple(a, b, c, conjure_vw_frill(frill_v, frill_w))


        if produce_conjure_with_frill:
            @rename('conjure_%s__with_frill', name)
            def conjure_with_frill(frill, a, b, c):
                if frill is meta_frill:
                    return conjure_triple(a, b, c)

                return conjure_quadruple(a, b, c, frill)


            return ((
                       conjure_triple_expression,
                       conjure_with_frill,
                   ))


        return conjure_triple_expression


    @privileged
    def produce_mutate_triple_expression(
            name, frill_priority, a_priority, b_priority, c_priority, conjure_with_frill,
    ):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b
            c     = t.c

            frill__2 = frill.morph (vary, frill_priority, frill_priority)
            a__2     = a    .mutate(vary, a_priority)
            b__2     = b    .mutate(vary, b_priority)
            c__2     = c    .mutate(vary, c_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2) and (c is c__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2, c__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    class ComprehensionForExpression(TripleExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__TRIPLE_EXPRESSION
        display_name = 'comprehension-for'
        frill        = conjure_vw_frill(W__FOR__W, W__IN__W)


    class TernaryExpression(TripleExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__TRIPLE_EXPRESSION
        display_name = '?:'
        frill        = conjure_vw_frill(W__IF__W, W__ELSE__W)


    [
        conjure_comprehension_for, conjure_comprehension_for__with_frill,
    ] = produce_conjure_triple_expression(
            'comprehension-for',
            ComprehensionForExpression,

            produce_conjure_with_frill = true,
        )

    [
        conjure_ternary_expression, conjure_ternary_expression__with_frill,
    ] = produce_conjure_triple_expression(
            'ternary-expression',
            TernaryExpression,

            produce_conjure_with_frill = true,
        )


    #
    #   .mutate
    #
    ComprehensionForExpression.mutate = produce_mutate_triple_expression(
                                            'comprehension_for_expression',
                                            PRIORITY_ASSIGN,
                                            PRIORITY_TERNARY,
                                            PRIORITY_ASSIGN,
                                            PRIORITY_TERNARY_LIST,
                                            conjure_comprehension_for__with_frill,
                                       )

    TernaryExpression.mutate = produce_mutate_triple_expression(
                                   'ternary_expression',
                                   PRIORITY_TERNARY,
                                   PRIORITY_BOOLEAN_OR,
                                   PRIORITY_BOOLEAN_OR,
                                   PRIORITY_TERNARY,
                                   conjure_ternary_expression__with_frill,
                              )


    share(
        'conjure_comprehension_for',    conjure_comprehension_for,
        'conjure_ternary_expression',   conjure_ternary_expression,
    )

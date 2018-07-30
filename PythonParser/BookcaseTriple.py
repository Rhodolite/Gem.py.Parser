#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseTriple')
def module():
    require_module('PythonParser.QuadrupleFrill')


    triple_expression_cache  = create_cache('triple-expression', conjure_nub)
    lookup_triple_expression = triple_expression_cache.get
    store_triple_expression  = triple_expression_cache.__setitem__


    @share
    class BookcaseTripleExpression(TripleTwig):
        __slots__ = (())


        class_order = CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION


        def count_newlines(t):
            return (
                         t.a    .count_newlines()
                       + t.b    .count_newlines()
                       + t.c    .count_newlines()
                       + t.frill.count_newlines()
                   )


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            frill    .w.dump_token(f)
            t        .b.dump_token(f)
            frill    .x.dump_token(f)
            t        .c.dump_token(f)
            r = frill.y.dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_abc


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)
            t.c.write(w)
            w(frill.y.s)


    def produce_conjure_bookcase_triple_expression(name, Meta):
        cache  = create_cache(name, conjure_nub)
        lookup = cache.lookup
        store  = cache.store


        def conjure_Meta_WithFrill(a, b, c, frill):
            BookcaseTripleExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseTripleExpression_WithFrill is none:
                class BookcaseTripleExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   QuadrupleFrill
                    ))


                    def __init__(t, a, b, c, frill):
                        t.a     = a
                        t.b     = b
                        t.c     = c
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.frill)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            frill_v = frill.v

                            return arrange('<%s+frill %+d %s %s %s %s %s %s %s>',
                                           t.display_name,
                                           frill_v.a.total,
                                           frill_v.b.display_token(),
                                           t      .a.display_token(),
                                           frill  .w.display_token(),
                                           t      .b.display_token(),
                                           frill  .x.display_token(),
                                           t      .c.display_token(),
                                           frill  .y.display_token())


                BookcaseTripleExpression_WithFrill.k4 = BookcaseTripleExpression_WithFrill.frill


                if python_debug_mode:
                    BookcaseTripleExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseTripleExpression_WithFrill)

            return BookcaseTripleExpression_WithFrill(a, b, c, frill)


        conjure_triple = produce_conjure_unique_triple(name, Meta, cache, lookup, store)

        conjure_quadruple = produce_conjure_quadruple__4123(
                                name,
                                conjure_Meta_WithFrill,
                                triple_expression_cache,
                                lookup_triple_expression,
                                store_triple_expression,
                            )

        meta_frill_v = Meta.frill.v
        meta_frill_w = Meta.frill.w
        meta_frill_x = Meta.frill.x
        meta_frill_y = Meta.frill.y


        @rename('conjure_%s', name)
        def conjure_bookcase_triple(frill_v, a, frill_w, b, frill_x, c, frill_y):
            if (
                       frill_v is meta_frill_v
                   and frill_w is meta_frill_w
                   and frill_x is meta_frill_x
                   and frill_y is meta_frill_y
            ):
                return conjure_triple(a, b, c)

            return conjure_quadruple(a, b, c, conjure_vwxy_frill(frill_v, frill_w, frill_x, frill_y))


        return conjure_bookcase_triple


    class RaiseStatement_3(BookcaseTripleExpression):
        __slots__    = (())
        display_name = 'raise-statement-3'
        frill        = conjure_vwxy_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_with('raise ')),
                           COMMA__W,
                           COMMA__W,
                           LINE_MARKER,
                       )

        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        @property
        def indentation(t):
            return t.frill.v.a


    conjure_raise_statement_3 = produce_conjure_bookcase_triple_expression('raise-statement-3', RaiseStatement_3)


    share(
        'conjure_raise_statement_3',    conjure_raise_statement_3,
    )

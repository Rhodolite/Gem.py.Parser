#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.BookcaseDualTwig')
def module():
    require_module('CoreParser.Core')
    require_module('CoreParser.DualTwig')


    bookcase_dual_twig_with_frill_cache  = create_cache('bookcase-dual-twig-with-frill', conjure_nub)
    lookup_bookcase_dual_twig_with_frill = bookcase_dual_twig_with_frill_cache.lookup
    store_bookcase_dual_twig_with_frill  = bookcase_dual_twig_with_frill_cache.store


    @export
    class BookcaseDualTwig(DualTwig):
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


        if capital_global.python_parser:
            order = order__frill_ab


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)


    BookcaseDualTwig.k1 = BookcaseDualTwig.a
    BookcaseDualTwig.k2 = BookcaseDualTwig.b
    BookcaseDualTwig.k3 = none


    @export
    def produce_conjure_bookcase_dual_twig(
            name, Meta,

            produce_conjure_plain = false,
    ):
        assert type(produce_conjure_plain) is Boolean

        cache = create_cache(name, conjure_nub)


        def conjure_Meta_WithFrill(frill, a, b):
            BookcaseDualTwig_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseDualTwig_WithFrill is none:
                class BookcaseDualTwig_WithFrill(Meta):
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


                BookcaseDualTwig_WithFrill.k1 = BookcaseDualTwig_WithFrill.frill
                BookcaseDualTwig_WithFrill.k2 = BookcaseDualTwig_WithFrill.a
                BookcaseDualTwig_WithFrill.k3 = BookcaseDualTwig_WithFrill.b


                write = attribute(Meta, 'write__frill', none)


                if write is not none:
                    BookcaseDualTwig_WithFrill.write = write


                if __debug__:
                    BookcaseDualTwig_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseDualTwig_WithFrill)

            return BookcaseDualTwig_WithFrill(frill, a, b)


        conjure_dual = produce_conjure_unique_dual(name, Meta, cache)

        conjure_triple_with_frill = produce_conjure_unique_triple(
                                        name,
                                        conjure_Meta_WithFrill,
                                        bookcase_dual_twig_with_frill_cache,
                                        lookup_bookcase_dual_twig_with_frill,
                                        store_bookcase_dual_twig_with_frill,
                                    )

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w
        meta_frill_x = meta_frill.x


        @rename('conjure_%s', name)
        def conjure_bookcase_dual_twig(frill_v, a, frill_w, b, frill_x):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w) and (frill_x is meta_frill_x):
                return conjure_dual(a, b)

            return conjure_triple_with_frill(conjure_vwx_frill(frill_v, frill_w, frill_x), a, b)


        @rename('conjure_%s__with_frill', name)
        def conjure_bookcase_dual_twig__with_frill(frill, a, b):
            if frill is meta_frill:
                return conjure_dual(a, b)

            return conjure_triple_with_frill(frill, a, b)


        if produce_conjure_plain:
            return ((
                       conjure_bookcase_dual_twig,
                       static_method(conjure_dual),
                       conjure_bookcase_dual_twig__with_frill,
                   ))

        return ((
                   conjure_bookcase_dual_twig,
                   conjure_bookcase_dual_twig__with_frill,
               ))

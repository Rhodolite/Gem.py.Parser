#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.BookcaseCoupleTwig')
def gem():
    require_gem('CoreParser.Core')
    require_gem('CoreParser.DualTwig')


    #
    #   BookcaseCoupleTwig:
    #
    #       A "bookcase" around a "couple".
    #
    #           There is *NO* frill between the two "couple" members.
    #           Thus there is *ONLY* frill before & after the "couple".
    #
    #       Contrast to the much more common 'BookcaseDualTwig':
    #
    #           This has the more typical:
    #
    #               Frill before, Frill between, & Frill after.
    #
    #   Other differences:
    #
    #       Also a `BookcaseCoupleTwig` *ALWAYS* comes with a `.frill` member (and does not
    #       have a `.frill` class member).
    #
    #       Contrast to the much more common 'BookcaseDualTwig':
    #
    #           It has a default `.frill` class member; and when it wants a different `.frill`
    #           member it calls `conjure_Meta_WithFrill` to dynamically create a derived
    #           class with a `.frill` member.
    #
    @export
    class BookcaseCoupleTwig(DualTwig):
        __slots__ = ((
            'frill',
        ))


        __init__ = construct__123


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.frill, t.a, t.b)


        def count_newlines(t):
            return t.frill.count_newlines() + t.a.count_newlines() + t.a.count_newlines()


        def dump_token(t, f, newline = true):
            frill = t.frill
            
            f.partial('<%s +%d ', t.display_name, frill.v.total)

            t        .a.dump_token(f)
            t        .b.dump_token(f)
            r = frill.w.dump_token(f, false)

            return f.token_result(r, newline)


        def display_token(t):
            frill = t.frill

            return arrange('<%s +%d%s %s %s>',
                           t.display_name,
                           frill.v.total,
                           t    .a.display_token(),
                           t    .b.display_token(),
                           frill.w.display_token())


        if gem_global.python_parser:
            order = order__frill_ab


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            t.b .write(w)
            w(frill.w.s)


    BookcaseCoupleTwig.k1 = BookcaseCoupleTwig.frill
    BookcaseCoupleTwig.k2 = BookcaseCoupleTwig.a
    BookcaseCoupleTwig.k3 = BookcaseCoupleTwig.b


    @export
    def produce_conjure_bookcase_couple_twig(name, meta):
        cache = create_cache(name, conjure_nub)

        return produce_conjure_unique_triple__312(name, meta, cache)

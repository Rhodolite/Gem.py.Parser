#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.DualTwig')
def gem():
    require_gem('Sapphire.Tree')


    dual_twig_cache  = {}
    lookup_dual_twig = dual_twig_cache.get
    store_dual_twig  = dual_twig_cache.__setitem__


    @share
    def construct__ab(t, a, b):
        t.a = a
        t.b = b


    @share
    def portray__ab(t):
        return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


    @share
    def count_newlines__ab(t):
        return t.a.count_newlines() + t.b.count_newlines()


    @share
    def display_token__ab(t):
        return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


    @share
    class DualTwig(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
        ))


        __init__       = construct__ab
        __repr__       = portray__ab
        count_newlines = count_newlines__ab
        display_token  = display_token__ab


        def dump_token(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            r = t.b.dump_token(f, false)

            return f.token_result(r, newline)


        order = order__ab


        def write(t, w):
            t.a.write(w)
            t.b.write(w)


    DualTwig.k1 = DualTwig.a
    DualTwig.k2 = DualTwig.b


    @share
    def produce_conjure_dual_twig(name, Meta):
        return produce_conjure_dual__21(name, Meta, dual_twig_cache, lookup_dual_twig, store_dual_twig)


    append_cache('dual-twig', dual_twig_cache)

#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.QuadrupleTwig')
def gem():
    @share
    def construct__abcd(t, a, b, c, d):
        t.a = a
        t.b = b
        t.c = c
        t.d = d


    @share
    def count_newlines__abcd(t):
        return t.a.count_newlines() + t.b.count_newlines() + t.c.count_newlines() + t.d.count_newlines()


    @share
    def display_token__abcd(t):
        return arrange('<%s %s %s %s %s>',
                       t.display_name,
                       t.a.display_token(),
                       t.b.display_token(),
                       t.c.display_token(),
                       t.d.display_token())


    @share
    def portray__abcd(t):
        return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.d)


    @share
    class QuadrupleTwig(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'd',                        #   Any
        ))


        __init__       = construct__abcd
        __repr__       = portray__abcd
        count_newlines = count_newlines__abcd
        display_token  = display_token__abcd


        def dump_token(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            t    .b.dump_token(f)
            t    .c.dump_token(f)
            r = t.d.dump_token(f, false)

            return f.token_result(r, newline)


        def write(t, w):
            t.a.write(w)
            t.b.write(w)
            t.c.write(w)
            t.d.write(w)


    QuadrupleTwig.k1 = QuadrupleTwig.a
    QuadrupleTwig.k2 = QuadrupleTwig.b
    QuadrupleTwig.k3 = QuadrupleTwig.c
    QuadrupleTwig.k4 = QuadrupleTwig.d


    @share
    def produce_conjure_quadruple_twig(name, Meta):
        return produce_conjure_quadruple__4123(name, Meta, create_cache(name, conjure_nub))

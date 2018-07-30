#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.DualTwig')
def module():
    require_module('CoreParser.Cache')
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.Method')
    require_module('CoreParser.ParserTrunk')


    dual_twig_cache  = {}
    lookup_dual_twig = dual_twig_cache.get
    store_dual_twig  = dual_twig_cache.__setitem__


    @export
    class DualTwig(ParserTrunk):
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


        if capital_global.python_parser:
            order = order__ab


        def write(t, w):
            t.a.write(w)
            t.b.write(w)


    DualTwig.k1 = DualTwig.a
    DualTwig.k2 = DualTwig.b


    @export
    def produce_conjure_dual_twig(name, Meta):
        return produce_conjure_dual__21(name, Meta, dual_twig_cache, lookup_dual_twig, store_dual_twig)


    append_cache('dual-twig', dual_twig_cache)

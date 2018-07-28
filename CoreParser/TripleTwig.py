#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.TripleTwig')
def gem():
    require_gem('CoreParser.Method')


    @export
    class TripleTwig(ParserTrunk):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
        ))


        __init__       = construct__123
        __repr__       = portray__123
        count_newlines = count_newlines__123
        display_token  = display_token__123
        dump_token     = dump_token__123
        write          = write__123


    TripleTwig.k1 = TripleTwig.a
    TripleTwig.k2 = TripleTwig.b
    TripleTwig.k3 = TripleTwig.c


    @export
    def produce_conjure_triple_twig(name, Meta):
        cache = create_cache(name, conjure_nub)

        return produce_conjure_unique_triple__312(name, Meta, cache)

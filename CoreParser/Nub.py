#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Nub')
def module():
    require_module('CoreParser.Core')


    nub_cache   = create_cache('nub')
    lookup_nub  = nub_cache.lookup
    provide_nub = nub_cache.provide


    class Nub(Object):
        __slots__ = ((
            'a',                        #   Any
        ))


        herd_estimate = 0
        is_herd       = false


        def __init__(t, a):
            t.a = a


        def __ge__(a, b):
            return a.a.order(b.a) >= 0


        def __gt__(a, b):
            return a.a.order(b.a) > 0


        def __le__(a, b):
            return a.a.order(b.a) <= 0


        def __lt__(a, b):
            return a.a.order(b.a) < 0


        def display_token(t):
            return arrange('<nub %s>', t.a.display_token())


    @export
    def conjure_nub(a):
        return (lookup_nub(a)) or (provide_nub(a, Nub(a)))


    export(
        'static_conjure_nub',   static_method(conjure_nub),
    )

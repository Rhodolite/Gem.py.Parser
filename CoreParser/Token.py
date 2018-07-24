#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.Token')
def gem():
    @export
    class Token(Object):
        __slots__ = ((
            's',
        ))


        def __init__(t, s):
            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.s)


        display_token = __repr__


        def write(t, w):
            w(t.s)


    @export
    class Identifier(Token):
        __slots__    = (())
        display_name = 'Identifier'


        def display_token(t):
            return t.s



    [
            conjure_identifier, lookup_identifier,
    ] = produce_cache_functions(
            'identifier', Identifier,

            produce_conjure_by_name = true,
            produce_lookup          = true,
        )


    export(
        'conjure_identifier',   conjure_identifier,
        'lookup_identifier',    lookup_identifier,
    )
